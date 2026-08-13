# 题库格式说明（Question Bank Format）

欢迎给 awesome-toefl 贡献题目！本文件说明 `bank/` 下各类题库的**书写约定**。
`scripts/build_practice.py` 会按这些约定把 Markdown 编译成 `bank/data.js`，供 `practice.html` 直接加载——**你只需要按格式写 `.md`，然后跑一下构建脚本即可**。

> 新增题目最稳妥的方式：**复制一个现有同类型条目，替换内容，保持所有小标题不变**。

---

## 0. 通用规则

1. 每个题库文件用 `#` 写大标题，`>` 写说明，`##` 分隔每道题，`###` 分隔题目内的子块。
2. **ID 命名**：题型前缀 + 序号，全局唯一，不要和已有 ID 重复。
   | 题型 | 文件 | ID 前缀 | 示例 |
   | --- | --- | --- | --- |
   | 写作 · 邮件 | `bank/writing/email.md` | `W-E` | `W-E07` |
   | 写作 · 学术讨论 | `bank/writing/academic-discussion.md` | `W-A` | `W-A09` |
   | 口语 · 访谈 | `bank/speaking/interview.md` | `S-I` | `S-I15` |
   | 口语 · 听后复述 | `bank/speaking/repeat-sentences.md` | `S-R` | `S-R03` |
   | 阅读 | `bank/reading/rN.md` | 按 Passage 编号 | `R4` |
   | 听力 | `bank/listening/lN.md` | 按 Transcript 编号 | `L4` |
3. 改完 `.md` 后必须重新生成 `data.js`：
   ```bash
   python scripts/build_practice.py
   ```
   提交时请同时提交改动后的 `.md` **和**重新生成的 `bank/data.js`。

> ⚠️ 阅读 / 听力题为 **ETS 风格练习文本，非官方真题**，仅供方法训练；写作范文为真题风格示例。投稿时请注明来源或声明为自编。

---

## 1. 写作 · 邮件（`bank/writing/email.md`）

每道题是一个 `##` 区块，字段如下（顺序随意，小标题必须一致）：

```markdown
## W-E07 · 一句话描述这道题
**情境**：给考生的情境说明（谁、什么场合、要写什么）。
**要求**：
1. 内容点一
2. 内容点二
3. 内容点三
**限时**：7 分钟
**难度**：★★☆

### 满分范文
Dear Professor Smith,

（英文范文，用真实、具体的例子，80+ 词）

Best regards,
Li Hua

### 高分短语
- 短语或句型 → 为什么好 / 使用注意
- 另一个短语 → 注解

### 结构拆解
1. 开门见山：……
2. 展开：……
3. 收尾：……
```

---

## 2. 写作 · 学术讨论（`bank/writing/academic-discussion.md`）

结构与邮件一致，ID 用 `W-A` 前缀，**难度按 10 分钟写 110–160 词**设计：

```markdown
## W-A09 · 一句话描述
**情境**：教授问题 + 两位同学已有观点（贴新版真实考法）。
**要求**：
1. 直接回应教授问题
2. 给出一个说透的理由 + 具体例子
3. 与至少一位同学观点互动
**限时**：10 分钟
**难度**：★★★☆☆

### 满分范文
（英文范文，注意「部分认同 + 推进一层」的互动感）

### 高分短语
- …… → ……

### 结构拆解
1. ……
2. ……
```

---

## 3. 口语 · 访谈（`bank/speaking/interview.md`）

```markdown
## S-I15 · 一句话描述
**问题**：What do you usually do to relax after a busy day?
**类型**：经历 / 观点
**可挂素材**：一次坚持的爱好 · 压力释放
**限时**：45 秒

### 示范回答
（英文回答，说满 35 秒以上，语言自然优先于立场）

### 应答结构
1. 直接回答：……
2. 展开：……
3. 例子收尾：……
```

---

## 4. 阅读（`bank/reading/rN.md`）

一篇 Passage + 一组题目；`## 题目` 下用 `### Qn` 分隔每题：

```markdown
# 阅读 Passage R4 · 文章标题
> 练习文本（ETS 风格，非官方真题）。训练目标：……

（英文文章正文，若干段落）

## 题目

### Q1
**题干**：According to Paragraph 1, ...?
**选项**：
A. ...
B. ...
C. ...
D. ...
**答案**：B
**解析**：（说明为什么选 B、排除其它）
```

---

## 5. 听力（`bank/listening/lN.md`）

与阅读同构，正文是带说话人标记的 Transcript：

```markdown
# 听力 Transcript L4 · Office Hour 对话
> 文字稿练习素材，配合官方/免费音频使用。训练目标：听辨目的 + 态度 + 细节。

**Professor Diaz:** Thanks for stopping by, Kevin. ...
**Kevin:** Yeah, I got the paper back, ...

## 题目

### Q1
**题干**：Why did Kevin visit the professor?
**选项**：
A. ...
B. ...
C. ...
D. ...
**答案**：B
**解析**：……
```

---

## 6. 口语 · 听后复述（`bank/speaking/repeat-sentences.md`）

句库形式，按现有条目结构续写即可（保持已有的 `##` 小标题约定）。

---

## 7. 提交清单（PR 前自查）

- [ ] 题目放在正确的 `bank/` 文件、正确的题型分区；
- [ ] ID 唯一、不与已有重复；
- [ ] 所有 `###` 子块标题与现有条目一致；
- [ ] 范文 / 示范回答英文地道、例子具体；
- [ ] 已运行 `python scripts/build_practice.py` 并提交了更新后的 `bank/data.js`；
- [ ] 阅读 / 听力标注为 ETS 风格练习文本，非官方真题。

不确定格式？直接复制最近的同类型条目改内容最稳。有问题开 Issue 或 PR 里留言即可。
