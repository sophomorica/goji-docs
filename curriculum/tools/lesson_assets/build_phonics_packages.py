#!/usr/bin/env python3
"""Author the six K–2 phonics interactive packages (shared engine + unique data)."""
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = os.path.normpath(os.path.join(HERE, "..", "..", "assets", "lessons"))
SEED = os.path.normpath(
    os.path.join(HERE, "..", "..", "..", "goji_computer", "backend", "seed_data", "lessons")
)

CSS = """
:root{--cream:#fbf5ea;--cream2:#f3e9d6;--ink:#3b2a1e;--ink2:#6b5646;--red:#b5382f;--red2:#8e2a23;--green:#3f7d4e;--sky:#cfe6ee;--gold:#e0a93b;--radius:22px;--shadow:0 6px 0 rgba(59,42,30,.12)}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%;margin:0}
body{font-family:"Avenir Next","Nunito","Segoe UI",system-ui,sans-serif;background:var(--cream);color:var(--ink);display:flex;flex-direction:column;align-items:center;min-height:100vh;user-select:none}
header{width:100%;max-width:1100px;display:flex;align-items:center;justify-content:space-between;padding:14px 22px 0}
.seal{display:flex;align-items:center;gap:10px;font-weight:800;font-size:20px;color:var(--red)}
.seal i{width:30px;height:30px;border-radius:50%;background:var(--red);display:inline-block;box-shadow:inset 0 0 0 5px var(--cream),inset 0 0 0 8px var(--red)}
.dots{display:flex;gap:10px}
.dots b{width:16px;height:16px;border-radius:50%;background:var(--cream2);border:3px solid #9fc7d6;display:block}
.dots b.on{background:var(--red);border-color:var(--red)}
.dots b.done{background:var(--green);border-color:var(--green)}
main{width:100%;max-width:1100px;flex:1;padding:12px 22px 24px;display:flex;flex-direction:column}
.stage{display:none;flex:1;flex-direction:column}
.stage.active{display:flex}
@media (prefers-reduced-motion: no-preference){.stage.active{animation:fadein .35s}@keyframes fadein{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}}
h1{font-size:38px;margin:8px 0 4px;line-height:1.1}
h2{font-size:30px;margin:6px 0;line-height:1.15}
p.lead{font-size:24px;color:var(--ink2);margin:4px 0 14px;line-height:1.3}
.say{display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:50%;border:0;background:var(--sky);font-size:26px;cursor:pointer;box-shadow:var(--shadow);margin-left:8px}
.btn{font:inherit;font-weight:800;font-size:24px;border:0;border-radius:var(--radius);padding:16px 30px;cursor:pointer;background:var(--red);color:#fff;box-shadow:0 6px 0 var(--red2);min-width:160px;min-height:68px}
.btn:active{transform:translateY(4px);box-shadow:0 2px 0 var(--red2)}
.btn.ghost{background:var(--cream2);color:var(--ink);box-shadow:0 6px 0 #d9ccb4}
.btn[disabled]{opacity:.45}
.row{display:flex;gap:14px;flex-wrap:wrap;align-items:center;justify-content:center;margin-top:auto;padding-top:14px}
.choice2{display:grid;grid-template-columns:1fr 1fr;gap:18px;flex:1;min-height:220px}
.pick{border:5px solid transparent;border-radius:var(--radius);background:#fff;box-shadow:var(--shadow);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;cursor:pointer;font-size:28px;font-weight:800;padding:16px;min-height:160px}
.pick.sel{border-color:var(--gold)}
.tiles{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin:16px 0}
.tile{min-width:72px;min-height:72px;padding:10px 16px;border:0;border-radius:16px;background:#fff;box-shadow:var(--shadow);font:inherit;font-weight:900;font-size:32px;cursor:pointer}
.tile.on{background:var(--gold)}
.tile.used{opacity:.35}
.word{font-size:56px;font-weight:900;letter-spacing:2px;text-align:center;margin:10px 0}
.fb{min-height:40px;font-size:22px;font-weight:800;text-align:center}
.fb.good{color:var(--green)}.fb.bad{color:var(--red)}
.bins{display:grid;grid-template-columns:1fr 1fr;gap:16px;flex:1}
.bin{background:#fff;border-radius:var(--radius);box-shadow:var(--shadow);padding:14px;min-height:180px}
.bin h3{margin:0 0 10px;font-size:22px}
.opt{min-height:68px;font:inherit;font-weight:800;font-size:24px;border:0;border-radius:16px;background:#fff;box-shadow:var(--shadow);padding:12px 18px;cursor:pointer;width:100%;text-align:left}
.opt.right{background:#dcecdc}.opt.wrong{background:#fde8e6}
#opts{display:flex;flex-direction:column;gap:12px;margin:12px 0}
#result{display:none;flex:1;flex-direction:column;align-items:center;justify-content:center;text-align:center}
"""

ENGINE = r"""
<script>
(function(){
  const L = window.GOJI_LESSON;
  const t0 = Date.now();
  let reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function post(type, payload){
    try{ if(window.parent!==window) window.parent.postMessage({type, lesson:L.id, ...payload}, '*'); }catch(e){}
  }
  addEventListener('message', e => {
    const m = e.data || {};
    if(m.type === 'player.config' && m.reduced_motion) reduced = true;
  });
  post('lesson.ready', {id:L.id, version:L.version||1});

  let say = function(txt){
    try{
      if(!('speechSynthesis' in window)) return;
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(txt);
      u.rate = 0.92; u.pitch = 1.05;
      speechSynthesis.speak(u);
    }catch(e){}
  };
  const M = window.GOJI_MEDIA || {img:{}, clip:{}, voice:{}};
  const vo = id => M.voice && M.voice[id];
  let audio = null;
  const _say = say;
  say = function(txt, id){
    if(audio){ audio.pause(); audio = null; }
    const f = id && vo(id);
    if(f){ try{ audio = new Audio(f); audio.play().catch(()=>_say(txt)); return; }catch(e){} }
    _say(txt);
  };
  document.querySelectorAll('[data-say]').forEach(b => {
    b.addEventListener('click', () => say(b.dataset.say, b.dataset.voice));
  });

  const stages = ['hook','teach','practice','check'];
  let cur = 0;
  function go(n){
    document.querySelectorAll('.stage').forEach((s,i)=>s.classList.toggle('active', i===n));
    document.querySelectorAll('.dots b').forEach((d,i)=>{ d.classList.toggle('on', i===n); d.classList.toggle('done', i<n); });
    cur = n;
    post('lesson.stage', {stage: stages[n]});
    window.scrollTo(0,0);
    if(n===1) playTeach();
    if(n===2) startPractice();
    if(n===3) startQuiz();
  }
  window.go = go;

  /* ---- hook ---- */
  let hookChoice = null;
  document.querySelectorAll('#hookPicks .pick').forEach(p => {
    p.addEventListener('click', () => {
      document.querySelectorAll('#hookPicks .pick').forEach(x => x.classList.remove('sel'));
      p.classList.add('sel');
      hookChoice = p.dataset.k;
      document.getElementById('hookNext').disabled = false;
      say(p.dataset.say || p.textContent, p.dataset.voice);
    });
  });

  /* ---- teach ---- */
  let teachTimer = [];
  function later(fn, ms){ const id = setTimeout(fn, reduced ? 80 : ms); teachTimer.push(id); }
  function playTeach(){
    teachTimer.forEach(clearTimeout); teachTimer = [];
    const beats = L.teach || [];
    const cap = document.getElementById('teachCap');
    const tiles = document.getElementById('teachTiles');
    function show(i){
      const b = beats[i];
      if(!b){ document.getElementById('teachNext').disabled = false; return; }
      cap.textContent = b.text;
      tiles.innerHTML = (b.tiles||[]).map(t => '<span class="tile on">'+t+'</span>').join('');
      say(b.say || b.text, b.voice);
      later(() => show(i+1), b.ms || 3200);
    }
    document.getElementById('teachNext').disabled = true;
    show(0);
  }
  document.getElementById('sayTeach').onclick = () => {
    say((L.teach||[]).map(b => b.say || b.text).join(' '));
  };

  /* ---- practice ---- */
  const P = L.practice;
  let pi = 0, pDone = 0;
  function startPractice(){
    pi = 0; pDone = 0;
    document.getElementById('pracNext').disabled = true;
    nextPractice();
  }
  function nextPractice(){
    const fb = document.getElementById('pracFb');
    fb.textContent = ''; fb.className = 'fb';
    if(pi >= P.items.length){
      document.getElementById('pracPrompt').textContent = P.done;
      document.getElementById('pracBoard').innerHTML = '';
      document.getElementById('pracNext').disabled = false;
      say(P.done, 'prac_done');
      return;
    }
    const it = P.items[pi];
    document.getElementById('pracPrompt').textContent = it.prompt;
    say(it.say || it.prompt, it.voice);
    const board = document.getElementById('pracBoard');
    board.innerHTML = '';
    if(P.kind === 'blend'){
      const built = document.createElement('div'); built.className = 'word'; built.id = 'built';
      board.appendChild(built);
      const row = document.createElement('div'); row.className = 'tiles';
      it.tiles.forEach((t, i) => {
        const b = document.createElement('button'); b.className = 'tile'; b.textContent = t; b.type = 'button';
        b.onclick = () => {
          if(t === it.want[document.getElementById('built').dataset.n|0]){
            document.getElementById('built').textContent += t;
            document.getElementById('built').dataset.n = (document.getElementById('built').dataset.n|0)+1;
            b.classList.add('used');
            if((document.getElementById('built').dataset.n|0) === it.want.length){
              fb.className = 'fb good'; fb.textContent = 'Yes — '+it.word+'!';
              say('Yes. '+it.word, 'yes');
              pDone++; pi++; setTimeout(nextPractice, reduced?200:700);
            }
          } else {
            fb.className = 'fb bad'; fb.textContent = 'Blend left to right.';
            say('Blend left to right.','hint');
          }
        };
        row.appendChild(b);
      });
      board.appendChild(row);
    } else if(P.kind === 'sort'){
      const word = document.createElement('div'); word.className = 'word'; word.textContent = it.word;
      board.appendChild(word);
      const bins = document.createElement('div'); bins.className = 'bins';
      P.bins.forEach(bin => {
        const el = document.createElement('button'); el.type='button'; el.className='pick'; el.textContent = bin.label;
        el.onclick = () => {
          if(bin.id === it.bin){
            fb.className='fb good'; fb.textContent='Yes! '+it.why;
            say('Yes. '+it.why,'yes'); pDone++; pi++; setTimeout(nextPractice, reduced?200:700);
          } else {
            fb.className='fb bad'; fb.textContent=it.hint; say(it.hint,'hint');
          }
        };
        bins.appendChild(el);
      });
      board.appendChild(bins);
    } else if(P.kind === 'toggle'){
      const word = document.createElement('div'); word.className = 'word'; word.id='tog'; word.textContent = it.start;
      board.appendChild(word);
      const row = document.createElement('div'); row.className='row'; row.style.marginTop='8px';
      const add = document.createElement('button'); add.type='button'; add.className='btn ghost'; add.textContent='Add magic e';
      const rem = document.createElement('button'); rem.type='button'; rem.className='btn ghost'; rem.textContent='Take e away';
      function check(val){
        word.textContent = val;
        if(val === it.want){
          fb.className='fb good'; fb.textContent='Yes — '+it.why;
          say('Yes. '+it.why,'yes'); pDone++; pi++; setTimeout(nextPractice, reduced?200:800);
        }
      }
      add.onclick = () => check(it.start.endsWith('e') ? it.start : it.start+'e');
      rem.onclick = () => check(it.start.endsWith('e') ? it.start.slice(0,-1) : it.start);
      row.appendChild(add); row.appendChild(rem); board.appendChild(row);
    } else if(P.kind === 'spot'){
      const word = document.createElement('div'); word.className='tiles';
      it.chunks.forEach((ch, i) => {
        const b = document.createElement('button'); b.type='button'; b.className='tile'; b.textContent=ch;
        b.onclick = () => {
          if(i === it.team){
            fb.className='fb good'; fb.textContent='That team says '+it.sound+'!';
            say('Yes. That team says '+it.sound,'yes'); pDone++; pi++; setTimeout(nextPractice, reduced?200:700);
          } else {
            fb.className='fb bad'; fb.textContent='Find the two letters that share one sound.';
            say('Find the two letters that share one sound.','hint');
          }
        };
        word.appendChild(b);
      });
      board.appendChild(word);
    } else if(P.kind === 'chop'){
      const word = document.createElement('div'); word.className='tiles';
      it.letters.forEach((ch, i) => {
        const wrap = document.createElement('span');
        const b = document.createElement('button'); b.type='button'; b.className='tile'; b.textContent=ch;
        wrap.appendChild(b);
        if(i < it.letters.length-1){
          const cut = document.createElement('button'); cut.type='button'; cut.className='tile'; cut.textContent='|';
          cut.onclick = () => {
            if(i+1 === it.cut){
              fb.className='fb good'; fb.textContent=it.parts.join(' · ');
              say('Yes. '+it.parts.join(' then '),'yes'); pDone++; pi++; setTimeout(nextPractice, reduced?200:700);
            } else {
              fb.className='fb bad'; fb.textContent='Chop between the vowel chunks.';
              say('Chop between the vowel chunks.','hint');
            }
          };
          wrap.appendChild(cut);
        }
        word.appendChild(wrap);
      });
      board.appendChild(word);
    }
  }

  /* ---- check ---- */
  const QUIZ = L.quiz;
  let qi = 0, score = 0, locked = false;
  function startQuiz(){
    qi = 0; score = 0;
    document.getElementById('result').style.display = 'none';
    document.getElementById('qBox').style.display = 'block';
    showQ();
  }
  function showQ(){
    locked = false;
    const q = QUIZ[qi];
    document.getElementById('qText').textContent = q.q;
    document.getElementById('qNext').disabled = true;
    document.getElementById('sayQ').onclick = () => say(q.q+' '+q.o.join(', or '), 'q'+(q.id||qi));
    const opts = document.getElementById('opts'); opts.innerHTML = '';
    q.o.forEach((lab, i) => {
      const b = document.createElement('button'); b.type='button'; b.className='opt'; b.textContent=lab;
      b.onclick = () => {
        if(locked) return;
        locked = true;
        const ok = i === q.a;
        b.classList.add(ok ? 'right' : 'wrong');
        if(ok) score++;
        else opts.children[q.a].classList.add('right');
        document.getElementById('qNext').disabled = false;
      };
      opts.appendChild(b);
    });
    say(q.q, 'q'+(q.id||qi));
  }
  document.getElementById('qNext').onclick = () => {
    qi++;
    if(qi >= QUIZ.length) finish();
    else showQ();
  };
  function finish(){
    document.getElementById('qBox').style.display = 'none';
    const box = document.getElementById('result');
    box.style.display = 'flex';
    const pass = score >= (L.pass||4);
    document.getElementById('gateTxt').textContent = pass ? L.passText : L.retryText;
    document.getElementById('guessTxt').textContent = score+' / '+QUIZ.length;
    say((pass?L.passText:L.retryText)+' '+score+' out of '+QUIZ.length, pass?'pass':'retry');
    post('lesson.check', {quiz_id:L.quiz_id, score, total:QUIZ.length, items:[]});
    post('lesson.complete', {quiz_id:L.quiz_id, score, total:QUIZ.length, duration_s: Math.round((Date.now()-t0)/1000)});
  }

  window.GOJI_TEST = {
    go,
    quiz: () => QUIZ,
    autoCheck: function(pass=true){
      go(3);
      return new Promise(res => {
        const step = () => {
          if(document.getElementById('result').style.display !== 'none'){
            res({score}); return;
          }
          const q = QUIZ[qi];
          const want = pass ? q.a : ((q.a+1)%q.o.length);
          document.querySelectorAll('#opts .opt')[want].click();
          setTimeout(() => { document.getElementById('qNext').click(); setTimeout(step, 50); }, 40);
        };
        setTimeout(step, 150);
      });
    }
  };
  document.getElementById('hookNext').onclick = () => go(1);
  document.getElementById('teachNext').onclick = () => go(2);
  document.getElementById('pracNext').onclick = () => go(3);
})();
</script>
"""


def html_for(data):
    hook = data["hook"]
    picks = "".join(
        f'<button type="button" class="pick" data-k="{p["k"]}" data-say="{p["say"]}" data-voice="{p["voice"]}">{p["label"]}</button>'
        for p in hook["picks"]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{data["title"]} — Goji</title>
<script src="media/index.js"></script>
<style>{CSS}</style>
</head>
<body>
<header>
  <div class="seal"><i></i> Goji</div>
  <div class="dots"><b class="on"></b><b></b><b></b><b></b></div>
</header>
<main>
  <section class="stage active" id="hook">
    <h1>{data["title"]} <button class="say" data-say="{hook["say"]}" data-voice="hook" type="button">🔊</button></h1>
    <p class="lead">{hook["lead"]}</p>
    <div class="choice2" id="hookPicks">{picks}</div>
    <div class="row"><button class="btn" id="hookNext" disabled type="button">Next</button></div>
  </section>
  <section class="stage" id="teach">
    <h2>Watch the code <button class="say" id="sayTeach" type="button">🔊</button></h2>
    <p class="lead" id="teachCap">Listen first.</p>
    <div class="tiles" id="teachTiles"></div>
    <div class="row"><button class="btn ghost" type="button" onclick="go(1)">Replay</button><button class="btn" id="teachNext" disabled type="button">My turn</button></div>
  </section>
  <section class="stage" id="practice">
    <h2>Your turn</h2>
    <p class="lead" id="pracPrompt"></p>
    <div id="pracBoard"></div>
    <p class="fb" id="pracFb"></p>
    <div class="row"><button class="btn" id="pracNext" disabled type="button">Show what I know</button></div>
  </section>
  <section class="stage" id="check">
    <div id="qBox">
      <h2 id="qText"></h2>
      <button class="say" id="sayQ" type="button">🔊</button>
      <div id="opts"></div>
      <div class="row"><button class="btn" id="qNext" disabled type="button">Next</button></div>
    </div>
    <div id="result">
      <h1 id="gateTxt"></h1>
      <p class="lead" id="guessTxt"></p>
      <p class="lead">Next: the same words on flashcards, then Aesop, then Kiwix.</p>
    </div>
  </section>
</main>
<script>window.GOJI_LESSON = {json.dumps(data["engine"], ensure_ascii=False)};</script>
{ENGINE}
</body>
</html>
"""


PACKAGES = [
    {
        "id": "lesson.reading.k2.phonics.01",
        "title": "Crack the code",
        "objective": "obj.reading.k2.phonics.01",
        "va": ["1.FFR.3"],
        "anim": "anim.reading.k2.phonics.01",
        "quiz_id": "quiz.reading.k2.phonics.01",
        "anchor": "fox, hen, dog — tonight's Aesop animals",
        "research": "Fox",
        "hook": {
            "lead": "The fox wants the grapes. Which one is the WORD fox?",
            "say": "The fox wants the grapes. Which one is the word fox? Tap your guess.",
            "picks": [
                {"k": "word", "label": "fox", "say": "fox — three sounds.", "voice": "hook_word"},
                {"k": "pic", "label": "🦊 picture", "say": "That is a picture, not the word.", "voice": "hook_pic"},
            ],
        },
        "engine": {
            "id": "lesson.reading.k2.phonics.01",
            "version": 1,
            "quiz_id": "quiz.reading.k2.phonics.01",
            "pass": 4,
            "passText": "You can crack CVC words!",
            "retryText": "Good try. Blend left to right once more.",
            "teach": [
                {"text": "Letters make sounds.", "tiles": ["f", "o", "x"], "say": "Letters make sounds. f, o, x.", "voice": "t1", "ms": 2800},
                {"text": "Slide them together: fff-ooo-x.", "tiles": ["f-o-x"], "say": "Slide them together. fff ooo x. Fox.", "voice": "t2", "ms": 3200},
                {"text": "Never guess from a picture. Read the code.", "tiles": ["fox"], "say": "Never guess from a picture. Read the code.", "voice": "t3", "ms": 3000},
            ],
            "practice": {
                "kind": "blend",
                "done": "All blended! Now show what you know.",
                "items": [
                    {"prompt": "Build fox.", "tiles": ["x", "f", "o"], "want": ["f", "o", "x"], "word": "fox", "voice": "p1"},
                    {"prompt": "Build hen.", "tiles": ["n", "h", "e"], "want": ["h", "e", "n"], "word": "hen", "voice": "p2"},
                    {"prompt": "Build dog.", "tiles": ["g", "d", "o"], "want": ["d", "o", "g"], "word": "dog", "voice": "p3"},
                    {"prompt": "Build sun.", "tiles": ["n", "s", "u"], "want": ["s", "u", "n"], "word": "sun", "voice": "p4"},
                    {"prompt": "Build hop.", "tiles": ["p", "h", "o"], "want": ["h", "o", "p"], "word": "hop", "voice": "p5"},
                    {"prompt": "Build ant.", "tiles": ["t", "a", "n"], "want": ["a", "n", "t"], "word": "ant", "voice": "p6"},
                    {"prompt": "Build cat.", "tiles": ["t", "c", "a"], "want": ["c", "a", "t"], "word": "cat", "voice": "p7"},
                    {"prompt": "Build log.", "tiles": ["g", "l", "o"], "want": ["l", "o", "g"], "word": "log", "voice": "p8"},
                ],
            },
            "quiz": [
                {"id": 1, "q": "c-a-t slides into…", "o": ["cat", "cut", "cot"], "a": 0},
                {"id": 2, "q": "The Aesop animal: f-o-x", "o": ["fix", "fox", "box"], "a": 1},
                {"id": 3, "q": "h-e-n is…", "o": ["han", "hen", "hin"], "a": 1},
                {"id": 4, "q": "Which word has the short o of hop?", "o": ["sun", "dog", "hen"], "a": 1},
                {"id": 5, "q": "How do you read a secret-code word?", "o": ["Guess the picture", "Blend left to right", "Skip it"], "a": 1},
            ],
        },
    },
    {
        "id": "lesson.reading.k2.phonics.04",
        "title": "Sound teams",
        "objective": "obj.reading.k2.phonics.04",
        "va": ["1.FFR.3", "2.FFR.3"],
        "anim": "anim.reading.k2.phonics.04",
        "quiz_id": "quiz.reading.k2.phonics.04",
        "anchor": "ship / sip — then Aesop's sheep",
        "research": "Sheep",
        "hook": {
            "lead": "ship and sip look almost the same. What did sh do?",
            "say": "Ship and sip look almost the same. What did s h do? Tap your guess.",
            "picks": [
                {"k": "melt", "label": "They melted into one new sound", "say": "Yes. s h melts into sh.", "voice": "hook_melt"},
                {"k": "two", "label": "You still say /s/ and /h/", "say": "Not quite. They melt.", "voice": "hook_two"},
            ],
        },
        "engine": {
            "id": "lesson.reading.k2.phonics.04",
            "version": 1,
            "quiz_id": "quiz.reading.k2.phonics.04",
            "pass": 4,
            "passText": "You can hear melt vs hold-hands!",
            "retryText": "Listen again: melt makes one new sound.",
            "teach": [
                {"text": "sh, ch, th, wh, ck MELT. One new sound.", "tiles": ["sh", "ch", "th"], "say": "S H, C H, T H melt. One new sound.", "voice": "t1", "ms": 3400},
                {"text": "st, gr, fl HOLD HANDS. You still hear both.", "tiles": ["st", "gr", "fl"], "say": "S T, G R, F L hold hands. You still hear both.", "voice": "t2", "ms": 3400},
                {"text": "ship has /sh/. sip has /s/.", "tiles": ["ship", "sip"], "say": "Ship has sh. Sip has s.", "voice": "t3", "ms": 2800},
            ],
            "practice": {
                "kind": "sort",
                "bins": [{"id": "melt", "label": "Melt (one sound)"}, {"id": "hold", "label": "Hold hands (both)"}],
                "done": "Sorted! Digraphs melt. Blends keep both.",
                "items": [
                    {"word": "ship", "bin": "melt", "why": "sh is one new sound.", "hint": "Do you still hear /s/ and /h/?", "prompt": "Does ship melt or hold hands?", "voice": "p1"},
                    {"word": "stop", "bin": "hold", "why": "You still hear /s/ and /t/.", "hint": "Can you hear both sounds?", "prompt": "Does stop melt or hold hands?", "voice": "p2"},
                    {"word": "chat", "bin": "melt", "why": "ch is one new sound.", "hint": "Is ch one sound or two?", "prompt": "Does chat melt or hold hands?", "voice": "p3"},
                    {"word": "frog", "bin": "hold", "why": "/f/ and /r/ both stay.", "hint": "Aesop's frog keeps both sounds.", "prompt": "Does frog melt or hold hands?", "voice": "p4"},
                    {"word": "this", "bin": "melt", "why": "th is one new sound.", "hint": "th melts.", "prompt": "Does this melt or hold hands?", "voice": "p5"},
                    {"word": "grass", "bin": "hold", "why": "/g/ and /r/ both stay.", "hint": "gr holds hands.", "prompt": "Does grass melt or hold hands?", "voice": "p6"},
                    {"word": "duck", "bin": "melt", "why": "ck is just /k/.", "hint": "ck is a spelling of /k/.", "prompt": "Does duck melt or hold hands?", "voice": "p7"},
                    {"word": "when", "bin": "melt", "why": "wh is one new sound.", "hint": "wh melts.", "prompt": "Does when melt or hold hands?", "voice": "p8"},
                ],
            },
            "quiz": [
                {"id": 1, "q": "sh in ship is…", "o": ["two sounds", "one new sound", "silent"], "a": 1},
                {"id": 2, "q": "st in stop is…", "o": ["one melted sound", "both /s/ and /t/", "silent t"], "a": 1},
                {"id": 3, "q": "Which word has a melt team?", "o": ["frog", "chip", "grass"], "a": 1},
                {"id": 4, "q": "then vs ten — what did th do?", "o": ["Added a new melted sound", "Made it longer", "Nothing"], "a": 0},
                {"id": 5, "q": "ck at the end of duck says…", "o": ["/s/", "/k/", "/ch/"], "a": 1},
            ],
        },
    },
    {
        "id": "lesson.reading.k2.phonics.02",
        "title": "Magic-e",
        "objective": "obj.reading.k2.phonics.02",
        "va": ["1.FFR.3"],
        "anim": "anim.reading.k2.phonics.02",
        "quiz_id": "quiz.reading.k2.phonics.02",
        "anchor": "hop / hope — the hare can hop; we hope he wins",
        "research": "Hare",
        "hook": {
            "lead": "cap and cape. What did the silent e do?",
            "say": "Cap and cape. What did the silent e do? Tap your guess.",
            "picks": [
                {"k": "wake", "label": "It woke the a — /ā/", "say": "Yes. Magic e wakes the vowel.", "voice": "hook_wake"},
                {"k": "add", "label": "It added a new sound /e/", "say": "The e is silent. It changes the other vowel.", "voice": "hook_add"},
            ],
        },
        "engine": {
            "id": "lesson.reading.k2.phonics.02",
            "version": 1,
            "quiz_id": "quiz.reading.k2.phonics.02",
            "pass": 4,
            "passText": "You can work the magic-e switch!",
            "retryText": "Remember: e is silent. It wakes the other vowel.",
            "teach": [
                {"text": "hop is short o. Add e → hope.", "tiles": ["hop", "→", "hope"], "say": "Hop is short o. Add e and it becomes hope.", "voice": "t1", "ms": 3200},
                {"text": "The e is silent. It wakes the first vowel.", "tiles": ["h", "o", "p", "e"], "say": "The e is silent. It wakes the first vowel.", "voice": "t2", "ms": 3000},
                {"text": "cap / cape. kit / kite. cut / cute.", "tiles": ["cape", "kite", "cute"], "say": "Cap cape. Kit kite. Cut cute.", "voice": "t3", "ms": 3000},
            ],
            "practice": {
                "kind": "toggle",
                "done": "You can add and take the magic e!",
                "items": [
                    {"prompt": "Make hop say its name.", "start": "hop", "want": "hope", "why": "hope — long o. The hare can hope.", "voice": "p1"},
                    {"prompt": "Take the magic e off cape.", "start": "cape", "want": "cap", "why": "cap — short a.", "voice": "p2"},
                    {"prompt": "Wake the i in kit.", "start": "kit", "want": "kite", "why": "kite — long i.", "voice": "p3"},
                    {"prompt": "Take e off cute.", "start": "cute", "want": "cut", "why": "cut — short u.", "voice": "p4"},
                    {"prompt": "Wake the a in cap.", "start": "cap", "want": "cape", "why": "cape — long a.", "voice": "p5"},
                    {"prompt": "Take e off pine.", "start": "pine", "want": "pin", "why": "pin — short i.", "voice": "p6"},
                    {"prompt": "Wake the o in not.", "start": "not", "want": "note", "why": "note — long o.", "voice": "p7"},
                    {"prompt": "Make hid say its name.", "start": "hid", "want": "hide", "why": "hide — Aesop's mice hide.", "voice": "p8"},
                ],
            },
            "quiz": [
                {"id": 1, "q": "hop + magic e is…", "o": ["hopp", "hope", "hoop"], "a": 1},
                {"id": 2, "q": "The e in cape is…", "o": ["said /e/", "silent — it wakes a", "a blend"], "a": 1},
                {"id": 3, "q": "Which pair is a magic-e switch?", "o": ["fox / box", "cap / cape", "ship / shop"], "a": 1},
                {"id": 4, "q": "bone (the dog's bone) has…", "o": ["short o", "long o", "silent o"], "a": 1},
                {"id": 5, "q": "kit without a change is short. kite is…", "o": ["still short i", "long i", "a new consonant"], "a": 1},
            ],
        },
    },
    {
        "id": "lesson.reading.k2.phonics.03",
        "title": "Vowel teams & bossy r",
        "objective": "obj.reading.k2.phonics.03",
        "va": ["1.FFR.3", "2.FFR.3"],
        "anim": "anim.reading.k2.phonics.03",
        "quiz_id": "quiz.reading.k2.phonics.03",
        "anchor": "rain / oak / sheep — Aesop weather and the oak",
        "research": "Oak",
        "hook": {
            "lead": "rain and ran. What are a and i doing?",
            "say": "Rain and ran. What are a and i doing? Tap your guess.",
            "picks": [
                {"k": "team", "label": "They sing one voice: /ā/", "say": "Yes. A team. First vowel talks.", "voice": "hook_team"},
                {"k": "two", "label": "You say /a/ then /i/", "say": "Not two voices. One team.", "voice": "hook_two"},
            ],
        },
        "engine": {
            "id": "lesson.reading.k2.phonics.03",
            "version": 1,
            "quiz_id": "quiz.reading.k2.phonics.03",
            "pass": 4,
            "passText": "You can spot teams and bossy r!",
            "retryText": "Find the two letters that share one voice.",
            "teach": [
                {"text": "When two vowels go walking, the first one talks.", "tiles": ["ai", "ee", "oa", "ea"], "say": "When two vowels go walking, the first one talks.", "voice": "t1", "ms": 3400},
                {"text": "rain, sheep, goat, oak, beak.", "tiles": ["rain", "sheep", "oak"], "say": "Rain, sheep, goat, oak, beak.", "voice": "t2", "ms": 3000},
                {"text": "Bossy r grabs the vowel: ar, or, er.", "tiles": ["ar", "or", "er"], "say": "Bossy r grabs the vowel. ar, or, er.", "voice": "t3", "ms": 3200},
            ],
            "practice": {
                "kind": "spot",
                "done": "You found the teams!",
                "items": [
                    {"prompt": "Tap the team in rain.", "chunks": ["r", "ai", "n"], "team": 1, "sound": "/ā/", "voice": "p1"},
                    {"prompt": "Tap the team in sheep.", "chunks": ["sh", "ee", "p"], "team": 1, "sound": "/ē/", "voice": "p2"},
                    {"prompt": "Tap the team in goat.", "chunks": ["g", "oa", "t"], "team": 1, "sound": "/ō/", "voice": "p3"},
                    {"prompt": "Tap the team in oak.", "chunks": ["oa", "k"], "team": 0, "sound": "/ō/", "voice": "p4"},
                    {"prompt": "Tap bossy r in farm.", "chunks": ["f", "ar", "m"], "team": 1, "sound": "/ar/", "voice": "p5"},
                    {"prompt": "Tap bossy r in corn.", "chunks": ["c", "or", "n"], "team": 1, "sound": "/or/", "voice": "p6"},
                    {"prompt": "Tap the team in beak.", "chunks": ["b", "ea", "k"], "team": 1, "sound": "/ē/", "voice": "p7"},
                    {"prompt": "Tap bossy r in her.", "chunks": ["h", "er"], "team": 1, "sound": "/er/", "voice": "p8"},
                ],
            },
            "quiz": [
                {"id": 1, "q": "ai in rain says…", "o": ["/ă/", "/ā/", "/ī/"], "a": 1},
                {"id": 2, "q": "The Aesop oak has which team?", "o": ["ee", "oa", "oi"], "a": 1},
                {"id": 3, "q": "sheep (wolf in sheep's clothing) has…", "o": ["short e", "the ee team", "magic e"], "a": 1},
                {"id": 4, "q": "r in farm is…", "o": ["just /r/ after /ă/", "bossy — it grabs a", "silent"], "a": 1},
                {"id": 5, "q": "ran vs rain — what changed?", "o": ["A vowel team was added", "A blend melted", "Magic e"], "a": 0},
            ],
        },
    },
    {
        "id": "lesson.reading.k2.phonics.05",
        "title": "Tricky teams",
        "objective": "obj.reading.k2.phonics.05",
        "va": ["2.FFR.3"],
        "anim": "anim.reading.k2.phonics.05",
        "quiz_id": "quiz.reading.k2.phonics.05",
        "anchor": "mouse / moon — Town Mouse; the moon above the meadow",
        "research": "Mouse",
        "hook": {
            "lead": "moon and book both have oo. Same sound?",
            "say": "Moon and book both have o o. Same sound? Tap your guess.",
            "picks": [
                {"k": "two", "label": "Two faces of oo", "say": "Yes. Moon-oo and book-oo.", "voice": "hook_two"},
                {"k": "same", "label": "Always the same", "say": "Not always. Two faces.", "voice": "hook_same"},
            ],
        },
        "engine": {
            "id": "lesson.reading.k2.phonics.05",
            "version": 1,
            "quiz_id": "quiz.reading.k2.phonics.05",
            "pass": 4,
            "passText": "You can hear the noise-makers!",
            "retryText": "Try the two faces of oo again.",
            "teach": [
                {"text": "oi/oy and ou/ow are noise-makers: ahoy! ouch!", "tiles": ["oi", "oy", "ou", "ow"], "say": "O I and O Y say ahoy. O U and O W say ouch.", "voice": "t1", "ms": 3600},
                {"text": "aw is the crow's caw. paw, straw.", "tiles": ["aw", "paw"], "say": "A W is the crow's caw. Paw. Straw.", "voice": "t2", "ms": 3000},
                {"text": "oo has two faces: moon and book.", "tiles": ["moon", "book"], "say": "O O has two faces. Moon. Book.", "voice": "t3", "ms": 3000},
            ],
            "practice": {
                "kind": "sort",
                "bins": [{"id": "moon", "label": "moon-oo"}, {"id": "book", "label": "book-oo"}],
                "done": "Two faces sorted. Now the check.",
                "items": [
                    {"word": "moon", "bin": "moon", "why": "Long oo, like soon and food.", "hint": "Does it sound like moon or book?", "prompt": "Which face of oo?", "voice": "p1"},
                    {"word": "book", "bin": "book", "why": "Short oo, like look and good.", "hint": "Does it sound like moon or book?", "prompt": "Which face of oo?", "voice": "p2"},
                    {"word": "food", "bin": "moon", "why": "Food has moon-oo.", "hint": "Say food slowly.", "prompt": "Which face of oo?", "voice": "p3"},
                    {"word": "look", "bin": "book", "why": "Look has book-oo.", "hint": "Say look slowly.", "prompt": "Which face of oo?", "voice": "p4"},
                    {"word": "soon", "bin": "moon", "why": "Soon has moon-oo.", "hint": "Soon rhymes with moon.", "prompt": "Which face of oo?", "voice": "p5"},
                    {"word": "good", "bin": "book", "why": "Good has book-oo.", "hint": "Good rhymes with wood.", "prompt": "Which face of oo?", "voice": "p6"},
                    {"word": "wood", "bin": "book", "why": "Wood has book-oo.", "hint": "Wood, not wooed.", "prompt": "Which face of oo?", "voice": "p7"},
                    {"word": "too", "bin": "moon", "why": "Too has moon-oo.", "hint": "Too like moon.", "prompt": "Which face of oo?", "voice": "p8"},
                ],
            },
            "quiz": [
                {"id": 1, "q": "oi in coin says…", "o": ["/ō/", "ahoy!", "/oo/"], "a": 1},
                {"id": 2, "q": "mouse (Town Mouse) has…", "o": ["magic e only", "the ou ouch-team", "short u"], "a": 1},
                {"id": 3, "q": "moon and book show that oo…", "o": ["is always the same", "has two faces", "is silent"], "a": 1},
                {"id": 4, "q": "paw (the lion's paw) has…", "o": ["aw like the crow's caw", "long a", "ou"], "a": 0},
                {"id": 5, "q": "out vs oat — out is…", "o": ["a vowel team /ō/", "a noise-maker ouch", "magic e"], "a": 1},
            ],
        },
    },
    {
        "id": "lesson.reading.k2.phonics.06",
        "title": "Two bites",
        "objective": "obj.reading.k2.phonics.06",
        "va": ["1.FFR.3", "2.FFR.3"],
        "anim": "anim.reading.k2.phonics.06",
        "quiz_id": "quiz.reading.k2.phonics.06",
        "anchor": "picnic / rabbit — Aesop's hare family",
        "research": "Rabbit",
        "hook": {
            "lead": "picnic is a big word. How do we read it?",
            "say": "Picnic is a big word. How do we read it? Tap your guess.",
            "picks": [
                {"k": "chop", "label": "Chop: pic · nic", "say": "Yes. Two bites.", "voice": "hook_chop"},
                {"k": "guess", "label": "Guess the whole word", "say": "Don't guess. Chop first.", "voice": "hook_guess"},
            ],
        },
        "engine": {
            "id": "lesson.reading.k2.phonics.06",
            "version": 1,
            "quiz_id": "quiz.reading.k2.phonics.06",
            "pass": 4,
            "passText": "You can chop big words!",
            "retryText": "Chop between the vowel chunks, then add the ending.",
            "teach": [
                {"text": "Every bite needs a vowel. picnic → pic · nic", "tiles": ["pic", "nic"], "say": "Every bite needs a vowel. Picnic. Pic. Nic.", "voice": "t1", "ms": 3400},
                {"text": "rabbit → rab · bit. The hare family.", "tiles": ["rab", "bit"], "say": "Rabbit. Rab. Bit.", "voice": "t2", "ms": 2800},
                {"text": "Endings: -s, -ing, -ed. jump → jumping, jumped, jumps.", "tiles": ["-s", "-ing", "-ed"], "say": "Endings. S, I N G, E D. Jump, jumping, jumped, jumps.", "voice": "t3", "ms": 3600},
            ],
            "practice": {
                "kind": "chop",
                "done": "Chopped! Endings next in the check.",
                "items": [
                    {"prompt": "Chop picnic.", "letters": ["p","i","c","n","i","c"], "cut": 3, "parts": ["pic","nic"], "voice": "p1"},
                    {"prompt": "Chop rabbit.", "letters": ["r","a","b","b","i","t"], "cut": 3, "parts": ["rab","bit"], "voice": "p2"},
                    {"prompt": "Chop basket.", "letters": ["b","a","s","k","e","t"], "cut": 3, "parts": ["bas","ket"], "voice": "p3"},
                    {"prompt": "Chop sunset.", "letters": ["s","u","n","s","e","t"], "cut": 3, "parts": ["sun","set"], "voice": "p4"},
                    {"prompt": "Chop napkin.", "letters": ["n","a","p","k","i","n"], "cut": 3, "parts": ["nap","kin"], "voice": "p5"},
                    {"prompt": "Chop helmet.", "letters": ["h","e","l","m","e","t"], "cut": 3, "parts": ["hel","met"], "voice": "p6"},
                ],
            },
            "quiz": [
                {"id": 1, "q": "picnic chops into…", "o": ["pi · cnic", "pic · nic", "picn · ic"], "a": 1},
                {"id": 2, "q": "Each syllable needs…", "o": ["a silent e", "a vowel", "a blend"], "a": 1},
                {"id": 3, "q": "jump + ing is…", "o": ["jumpd", "jumping", "jumpsed"], "a": 1},
                {"id": 4, "q": "-ed can say…", "o": ["only /ed/", "/t/, /d/, or /ed/", "always /ēd/"], "a": 1},
                {"id": 5, "q": "rabbit (the hare's cousin) is…", "o": ["one closed syllable", "two closed syllables", "magic-e"], "a": 1},
            ],
        },
    },
]


def voices_for(pkg):
    lines = [
        {"id": "hook", "text": pkg["hook"]["say"]},
        {"id": "prac_done", "text": pkg["engine"]["practice"]["done"]},
        {"id": "yes", "text": "Yes!"},
        {"id": "hint", "text": "Try again."},
        {"id": "pass", "text": pkg["engine"]["passText"]},
        {"id": "retry", "text": pkg["engine"]["retryText"]},
    ]
    for p in pkg["hook"]["picks"]:
        lines.append({"id": p["voice"], "text": p["say"]})
    for i, beat in enumerate(pkg["engine"]["teach"], 1):
        lines.append({"id": f"t{i}", "text": beat["say"]})
    for i, item in enumerate(pkg["engine"]["practice"]["items"], 1):
        lines.append({"id": f"p{i}", "text": item.get("say") or item["prompt"]})
    for q in pkg["engine"]["quiz"]:
        lines.append({"id": f"q{q['id']}", "text": q["q"] + " " + ", or ".join(q["o"])})
    # de-dupe by id
    seen = {}
    for line in lines:
        seen[line["id"]] = line
    return list(seen.values())


def write_pkg(pkg):
    lid = pkg["id"]
    dest = os.path.join(LESSONS, lid)
    os.makedirs(os.path.join(dest, "media"), exist_ok=True)
    lesson = {
        "id": lid,
        "title": pkg["title"],
        "subject": "reading",
        "band": "k2",
        "grade_hint": "1",
        "objectives": [pkg["objective"]],
        "va_sol": pkg["va"],
        "duration_min": 12,
        "anchor": {"book": "aesop-fables", "note": pkg["anchor"], "research": pkg["research"]},
        "stages": ["hook", "teach", "practice", "check"],
        "check": {"quiz_id": pkg["quiz_id"], "n_items": 5, "pass": 4},
        "animations": [pkg["anim"]],
        "reduced_motion": True,
        "version": 1,
        "entry": "index.html",
    }
    assets = {
        "lesson": lid,
        "style": "../../../tools/lesson_assets/style.json",
        "voice": voices_for(pkg),
        "images": [
            {"id": "hook", "prompt": f"storybook scene for {pkg['title']}, Aesop meadow, no letters", "kind": "scene"}
        ],
        "clips": [],
        "notes": "House voice is luna (Grok TTS, British woman, 0.92). Packages run with speechSynthesis until media/ is generated.",
    }
    with open(os.path.join(dest, "lesson.json"), "w") as f:
        json.dump(lesson, f, indent=2)
        f.write("\n")
    with open(os.path.join(dest, "assets.json"), "w") as f:
        json.dump(assets, f, indent=2)
        f.write("\n")
    with open(os.path.join(dest, "index.html"), "w") as f:
        f.write(html_for(pkg))
    with open(os.path.join(dest, "media", "index.js"), "w") as f:
        f.write("window.GOJI_MEDIA=window.GOJI_MEDIA||{img:{},clip:{},voice:{}};\n")
    if os.path.isdir(os.path.dirname(SEED)):
        seed_dest = os.path.join(SEED, lid)
        if os.path.isdir(seed_dest):
            shutil.rmtree(seed_dest)
        shutil.copytree(dest, seed_dest)
    print("wrote", lid)


if __name__ == "__main__":
    os.makedirs(LESSONS, exist_ok=True)
    os.makedirs(SEED, exist_ok=True)
    for pkg in PACKAGES:
        write_pkg(pkg)
