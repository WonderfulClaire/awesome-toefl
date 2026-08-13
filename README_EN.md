<div align="center">

# 🏆 Awesome TOEFL 2026

**The first systematic, open-source prep guide built for the 2026 redesigned TOEFL iBT.**

[English](README_EN.md) · [中文](README.md)

Not another link dump — a complete path from 0 to your target score:
**Understand the exam → Make a plan → Drill each section → AI practice partner → Test-day execution**

[![🚀 Start Practicing](https://img.shields.io/badge/%F0%9F%9A%80%20Start%20Practicing-EF476F?style=for-the-badge)](https://wonderfulclaire.github.io/awesome-toefl/practice.html)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](CHANGELOG.md)
[![Updated](https://img.shields.io/badge/updated-2026--08--13-brightgreen)](CHANGELOG.md)
[![Stars](https://img.shields.io/github/stars/WonderfulClaire/awesome-toefl?style=social)](https://github.com/WonderfulClaire/awesome-toefl/stargazers)
[![TOEFL 2026](https://img.shields.io/badge/TOEFL-2026%20Redesign-blue.svg)](docs/01-getting-started/new-toefl-2026.md)

**🔗 [Online Practice App (no API key required)](https://wonderfulclaire.github.io/awesome-toefl/practice.html)**

</div>

---

## ⚡ Why this repository?

**Since January 21, 2026, TOEFL has undergone its biggest reform ever**: adaptive testing, 5 new question types, speaking cut in half, and a new 1–6 scoring scale.
Yet most prep materials on the market (including top-starred GitHub repos) are still built for the old exam — their methods are partly obsolete.

This repo does three things:

1. **Explains the new exam clearly** — old-vs-new comparison, every question type broken down, scoring logic explained;
2. **Gives actionable methods** — each section has a three-layer structure: *skill training + test strategy + templates*;
3. **Embraces AI prep** — a full prompt-workflow toolkit that turns AI into your personal tutor.

---

## 🗺️ Learning Roadmap

<img src="assets/toefl-roadmap.svg" alt="TOEFL 2026 learning roadmap: understand → plan → section drills → AI practice + mock → test day → score review" width="100%">

---

## 📚 Contents

### Part 1 · Getting Started & Planning

| Section | What's inside | For whom |
| --- | --- | --- |
| [🆕 Full guide to the 2026 TOEFL](docs/01-getting-started/new-toefl-2026.md) | The reform, old-vs-new, all four sections dissected | Everyone (must-read) |
| [📊 Scores & goal-setting](docs/01-getting-started/score-and-cefr.md) | 1–6 scale, CEFR mapping, how to set a target | Everyone (must-read) |
| [🗓️ Study plans](docs/01-getting-started/study-plans.md) | 1 / 3 / 6-month plans + daily schedules | Those ready to start |

### Part 2 · Section Drills

| Section | Core content |
| --- | --- |
| [📖 Vocabulary](docs/02-vocabulary/vocabulary-guide.md) | Self-test, spaced repetition, wordlist choice, Anki |
| [📕 Reading](docs/03-reading/reading-guide.md) | Strategy under adaptive mode, 3 new question types, long-sentence training |
| [🎧 Listening](docs/04-listening/listening-guide.md) | 4 new question types, intensive listening, note-taking |
| [🎤 Speaking](docs/05-speaking/speaking-guide.md) | Listen & Repeat method, Interview framework &万能素材 |
| [✍️ Writing](docs/06-writing/writing-guide.md) | Build-a-Sentence grammar, email templates, Academic Discussion high-score framework, 11 model essays |

### Part 3 · Tools & Execution

| Section | Core content |
| --- | --- |
| [🤖 AI-assisted prep](docs/07-ai-prep/ai-toolkit.md) | Prompt library + one-click ChatGPT links + zero-dependency local tutor `ai_coach.py` (bring your own API key) |
| [🧰 Resources](docs/08-resources/resources.md) | Official resources, free sites, apps, mock platforms (all vetted) |
| [🎯 Test day](docs/09-test-day/test-day-guide.md) | Registration, pre-test checklist, time management, score sending & rating review |

---

## 🎯 Question Bank & Practice App (practice + get feedback)

Reading without practicing is pointless. This repo ships a **practiceable, fixable, contributable** bank and app:

- 🖥️ **[Online Practice App `practice.html`](practice.html)** — single-page app: random draw / timed mock / in-page **AI grading** for writing & speaking (bring your own API key, shared config with `coach.html`) / click-to-check for reading & listening + AI error analysis. Progress saved locally.
- 📦 **Bank source files** (`bank/`, Markdown, PRs welcome):
  - ✍️ [Writing · Email (6)](bank/writing/email.md) ｜ [Writing · Academic Discussion (8)](bank/writing/academic-discussion.md)
  - 🎤 [Speaking · Interview (14)](bank/speaking/interview.md) ｜ [Speaking · Repeat-sentence bank](bank/speaking/repeat-sentences.md)
  - 📖 [Reading (3 passages · 5 Q each)](bank/reading/) ｜ 🎧 [Listening (3 · 4 Q each)](bank/listening/)
  - 💎 [High-score phrase bank (writing/speaking/transitions)](bank/_phrases/phrases.md)
- 📝 **[Model Essay Library](bank/writing/samples/)** — 11 exam-style model essays (5 Integrated + 6 Academic Discussion), each with prompt + English essay + line-by-line Chinese analysis, mapped to the practice bank above.
- 🧠 **[AWL Academic Vocabulary Trainer](tools/vocab/vocab.html)** — 570 academic word-family items, spaced repetition + self-test, progress saved locally.
- ✍️ **[Writing Interactive Engine](tools/writing-interactive.html)** — dissect model-essay structure and draft against templates, all in the browser.

> 💡 **No API key needed to use it**: drawing questions / timed mode / click-to-check / progress saving all work offline. You only need your own API key when you click **AI grading** (shared config with `coach.html`). You can practice the full bank without any key.

> Reading/listening items are **ETS-style practice texts, not official questions**, for method training only; pair listening transcripts with official or free audio (see [Resources](docs/08-resources/resources.md)). Model essays are exam-style examples, not released by ETS.

---

## 🚀 Quick Start (3-minute version)

1. **Practice first** 👉 [Online Practice App](https://wonderfulclaire.github.io/awesome-toefl/practice.html) — nothing to install, open and drill a set;
2. **Then read** [Full guide to the 2026 TOEFL](docs/01-getting-started/new-toefl-2026.md) to understand what you're taking in 5 minutes;
3. **Take** [one official free mock](docs/08-resources/resources.md#official-resources) to find your baseline;
4. **Pick** a plan from [Study plans](docs/01-getting-started/study-plans.md) and start executing;
5. **Use** [AI prompts](docs/07-ai-prep/ai-toolkit.md) daily for grading and tutoring instead of expensive 1-on-1.

---

## 💡 Three principles

> 1. **New-exam first**: all strategies are built on the post-2026 redesign; old content is reference only;
> 2. **Method > material**: no net-disk link dumps — every chapter is an executable training plan;
> 3. **Free > paid**: official and free resources first; paid items are clearly labeled and only appear when no free alternative exists.

---

## 🤝 Contributing

Share your prep experience, corrections, new resources, or new questions! Read the [Contributing Guide](CONTRIBUTING.md) and the [Question Bank Format](bank/FORMAT.md).
High-quality test-day recollections (especially real experiences with the new exam) and **new-question submissions** are the most needed contributions right now.

## 📄 License

This repository is licensed under [CC BY-NC-SA 4.0](LICENSE) — free to redistribute and modify, but must be attributed, non-commercial, and shared under the same license.

---

<div align="center">

**If this repo helped you, please leave a ⭐ Star — it's the best support for open-source content.**

</div>
