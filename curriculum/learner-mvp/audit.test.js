'use strict';

var test = require('node:test');
var assert = require('node:assert/strict');
var fs = require('node:fs');
var path = require('node:path');
var audit = require('./audit.js');

var catalog = fs.readFileSync(
  path.join(__dirname, '..', 'skills', 'math-k.md'),
  'utf8'
);

test('catalog K.MG.2 stays gap', function () {
  var row = catalog.split('\n').find(function (line) {
    return line.indexOf('| K.MG.2 |') === 0;
  });
  assert.ok(row, 'K.MG.2 row exists');
  assert.match(row, /\*\*gap\*\*/);
  assert.doesNotMatch(row, /\*\*covered\*\*/);
});

test('pack does not flip coverage', function () {
  var pack = JSON.parse(fs.readFileSync(path.join(__dirname, 'pack.json'), 'utf8'));
  assert.equal(pack.coverage, 'gap');
  assert.equal(pack.do_not_flip_coverage, true);
  assert.equal(pack.skill.objective_id, 'obj.math.k2.shapes.01');
  assert.equal(pack.practice.cards.length, 8);
  assert.equal(pack.practice.seed_pipeline, false);
  assert.equal(pack.teach.do_not_rewrite, true);
});

test('lucky tap 1/1 hides passed', function () {
  var row = audit.derive({
    htmlFinished: true,
    flashcardCorrect: 1,
    flashcardTotal: 1,
    journal: 'This is a circle because it is round.',
    parentVerdict: 'pass'
  });
  assert.equal(row.confidence, 'not confident');
  assert.equal(row.showPassed, false);
  assert.equal(row.passedLabel, '—');
  assert.equal(row.passed, false);
});

test('9/10 + journal + html + parent pass is passed and visible', function () {
  var row = audit.derive({
    htmlFinished: true,
    flashcardCorrect: 9,
    flashcardTotal: 10,
    journal: 'This is a square because it has four same sides.',
    parentVerdict: 'pass'
  });
  assert.equal(row.confidence, 'confident');
  assert.equal(row.showPassed, true);
  assert.equal(row.passed, true);
  assert.equal(row.passedLabel, 'yes');
  assert.equal(row.coverage, 'gap');
});

test('any piece fail is not passed', function () {
  var base = {
    htmlFinished: true,
    flashcardCorrect: 9,
    flashcardTotal: 10,
    journal: 'This is a triangle because it has three corners.',
    parentVerdict: 'pass'
  };
  assert.equal(audit.derive(Object.assign({}, base, { htmlFinished: false })).passed, false);
  assert.equal(audit.derive(Object.assign({}, base, { flashcardCorrect: 8 })).passed, false);
  assert.equal(audit.derive(Object.assign({}, base, { journal: 'circle' })).passed, false);
  assert.equal(audit.derive(Object.assign({}, base, { parentVerdict: 'not_yet' })).passed, false);
});

test('10-item miss still shows passed=no when confident', function () {
  var row = audit.derive({
    htmlFinished: true,
    flashcardCorrect: 6,
    flashcardTotal: 10,
    journal: 'This is a rectangle because it has two long and two short sides.',
    parentVerdict: 'pass'
  });
  assert.equal(row.confidence, 'confident');
  assert.equal(row.passedLabel, 'no');
  assert.equal(row.passed, false);
});

test('journal needs because plus a School attribute', function () {
  assert.equal(audit.journalOk('This is a circle because it is round.'), true);
  assert.equal(audit.journalOk('This is a triangle because it has three corners.'), true);
  assert.equal(audit.journalOk('This is a square because four same sides.'), true);
  assert.equal(audit.journalOk('This is a rectangle because two long and two short.'), true);
  assert.equal(audit.journalOk('This is a circle because I like it.'), false);
  assert.equal(audit.journalOk('round'), false);
});

test('run is 8 cards plus 2 repeats', function () {
  var cards = [1, 2, 3, 4, 5, 6, 7, 8];
  var n = 0;
  var run = audit.buildRun(cards, function () {
    n += 0.17;
    return n % 1;
  });
  assert.equal(run.length, 10);
  cards.forEach(function (c) {
    assert.ok(run.indexOf(c) !== -1);
  });
});
