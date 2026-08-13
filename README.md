<div align="center">

# 🏆 Awesome TOEFL 2026

**第一个针对 2026 新版托福（TOEFL iBT）的体系化开源备考指南**

[English](README_EN.md) · 中文

不是资料堆砌，而是一条从 0 到目标分的完整路线：
**认知考试 → 制定计划 → 分项突破 → AI 陪练 → 考场实战**

[![🚀 立即开始 Start](https://img.shields.io/badge/%F0%9F%9A%80%20立即开始%20Start-EF476F?style=for-the-badge)](https://wonderfulclaire.github.io/awesome-toefl/practice.html)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](CHANGELOG.md)
[![Updated](https://img.shields.io/badge/updated-2026--08--13-brightgreen)](CHANGELOG.md)
[![Stars](https://img.shields.io/github/stars/WonderfulClaire/awesome-toefl?style=social)](https://github.com/WonderfulClaire/awesome-toefl/stargazers)
[![新版托福](https://img.shields.io/badge/TOEFL-2026%20新版-blue.svg)](docs/01-getting-started/new-toefl-2026.md)

**🔗 [在线练习台（无需 API Key 即可刷题）](https://wonderfulclaire.github.io/awesome-toefl/practice.html)**

</div>

---

## ⚡ 为什么需要这个仓库？

**2026 年 1 月 21 日起，托福迎来史上最大改革**：自适应考试、5 大新题型、口语砍半、新增 1–6 分制。
而市面上绝大多数备考资料（包括 GitHub 上的高星仓库）仍停留在旧版考试，方法论已部分失效。

这个仓库做三件事：

1. **讲透新版考试** —— 新旧对比、题型逐个拆解、评分逻辑；
2. **给出可执行的方法** —— 每个单项都有「能力训练 + 应试策略 + 模板」三层结构；
3. **拥抱 AI 备考** —— 一套完整的提示词工作流，把 AI 变成你的私人外教。

---

## 🗺️ 学习路线图

<img src="assets/toefl-roadmap.svg" alt="TOEFL 2026 学习路线图：认知 → 规划 → 分项突破 → AI 陪练 + 模考 → 考场实战 → 出分复盘" width="100%">

---

## 📚 目录

### 第一部分 · 入门与规划

| 章节 | 内容 | 适合谁 |
| --- | --- | --- |
| [🆕 2026 新版托福完全解读](docs/01-getting-started/new-toefl-2026.md) | 改革全貌、新旧对比、四科题型逐个拆解 | 所有人（必读） |
| [📊 分数体系与目标设定](docs/01-getting-started/score-and-cefr.md) | 1–6 分制、CEFR 对照、如何定目标分 | 所有人（必读） |
| [🗓️ 备考计划](docs/01-getting-started/study-plans.md) | 1 / 3 / 6 个月三套计划 + 每日时间表 | 准备开始备考的人 |

### 第二部分 · 分项突破

| 章节 | 核心内容 |
| --- | --- |
| [📖 词汇](docs/02-vocabulary/vocabulary-guide.md) | 词汇量自测、艾宾浩斯循环法、词表选择、Anki 用法 |
| [📕 阅读](docs/03-reading/reading-guide.md) | 自适应机制下的答题策略、3 类新题型攻略、长难句训练 |
| [🎧 听力](docs/04-listening/listening-guide.md) | 4 类新题型攻略、精听法（听写/跟读/复述）、笔记法 |
| [🎤 口语](docs/05-speaking/speaking-guide.md) | Listen & Repeat 复述训练法、Interview 应答框架与万能素材 |
| [✍️ 写作](docs/06-writing/writing-guide.md) | Build a Sentence 语法专项、邮件写作模板、学术讨论高分框架、11 篇高分范文 |

### 第三部分 · 工具与实战

| 章节 | 核心内容 |
| --- | --- |
| [🤖 AI 辅助备考](docs/07-ai-prep/ai-toolkit.md) | 提示词库 + 一键直开 ChatGPT 链接 + 零依赖本地陪练工具 `ai_coach.py`（接你自己的 API Key 无限刷题） |
| [🧰 资源汇总](docs/08-resources/resources.md) | 官方资源、免费网站、App、模考平台（全部亲测可用逻辑筛选） |
| [🎯 考场实战](docs/09-test-day/test-day-guide.md) | 报名流程、考前清单、考场时间管理、送分与复议 |

---

## 🎯 题库与练习台（边练边改）

光看不练等于没学。本仓库配套一套**可练、可改、可贡献**的题库与练习台：

- 🖥️ **[在线练习台 practice.html](practice.html)** —— 单页应用，随机抽题 / 限时模拟 / 写作口语**页面内直接 AI 批改**（接你自己的 API Key，与 coach.html 共用配置）/ 阅读听力即点即判 + AI 错因分析，进度存本机。
- 📦 **题库源文件**（`bank/`，Markdown，欢迎 PR 补题）：
  - ✍️ [写作 · 邮件（6 题）](bank/writing/email.md) ｜ [写作 · 学术讨论（8 题）](bank/writing/academic-discussion.md)
  - 🎤 [口语 · 访谈（14 题）](bank/speaking/interview.md) ｜ [口语 · 听后复述句库](bank/speaking/repeat-sentences.md)
  - 📖 [阅读（3 篇 · 各 5 题）](bank/reading/) ｜ 🎧 [听力（3 篇 · 各 4 题）](bank/listening/)
  - 💎 [高分语料库（写作/口语/衔接）](bank/_phrases/phrases.md)
- 📝 **[高分范文库](bank/writing/samples/)** —— 11 篇真题风格范文（综合写作 5 + 学术讨论 6），每篇配题目 + 英文范文 + 中文逐段解析，直接对标上面的练习题库。
- 🧠 **[AWL 学术词汇训练营](tools/vocab/vocab.html)** —— 570 个学术高频词，间隔重复 + 自测，进度存本机。
- ✍️ **[写作交互引擎](tools/writing-interactive.html)** —— 浏览器内拆解范文结构、对照模板练笔。

> 💡 **无需 API Key 即可使用**：抽题 / 限时 / 即点即判 / 进度保存全部离线可用；只有点「AI 批改」时才需要填入你自己的 API Key（与 `coach.html` 共用配置）。没有 Key 也能完整刷题。

> 阅读/听力题为 **ETS 风格练习文本，非官方真题**，仅供方法训练；听力文字稿请配合官方或免费音频使用（见[资源页](docs/08-resources/resources.md)）。写作范文为真题风格示例，非 ETS 官方发布。

---

## 🚀 快速开始（3 分钟版）

1. **先去练一练** 👉 [在线练习台](https://wonderfulclaire.github.io/awesome-toefl/practice.html) —— 不用装任何东西，打开就能刷一套；
2. **再读** [2026 新版托福完全解读](docs/01-getting-started/new-toefl-2026.md)，5 分钟搞清楚你要考的是什么；
3. **做一次** [官方免费模考](docs/08-resources/resources.md#官方资源) 摸清基础分；
4. **对照** [备考计划](docs/01-getting-started/study-plans.md) 选一套适合你的方案，开始执行；
5. **每天用** [AI 提示词](docs/07-ai-prep/ai-toolkit.md) 做批改和陪练，替代昂贵的一对一。

---

## 💡 本仓库的三个原则

> 1. **新版优先**：所有策略基于 2026 改革后的考试设计，旧版内容仅作对照；
> 2. **方法 > 资料**：拒绝网盘链接堆砌，每一章都是可执行的训练方案；
> 3. **免费 > 付费**：优先推荐官方与免费资源，付费项目明确标注且仅在无免费替代时出现。

---

## 🤝 贡献

欢迎分享你的备考经验、勘误、新资源、新题目！请阅读 [贡献指南](CONTRIBUTING.md) 与[题库格式说明](bank/FORMAT.md)。
高质量的考情回忆（尤其是新版考试的真实考场体验）和**新题投稿**是目前最需要的贡献。

## 📄 许可

本仓库采用 [CC BY-NC-SA 4.0](LICENSE) 许可 —— 可自由转载与修改，但需署名、禁止商用、需以相同方式共享。

---

<div align="center">

**如果这个仓库帮到了你，请点一个 ⭐ Star —— 这是对开源内容最好的支持。**

</div>
