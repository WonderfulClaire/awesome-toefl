# Changelog

本项目遵循[语义化版本](https://semver.org/lang/zh-CN/)（主版本.次版本.修订号）。所有重要变更记录于此。

---

## [v1.0.0] — 2026-08-13

首个稳定版本。awesome-toefl 从「指南」升级为「可直接使用的备考工具 + 社区题库」。

### ✨ 新增
- **英文 README（[README_EN.md](README_EN.md)）**，第一屏提供中英文切换，面向国际受众。
- **题库与练习台第一屏入口**：README 顶部新增醒目的「立即开始 / Start」按钮，直达[在线练习台](https://wonderfulclaire.github.io/awesome-toefl/practice.html)。
- **高分范文库（[`bank/writing/samples/`](bank/writing/samples/)）**：合并自 `toefl-learn`，新增 11 篇真题风格范文（综合写作 5 + 学术讨论 6），每篇含题目 + 英文范文 + 中文逐段解析。
- **写作参考指南（[`docs/06-writing/`](docs/06-writing/)）**：合并 `toefl-learn` 的 3 份资料——评分量表 `scoring-rubric.md`、高分句库 `sentence-bank.md`、模板骨架 `templates.md`。
- **AWL 学术词汇训练营（[`tools/vocab/`](tools/vocab/)）**：570 个学术高频词，间隔重复 + 自测，进度存本机。
- **写作交互引擎（[`tools/writing-interactive.html`](tools/writing-interactive.html)）**：浏览器内拆解范文结构、对照模板练笔。
- **无 API Key 模式说明**：明确练习台抽题 / 限时 / 即点即判 / 进度保存全部离线可用，AI 批改为可选功能。
- **题库格式说明（[`bank/FORMAT.md`](bank/FORMAT.md)）**：定义 `bank/data.js` 的题目结构与 `.md` 题库的投稿规范，方便社区补题。
- **Issue / PR 模板（`.github/`）**：新增 Bug 报告、新题投稿、功能建议模板与 PR 模板。
- **版本与更新时间徽章**：README 标注 `v1.0.0` 与最后更新日期。

### ♻️ 变更
- 原独立仓库 `toefl-learn` 的写作范文与词汇工具已合并进本仓库，`toefl-learn` 标记为 archived。
- `homepage` 字段指向 GitHub Pages 站点 `https://wonderfulclaire.github.io/awesome-toefl/`。

### 📌 说明
- 阅读 / 听力题为 **ETS 风格练习文本，非官方真题**，仅供方法训练。
- 写作范文为真题风格示例，非 ETS 官方发布。
- 题目与资料持续征集 PR，详见[贡献指南](CONTRIBUTING.md)。

---

## [v0.x] — 早期版本（汇总）

- 初版指南体系：9 个章节文档（`docs/`）。
- 在线练习台 `practice.html` + 题库 `bank/` + AI 陪练 `tools/ai_coach.py`。
- 已开通 GitHub Pages 站点。
- 已配置 topics：`toefl` / `toefl-2026` / `english-learning` / `exam-preparation` / `toefl-ibt` 等。
