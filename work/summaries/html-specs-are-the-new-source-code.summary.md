# 规格说明就是新的源代码（导读）

> 来源：Ravi Mehta and Danny Martinez（Ravi on Product，2025-07-31） · 文章 id：`html-specs-are-the-new-source-code` · 原文约 11.9K 字符

## 核心主张
本文由 Ravi Mehta 与 Danny Martinez 撰写，提出一个反直觉的论断：在 AI 让「构建」不再成为瓶颈的时代，规格说明（Spec）正从被随手丢弃的 paperwork 变成「新的源代码」。核心论点是：AI 生成的代码只是规格的 "lossy projection"，真正承载完整意图、并同时对齐人与机器的是 spec；因此稀缺技能不再是编码，而是写出充分捕捉意图与价值的规格。原型没有杀死 spec，反而让 spec 变得更好——它能成为产品团队与 LLM 共同的 source of truth。

## 关键要点（原文引用）
- 引用 OpenAI 的 Sean Grove 在演讲 The New Code 中的论点：a well-written prompt（即 spec）is the new source code。
- Grove 的名句："This feels like you shred the source and then you very carefully version control the binary."——我们留下代码却丢掉提示词，如同撕掉源码却给二进制做版本管理。
- 引 Andrew Ng 在 Building Faster with AI 中的观察："For the first time in my life that I saw managers proposed to me having twice as many PMs as engineers."
- 工作流对比：旧流程 vague idea → wireframes → designs → engineer-built MVP → customer feedback → painful spec revision → rebuild → pray；新流程 vague idea → rapid prototype → customer feedback → crystal-clear spec → AI-assisted implementation。
- 原型工具：v0、Lovable、Replit 让人无需工程即可在 hours, not weeks 内做出可用原型，从而在写 spec 之前先收集真实客户反馈。
- Danny 的实操技术栈：Project management tool: Linear；IDE: VS Code；Extension: GitHub Copilot Pro；Model: Claude Sonnet 4；MCP Server: Linear MCP server（让 Copilot 访问 Linear tickets）。
- 实操步骤与时间戳：00:14 从 Slack 消息生成 Linear ticket；01:18 让 Claude 打开 ticket；01:52 让 Claude 对照代码库分析；02:30 让 Claude 建分支并实现；02:52 测试改动；03:55 在 GitHub 开 pull request；随后等待工程师 review/approve。
- 三个必要前提：Being specific（含糊的 spec 只会得到混乱的代码库）、Being selective（越复杂的 ticket 越需要懂行的人介入）、Gatekeeping（需要一个真正的工程师 review PR，平衡简洁与功能）。
- 愿景："One day, you might even expect an AI agent to ship your ticket whilst you sip your coffee."
- 引用 William Gibson 的名言："The future is already here—it's just not very evenly distributed."——生成代码已到 AI 速度，而理解客户、发现需求仍停留在人类速度。

## 术语与译法
- `Spec` → 规格说明
- `Spec-driven Development` → 规格驱动开发
- `LLM` → 大语言模型
- `Pull Request` → 拉取请求
- `Repository` → 仓库
- `Agent` → 智能体
- `MCP Server` → MCP 服务器
- `Vibe Coding` → 氛围编程

## 结论
当 AI 把实现变得廉价，产品团队的价值重心从「实现工作」转向「理解工作」：spec 成为对齐团队、指导实现并在自动化开发中留存的关键产物。抓住能写清意图的规格能力，非技术人员也能借助 AI 与工程师协作，把想法一路走到线上功能。
