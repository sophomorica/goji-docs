#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { mkdtemp } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { setTimeout as sleep } from 'node:timers/promises';

const args = parseArgs(process.argv.slice(2));
const feature = required(args, 'feature');
const baseUrl = required(args, 'base-url').replace(/\/$/, '');
const evidenceDir = required(args, 'evidence-dir');
const chromeBin = resolveChrome(args['chrome-bin']);

const FEATURES = {
  'studio-board': driveStudioBoard,
  'studio-notes': driveStudioNotes,
  'studio-zoom': driveStudioZoom,
  'studio-child-tabs': driveStudioChildTabs,
  'lesson-living': driveLessonLiving,
  'lesson-practice': driveLessonPractice,
  'studio-walk': driveStudioWalk,
};

if (!FEATURES[feature]) {
  fail(`unknown feature ${feature}. Known: ${Object.keys(FEATURES).join(', ')}`);
}

mkdirSync(evidenceDir, { recursive: true });
const chrome = await launchChrome(chromeBin);
let code = 1;
try {
  const page = await chrome.connect();
  const result = await FEATURES[feature](page);
  writeFileSync(join(evidenceDir, 'action.json'), `${JSON.stringify(result, null, 2)}\n`);
  writeFileSync(join(evidenceDir, 'state.txt'), `${result.stateText}\n`);
  process.stdout.write(`drove ${feature}\n${result.stateText}\n`);
  code = 0;
} finally {
  await chrome.close();
  process.exit(code);
}

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 1) {
    const key = argv[i];
    if (!key.startsWith('--')) fail(`unexpected argument ${key}`);
    out[key.slice(2)] = argv[i + 1];
    i += 1;
  }
  return out;
}

function required(map, key) {
  if (!map[key]) fail(`missing --${key}`);
  return map[key];
}

function resolveChrome(explicit) {
  if (explicit === '/usr/local/bin/google-chrome') {
    fail('refusing /usr/local/bin/google-chrome because it pins the shared profile');
  }
  if (explicit && explicit !== 'google-chrome') return explicit;
  const candidates = [
    '/opt/google/chrome/chrome',
    '/usr/bin/google-chrome-stable',
    '/usr/bin/google-chrome',
  ];
  for (const bin of candidates) {
    if (existsSync(bin)) return bin;
  }
  return 'google-chrome';
}

function fail(message) {
  process.stderr.write(`drive: ${message}\n`);
  throw new Error(message);
}

function assert(cond, message) {
  if (!cond) fail(message);
}

async function launchChrome(bin) {
  const userData = await mkdtemp(join(tmpdir(), 'goji-docs-chrome-'));
  const child = spawn(
    bin,
    [
      '--headless=new',
      '--no-sandbox',
      '--disable-gpu',
      '--disable-dev-shm-usage',
      '--disable-crash-reporter',
      '--remote-debugging-port=0',
      `--user-data-dir=${userData}`,
      `--crash-dumps-dir=${userData}`,
      '--force-prefers-reduced-motion',
      'about:blank',
    ],
    { stdio: 'ignore', detached: true },
  );
  const closed = new Promise((resolve) => child.once('exit', resolve));
  let ws;
  try {
    const port = await waitForDevtoolsPort(userData, child);
    const version = await waitJson(`http://127.0.0.1:${port}/json/version`);
    ws = new WebSocket(version.webSocketDebuggerUrl);
    await onceOpen(ws);
    const session = cdpSession(ws);
    return {
      async connect() {
        const { targetId } = await session.send('Target.createTarget', { url: 'about:blank' });
        const { sessionId } = await session.send('Target.attachToTarget', { targetId, flatten: true });
        const page = session.session(sessionId);
        await page.send('Page.enable');
        await page.send('Runtime.enable');
        await page.send('Emulation.setEmulatedMedia', {
          features: [{ name: 'prefers-reduced-motion', value: 'reduce' }],
        });
        return page;
      },
      async close() {
        try { ws?.close(); } catch {}
        try { process.kill(-child.pid, 'SIGKILL'); } catch {}
        try { child.kill('KILL'); } catch {}
        await Promise.race([closed, sleep(1500)]);
        try { child.unref(); } catch {}
        rmSync(userData, { recursive: true, force: true });
      },
    };
  } catch (err) {
    try { ws?.close(); } catch {}
    try { process.kill(-child.pid, 'SIGKILL'); } catch {}
    try { child.kill('KILL'); } catch {}
    await Promise.race([closed, sleep(1500)]);
    try { child.unref(); } catch {}
    rmSync(userData, { recursive: true, force: true });
    throw err;
  }
}

async function waitForDevtoolsPort(userData, child) {
  const portFile = join(userData, 'DevToolsActivePort');
  for (let i = 0; i < 80; i += 1) {
    if (child.exitCode !== null) {
      fail(`chrome exited ${child.exitCode} before DevTools became ready`);
    }
    try {
      const first = readFileSync(portFile, 'utf8').split('\n')[0].trim();
      if (/^\d+$/.test(first)) return first;
    } catch {}
    await sleep(100);
  }
  fail('chrome DevTools port did not appear');
}

async function waitJson(url) {
  for (let i = 0; i < 40; i += 1) {
    try {
      const res = await fetch(url);
      if (res.ok) return res.json();
    } catch {}
    await sleep(100);
  }
  fail(`chrome HTTP ${url} did not answer`);
}

function onceOpen(ws) {
  return new Promise((resolve, reject) => {
    ws.addEventListener('open', () => resolve(), { once: true });
    ws.addEventListener('error', () => reject(new Error('chrome websocket failed')), { once: true });
  });
}

function cdpSession(ws) {
  let nextId = 1;
  const pending = new Map();
  ws.addEventListener('message', (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending.has(msg.id)) {
      const { resolve, reject } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) reject(new Error(msg.error.message || JSON.stringify(msg.error)));
      else resolve(msg.result || {});
    }
  });
  function send(method, params = {}, sessionId) {
    const id = nextId;
    nextId += 1;
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    ws.send(JSON.stringify(payload));
    return new Promise((resolve, reject) => {
      pending.set(id, { resolve, reject });
      setTimeout(() => {
        if (pending.has(id)) {
          pending.delete(id);
          reject(new Error(`cdp timeout ${method}`));
        }
      }, 15000);
    });
  }
  return {
    send,
    session(sessionId) {
      return {
        send(method, params = {}) {
          return send(method, params, sessionId);
        },
      };
    },
  };
}

async function goto(page, url) {
  await page.send('Page.navigate', { url });
  await waitReady(page);
}

async function waitReady(page) {
  for (let i = 0; i < 50; i += 1) {
    const state = await evaluate(page, 'document.readyState');
    if (state === 'complete') return;
    await sleep(100);
  }
  fail('document.readyState never became complete');
}

async function evaluate(page, expression) {
  const result = await page.send('Runtime.evaluate', {
    expression,
    returnByValue: true,
    awaitPromise: true,
  });
  if (result.exceptionDetails) {
    fail(result.exceptionDetails.text || 'Runtime.evaluate failed');
  }
  return result.result?.value;
}

async function screenshot(page, name) {
  const shot = await page.send('Page.captureScreenshot', { format: 'png' });
  writeFileSync(join(evidenceDir, name), Buffer.from(shot.data, 'base64'));
}

async function driveStudioBoard(page) {
  const url = `${baseUrl}/PARENT_APP_LAYOUT_STUDIO.html`;
  await goto(page, url);
  await screenshot(page, 'before.png');
  const info = await evaluate(page, `({
    title: document.title,
    hint: document.querySelector('.studio-bar .hint')?.textContent || '',
    slots: [...document.querySelectorAll('.slot')].map((s) => s.dataset.title),
  })`);
  const expected = [
    'Pair gate (unpaired)',
    'Family board',
    'Child detail',
    'Skill heat map',
    'Evidence sheet',
    'Plan the day',
    'Add task sheet',
    'Household tasks board',
    'Child task list',
    'Messages',
    'Content',
    'Settings',
    'Design system',
  ];
  assert(info.title === 'goji parent app — layout studio', `title was ${info.title}`);
  assert(info.hint.includes('click a screen title to zoom'), `hint was ${info.hint}`);
  for (const name of expected) {
    assert(info.slots.includes(name), `missing slot ${name}`);
  }
  await screenshot(page, 'after.png');
  return {
    feature: 'studio-board',
    entry: url,
    commands: ['Page.navigate studio'],
    observed: info,
    stateText: `title=${info.title}\nslots=${info.slots.join(' | ')}\nhint=${info.hint}`,
  };
}

async function driveStudioNotes(page) {
  const url = `${baseUrl}/PARENT_APP_LAYOUT_STUDIO.html`;
  await goto(page, url);
  const before = await evaluate(page, `({
    on: document.querySelector('#noteseg button[data-notes="on"]').getAttribute('aria-pressed'),
    off: document.querySelector('#noteseg button[data-notes="off"]').getAttribute('aria-pressed'),
    note: [...document.querySelectorAll('.note')].some((n) => n.textContent.includes('Why:') && n.offsetParent !== null),
  })`);
  assert(before.on === 'true' && before.off === 'false', 'notes did not start on');
  assert(before.note, 'Why note was hidden while Notes on');
  await screenshot(page, 'before.png');
  await evaluate(page, `document.querySelector('#noteseg button[data-notes="off"]').click()`);
  const hidden = await evaluate(page, `({
    on: document.querySelector('#noteseg button[data-notes="on"]').getAttribute('aria-pressed'),
    off: document.querySelector('#noteseg button[data-notes="off"]').getAttribute('aria-pressed'),
    board: document.getElementById('board').classList.contains('notes-off'),
  })`);
  assert(hidden.on === 'false' && hidden.off === 'true', 'Screens only did not press');
  assert(hidden.board, '#board missing notes-off');
  await screenshot(page, 'after.png');
  await evaluate(page, `document.querySelector('#noteseg button[data-notes="on"]').click()`);
  const restored = await evaluate(page, `({
    on: document.querySelector('#noteseg button[data-notes="on"]').getAttribute('aria-pressed'),
    note: [...document.querySelectorAll('.note')].some((n) => n.textContent.includes('Why:') && n.offsetParent !== null),
  })`);
  assert(restored.on === 'true' && restored.note, 'Notes on did not restore a Why note');
  return {
    feature: 'studio-notes',
    entry: 'Screens only',
    commands: [
      'click #noteseg button[data-notes="off"]',
      'click #noteseg button[data-notes="on"]',
    ],
    observed: { before, hidden, restored },
    stateText: `before on=${before.on} off=${before.off}\nafter off pressed=${hidden.off} board.notes-off=${hidden.board}\nrestored on=${restored.on}`,
  };
}

async function driveStudioZoom(page) {
  const url = `${baseUrl}/PARENT_APP_LAYOUT_STUDIO.html`;
  await goto(page, url);
  const closed = await evaluate(page, `document.getElementById('zoom').classList.contains('on')`);
  assert(!closed, 'zoom started open');
  await screenshot(page, 'before.png');
  await evaluate(page, `document.querySelector('.slot[data-title="Family board"] .slot-zoom').click()`);
  const open = await evaluate(page, `({
    on: document.getElementById('zoom').classList.contains('on'),
    side: document.getElementById('zside').textContent,
    phone: document.getElementById('zholder').textContent,
  })`);
  assert(open.on, '#zoom did not open');
  assert(open.side.includes('Family board'), `side was ${open.side}`);
  assert(open.phone.includes('Tuesday'), 'zoomed phone missing Tuesday');
  assert(open.phone.includes('Goji synced 2 min ago'), 'zoomed phone missing sync chip');
  await screenshot(page, 'after.png');
  await evaluate(page, `document.getElementById('zclose').click()`);
  const afterClose = await evaluate(page, `document.getElementById('zoom').classList.contains('on')`);
  assert(!afterClose, '#zoom stayed open after close');
  await evaluate(page, `document.querySelector('.slot[data-title="Family board"] .slot-title').click()`);
  const viaTitle = await evaluate(page, `({
    on: document.getElementById('zoom').classList.contains('on'),
    side: document.getElementById('zside').textContent,
  })`);
  assert(viaTitle.on && viaTitle.side.includes('Family board'), 'title click did not reopen zoom');
  await evaluate(page, `document.getElementById('zclose').click()`);
  return {
    feature: 'studio-zoom',
    entry: '.slot[data-title="Family board"] .slot-zoom',
    commands: [
      'click Family board zoom',
      'click #zclose',
      'click Family board title',
      'click #zclose',
    ],
    observed: { open, viaTitle },
    stateText: `zoom.on=${open.on}\nside=${open.side.split('\\n')[0]}\ntitle-reopen=${viaTitle.on}`,
  };
}

async function driveStudioChildTabs(page) {
  const url = `${baseUrl}/PARENT_APP_LAYOUT_STUDIO.html`;
  await goto(page, url);
  const today = await evaluate(page, `(() => {
    const slot = document.querySelector('.slot[data-title="Child detail"]');
    const selected = slot.querySelector('button[data-pane="p-today"]').getAttribute('aria-selected');
    return {
      selected,
      text: slot.querySelector('#p-today').textContent,
    };
  })()`);
  assert(today.selected === 'true', 'Today was not selected');
  assert(today.text.includes("Today's plan · 3 of 5 done"), 'Today pane missing plan copy');
  await screenshot(page, 'before.png');
  await evaluate(page, `document.querySelector('.slot[data-title="Child detail"] button[data-pane="p-standing"]').click()`);
  const standing = await evaluate(page, `(() => {
    const slot = document.querySelector('.slot[data-title="Child detail"]');
    return {
      selected: slot.querySelector('button[data-pane="p-standing"]').getAttribute('aria-selected'),
      visible: slot.querySelector('#p-standing').classList.contains('on'),
      text: slot.querySelector('#p-standing').textContent,
    };
  })()`);
  assert(standing.selected === 'true' && standing.visible, 'Standing tab did not select');
  assert(standing.text.includes('Where Eli stands'), 'Standing pane missing heading');
  await screenshot(page, 'after.png');
  await evaluate(page, `document.querySelector('.slot[data-title="Child detail"] button[data-pane="p-activity"]').click()`);
  const activity = await evaluate(page, `(() => {
    const slot = document.querySelector('.slot[data-title="Child detail"]');
    return {
      selected: slot.querySelector('button[data-pane="p-activity"]').getAttribute('aria-selected'),
      text: slot.querySelector('#p-activity').textContent,
    };
  })()`);
  assert(activity.selected === 'true', 'Activity tab did not select');
  assert(activity.text.includes('Looked up 4 words'), 'Activity pane missing yesterday row');
  return {
    feature: 'studio-child-tabs',
    entry: 'Child detail Standing',
    commands: [
      'click button[data-pane="p-standing"]',
      'click button[data-pane="p-activity"]',
    ],
    observed: { today, standing, activity },
    stateText: `today=${today.selected}\nstanding=${standing.selected} ${standing.visible}\nactivity=${activity.selected}`,
  };
}

async function driveLessonLiving(page) {
  const url = `${baseUrl}/curriculum/assets/lessons/lesson.science.k2.living.01/index.html`;
  await goto(page, url);
  const start = await evaluate(page, `({
    title: document.title,
    s0: document.getElementById('s0').classList.contains('active'),
    nextDisabled: document.getElementById('hookNext').disabled,
  })`);
  assert(start.title === 'Living or not living? — Goji', `title was ${start.title}`);
  assert(start.s0 && start.nextDisabled, 'hook did not start on s0 with next disabled');
  await evaluate(page, `document.querySelector('[data-guess="wolf"]').click()`);
  const guessed = await evaluate(page, `({
    sel: document.querySelector('[data-guess="wolf"]').classList.contains('sel'),
    nextDisabled: document.getElementById('hookNext').disabled,
  })`);
  assert(guessed.sel && !guessed.nextDisabled, 'wolf pick did not enable next');
  await screenshot(page, 'before.png');
  await evaluate(page, `document.getElementById('hookNext').click()`);
  const teach = await evaluate(page, `({
    s1: document.getElementById('s1').classList.contains('active'),
    heading: document.querySelector('#s1 h2')?.textContent || '',
  })`);
  assert(teach.s1, 'teach stage did not become active');
  assert(teach.heading.includes('The four signs of life'), `heading was ${teach.heading}`);
  await screenshot(page, 'after.png');
  return {
    feature: 'lesson-living',
    entry: '[data-guess="wolf"] then #hookNext',
    commands: ['click [data-guess="wolf"]', 'click #hookNext'],
    observed: { start, guessed, teach },
    stateText: `title=${start.title}\nhook->teach s1=${teach.s1}\nheading=${teach.heading}`,
  };
}

async function driveLessonPractice(page) {
  const url = `${baseUrl}/curriculum/assets/lessons/lesson.science.k2.living.01/index.html`;
  await goto(page, url);
  await evaluate(page, `document.querySelector('[data-guess="wolf"]').click()`);
  await screenshot(page, 'before.png');
  await evaluate(page, `document.getElementById('hookNext').click()`);
  let teachReady = false;
  for (let i = 0; i < 40; i += 1) {
    teachReady = await evaluate(page, `!document.getElementById('teachNext').disabled`);
    if (teachReady) break;
    await sleep(250);
  }
  assert(teachReady, 'Your turn stayed disabled');
  await evaluate(page, `document.getElementById('teachNext').click()`);
  const sort = await evaluate(page, `({
    s2: document.getElementById('s2').classList.contains('active'),
    lead: document.getElementById('pLead').textContent,
    name: document.getElementById('itemName').textContent,
    signs: document.getElementById('signstrip').hidden === false,
    svg: !!document.getElementById('itemPic').querySelector('svg'),
    emoji: document.getElementById('itemPic').textContent,
  })`);
  assert(sort.s2, 'practice stage did not open');
  assert(sort.lead.includes('four signs'), `lead was ${sort.lead}`);
  assert(sort.name === 'Tree' && sort.signs, 'guided sort did not start on Tree with the signs');
  assert(sort.svg && !sort.emoji.includes('🌳'), 'sort card was not an SVG drawing');
  await evaluate(page, `document.querySelector('[data-tap="dead"]').click()`);
  const missed = await evaluate(page, `document.getElementById('fb').textContent`);
  assert(missed.includes('still') && missed.includes('grow'), `feedback was ${missed}`);
  await screenshot(page, 'after.png');
  return {
    feature: 'lesson-practice',
    entry: '#teachNext then [data-tap="dead"]',
    commands: ['click #hookNext', 'wait #teachNext', 'click #teachNext', 'click [data-tap="dead"]'],
    observed: { sort, missed },
    stateText: `practice=${sort.s2} card=${sort.name} signs=${sort.signs}\nfeedback=${missed}`,
  };
}

async function driveStudioWalk(page) {
  const url = `${baseUrl}/PARENT_APP_LAYOUT_STUDIO.html`;
  await goto(page, url);
  const closed = await evaluate(page, `document.getElementById('walk').classList.contains('on')`);
  assert(!closed, 'walk started open');
  await screenshot(page, 'before.png');
  await evaluate(page, `document.getElementById('walkgo').click()`);
  const glance = await evaluate(page, `({
    on: document.getElementById('walk').classList.contains('on'),
    title: document.getElementById('wtitle').textContent,
    copy: document.getElementById('wcopy').textContent,
    phone: document.getElementById('wholder').textContent,
  })`);
  assert(glance.on, '#walk did not open');
  assert(glance.title === 'Six children. One look.', `title was ${glance.title}`);
  assert(glance.copy.includes('Needs you'), 'glance copy missing Needs you');
  assert(glance.phone.includes('Tuesday') && glance.phone.includes('Halfway'), 'family phone missing from the walk');
  await evaluate(page, `document.getElementById('wnext').click()`);
  const day = await evaluate(page, `({
    title: document.getElementById('wtitle').textContent,
    phone: document.getElementById('wholder').textContent,
  })`);
  assert(day.title === 'One red button.', `day title was ${day.title}`);
  assert(day.phone.includes("Today's plan · 3 of 5 done"), 'today plan missing from the walk');
  assert(day.phone.includes('Release day'), 'release action missing');
  await evaluate(page, `document.getElementById('wnext').click()`);
  const standing = await evaluate(page, `document.getElementById('wholder').textContent`);
  assert(standing.includes('Where Eli stands'), 'standing pane missing from the walk');
  assert(standing.includes('Needs help'), 'math struggle missing from the walk');
  await evaluate(page, `document.getElementById('wnext').click()`);
  const lessonTitle = await evaluate(page, `new Promise((resolve) => {
    const frame = document.getElementById('wframe');
    const read = () => resolve(frame.contentDocument ? frame.contentDocument.title : '');
    if (frame.contentDocument && frame.contentDocument.readyState === 'complete' && frame.contentDocument.title) read();
    else frame.addEventListener('load', read, { once: true });
  })`);
  assert(lessonTitle === 'Living or not living? — Goji', `lesson title was ${lessonTitle}`);
  const lessonStep = await evaluate(page, `({
    title: document.getElementById('wtitle').textContent,
    src: document.getElementById('wframe').getAttribute('src'),
    hook: document.getElementById('wframe').contentDocument.body.innerText,
  })`);
  assert(lessonStep.title === 'Living or not living.', `lesson step title was ${lessonStep.title}`);
  assert(String(lessonStep.src).includes('lesson.science.k2.living.01'), `src was ${lessonStep.src}`);
  assert(lessonStep.hook.includes('Which one is alive?'), 'lesson hook was not visible in the frame');
  await screenshot(page, 'after.png');
  await evaluate(page, `document.getElementById('wclose').click()`);
  const restored = await evaluate(page, `({
    on: document.getElementById('walk').classList.contains('on'),
    today: document.querySelector('.slot[data-title="Child detail"] button[data-pane="p-today"]').getAttribute('aria-selected'),
    tuesday: document.querySelector('.slot[data-title="Family board"]').innerText.includes('Tuesday'),
  })`);
  assert(!restored.on, 'walk stayed open');
  assert(restored.today === 'true', 'Today tab was not restored');
  assert(restored.tuesday, 'Family board phone did not return to its slot');
  return {
    feature: 'studio-walk',
    entry: '#walkgo',
    commands: ['click #walkgo', 'click #wnext', 'click #wnext', 'click #wnext', 'click #wclose'],
    observed: { glance: { title: glance.title }, day: { title: day.title }, lessonTitle, restored },
    stateText: `walk=${glance.title} -> ${day.title} -> lesson=${lessonTitle}\nrestored today=${restored.today} board=${restored.tuesday}`,
  };
}
