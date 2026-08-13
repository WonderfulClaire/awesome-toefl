/* =============================================================================
 * TOEFL AWL 词汇训练引擎 · 纯逻辑层（无 DOM 依赖）
 * -----------------------------------------------------------------------------
 * 设计原则：所有可被单元测试覆盖的"大脑"都放在这里，UI 只负责渲染与持久化。
 * - Leitner 间隔重复（5 盒：box 0..4，间隔 0/1/3/7/16 天）
 * - 选词队列（到期优先 → 新词 → 全量兜底，防止卡死）
 * - 统计（已学/待复习/掌握/薄弱）
 * - 自测选择题生成（从同批词里抽干扰项）
 * - 打卡连续天数
 *
 * 同时兼容浏览器（挂到 window.VocabEngine）与 Node（module.exports），便于冒烟测试。
 * ========================================================================== */
(function (root) {
  'use strict';

  // 盒子间隔（天）。box 0 = 当天重来，box 4 = 16 天后复习。
  var INTERVALS = [0, 1, 3, 7, 16];
  var DAY = 86400000;

  function clampBox(b) {
    b = (b | 0);
    if (b < 0) return 0;
    if (b > 4) return 4;
    return b;
  }

  // 一次打分后的状态更新。state: {id: {box, due, updated, seen, correct, wrong}}
  // ok=true 进一盒；ok=false 回到 box 0（彻底重来）。
  function applyReview(state, id, ok, now) {
    state = state || {};
    now = now || Date.now();
    var prev = state[id] || { box: 0, due: 0, updated: 0, seen: 0, correct: 0, wrong: 0 };
    var box = clampBox(prev.box);
    box = ok ? Math.min(4, box + 1) : 0;
    var due = now + INTERVALS[box] * DAY;
    state[id] = {
      box: box,
      due: due,
      updated: now,
      seen: (prev.seen || 0) + 1,
      correct: (prev.correct || 0) + (ok ? 1 : 0),
      wrong: (prev.wrong || 0) + (ok ? 0 : 1)
    };
    return state;
  }

  // 是否到期（新词 = 无记录 = 立即学）
  function isDue(card, now) {
    if (!card) return true;
    return (card.due || 0) <= (now || Date.now());
  }

  function dedupe(arr) {
    var seen = {}, out = [];
    arr.forEach(function (x) { if (!seen[x]) { seen[x] = 1; out.push(x); } });
    return out;
  }

  // 选本场复习队列
  // opts: { now, allowNew=true, ids 子集（如指定 sublist） }
  function pickSession(state, allIds, opts) {
    opts = opts || {};
    var now = opts.now || Date.now();
    state = state || {};
    var ids = opts.ids || allIds;

    var due = ids.filter(function (id) { return isDue(state[id], now); });
    if (due.length) return dedupe(due);

    // 没有到期词
    if (opts.allowNew !== false) {
      var fresh = ids.filter(function (id) { return !state[id] || !state[id].seen; });
      if (fresh.length) return dedupe(fresh);
      // 全部见过且没有到期 → 全部过一遍（兜底，避免"今日无事可做"卡死）
      return dedupe(ids.slice());
    }
    return [];
  }

  // 统计
  function stats(state, allIds, now) {
    now = now || Date.now();
    state = state || {};
    var boxCounts = [0, 0, 0, 0, 0];
    var due = 0, seen = 0, weak = 0, mastered = 0;
    allIds.forEach(function (id) {
      var c = state[id];
      if (c && c.seen) {
        seen++;
        var b = clampBox(c.box);
        boxCounts[b]++;
        if (b <= 1) weak++;
        if (b === 4) mastered++;
      }
      if (isDue(c, now)) due++;
    });
    return {
      total: allIds.length,
      seen: seen,
      due: due,
      weak: weak,
      mastered: mastered,
      boxCounts: boxCounts
    };
  }

  // 生成一道选择题。answer=正确项（AWL 条目），pool=同批候选，n=选项数
  function makeQuiz(answer, pool, n) {
    n = n || 4;
    var distract = pool
      .filter(function (x) { return x.w !== answer.w; })
      .sort(function () { return Math.random() - 0.5; })
      .slice(0, n - 1)
      .map(function (x) { return x.zh; });
    var opts = distract.concat([answer.zh]);
    // Fisher–Yates 打乱
    for (var i = opts.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = opts[i]; opts[i] = opts[j]; opts[j] = t;
    }
    return {
      word: answer.w,
      correct: answer.zh,
      options: opts,
      correctIndex: opts.indexOf(answer.zh)
    };
  }

  function pad(x) { return x < 10 ? '0' + x : '' + x; }
  function dayKey(d) {
    return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
  }

  // 连续打卡天数。daySet: ['YYYY-MM-DD', ...]
  function streak(daySet) {
    var s = {};
    (daySet || []).forEach(function (d) { s[d] = 1; });
    var d = new Date();
    // 今天没学但昨天学了 → 从昨天起算；今天昨天都没学 → 0
    if (!s[dayKey(d)]) {
      d.setDate(d.getDate() - 1);
      if (!s[dayKey(d)]) return 0;
    }
    var cur = 0;
    while (s[dayKey(d)]) { cur++; d.setDate(d.getDate() - 1); }
    return cur;
  }

  var API = {
    INTERVALS: INTERVALS,
    clampBox: clampBox,
    applyReview: applyReview,
    isDue: isDue,
    pickSession: pickSession,
    stats: stats,
    makeQuiz: makeQuiz,
    streak: streak
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = API;
  root.VocabEngine = API;
})(typeof window !== 'undefined' ? window : this);
