/**
 * K.MG.2 sit-through trust rules.
 * School owns the pack. This only decides the one audit row.
 * Catalog coverage is never written here.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.GojiKmg2Audit = factory();
  }
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  var FLASH_PASS = 9;
  var FLASH_TOTAL = 10;
  var ATTRIBUTES = [
    /\bround\b/i,
    /\bthree corners\b|\b3 corners\b/i,
    /\bfour same sides\b|\bsame sides\b|\bfour sides.{0,40}same\b/i,
    /\btwo long\b.{0,40}\btwo short|\btwo short\b.{0,40}\btwo long/
  ];

  function num(v) {
    var n = Number(v);
    return Number.isFinite(n) ? n : NaN;
  }

  function journalOk(text) {
    var t = String(text || '').trim();
    if (t.length < 12) return false;
    if (!/\bbecause\b/i.test(t)) return false;
    for (var i = 0; i < ATTRIBUTES.length; i++) {
      if (ATTRIBUTES[i].test(t)) return true;
    }
    return false;
  }

  function derive(state) {
    state = state || {};
    var correct = num(state.flashcardCorrect);
    var total = num(state.flashcardTotal);
    var hasRun = Number.isFinite(correct) && Number.isFinite(total) && total > 0;
    var htmlOk = !!state.htmlFinished;
    var practiceOk = hasRun && correct >= FLASH_PASS && total >= FLASH_TOTAL;
    var journal = journalOk(state.journal);
    var parentPass = state.parentVerdict === 'pass';
    var parentSet = state.parentVerdict === 'pass' || state.parentVerdict === 'not_yet';

    var attempted = !!(
      htmlOk ||
      hasRun ||
      String(state.journal || '').trim() ||
      parentSet ||
      state.teachOpened
    );

    // Several items = the School 10-item run. A 1-tap score is not confident.
    var confident = hasRun && total >= FLASH_TOTAL;
    var allThree = htmlOk && practiceOk && journal;
    var passed = !!(confident && allThree && parentPass);

    return {
      skillSol: 'K.MG.2',
      skillId: 'obj.math.k2.shapes.01',
      coverage: 'gap',
      attempted: attempted,
      passed: passed,
      showPassed: confident,
      passedLabel: confident ? (passed ? 'yes' : 'no') : '—',
      confidence: confident ? 'confident' : 'not confident',
      htmlOk: htmlOk,
      practiceOk: practiceOk,
      journalOk: journal,
      allThree: allThree
    };
  }

  function buildRun(cards, rand) {
    var list = (cards || []).slice();
    var rnd = typeof rand === 'function' ? rand : Math.random;
    function shuffle(arr) {
      var a = arr.slice();
      for (var i = a.length - 1; i > 0; i--) {
        var j = Math.floor(rnd() * (i + 1));
        var t = a[i];
        a[i] = a[j];
        a[j] = t;
      }
      return a;
    }
    var extras = shuffle(list).slice(0, 2);
    return shuffle(list.concat(extras));
  }

  return {
    FLASH_PASS: FLASH_PASS,
    FLASH_TOTAL: FLASH_TOTAL,
    journalOk: journalOk,
    derive: derive,
    buildRun: buildRun
  };
});
