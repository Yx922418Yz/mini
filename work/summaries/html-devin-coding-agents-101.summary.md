# 编码智能体 101：真正把事情做成的艺术（导读）

> 来源：Cognition Team（Devin 团队） · 文章 id：`html-devin-coding-agents-101` · 原文约 21.6K 字符

## 核心主张
文章面向软件工程师，说明自主编码智能体（autonomous Coding Agent）已能「把最初的描述一路推进到最终的拉取请求（Pull Request）」，只需少量人工介入。作者认为，能否用好这类工具的关键不在模型本身，而在于工程师的提示方式、工作流集成与验证习惯。资深到资深以上（senior-to-staff）的工程师上手最快，但人类仍需对代码的最终正确性负责。

## 关键要点（原文引用）
- 工具形态覆盖 web app、mobile app，以及 Slack、GitHub、Linear、Jira 等集成；近年发布的产品包括 Devin、OpenAI 的 Codex、Google 的 Jules，Cursor 与 Claude Code 可在并行的 workspace 中运行以复现类似效果。
- 第一条提示原则：说清「怎么做」而不只是「做什么」（"Say how you want things done, not just what"）。例如不要只说 "add unit tests"，而要指明要测试的功能、关键边界情况以及需要 mock 的部分。
- 要告诉智能体从何处入手（"Tell the agent where to start"）：即使不知道具体文件或函数名，也应给出仓库、相关文档与关键组件。
- 采用防御式提示（defensive prompting）：像给新来的实习生布置任务一样预判可能的混淆，例如提醒修改 C++ bindings 后每次都要重新编译再测试。
- 给智能体接入 CI、测试、类型系统与 linter，借助 type checkers、linters 与 unit tests 形成的反馈回路让它自我纠错；团队建议使用 typed Python 而非 plain Python，或 TypeScript 而非 JavaScript。
- 工作流用法：在 Slack 里 @Devin 处理小 bug 或小功能；通过移动端处理紧急问题；把 bisect 旧提交、更新文档等杂活交出去；让智能体分别实现两个架构方案以消除选择困难（在文本框选型中对比 Lexical 与 Slate，最终 Slate 胜出）。
- 设置 preview deployments（如使用 Vercel），让每个新 PR 自动生成可访问的实时 URL，便于评审 AI 完成的前端任务。
- 委派更大的工单是 ROI 最高的场景，典型为 1-6 小时的 medium-to-large 任务；让智能体先生成 PR 的初稿（first draft）可大幅削减工作量。
- 人类监督不可或缺：责任与验证始终是工程师的关键职责；软件工程师「不会消失」（"software engineers aren't going anywhere"）。
- 文章自我定位为 product-agnostic、tactical、technical 的指南，适合任何编码智能体。

## 术语与译法
- `Coding Agent` → 编码智能体
- `Agent` → 智能体
- `Prompt` → 提示词
- `Pull Request` → 拉取请求
- `Repository` → 仓库
- `Continuous Integration` → 持续集成
- `Unit Test` → 单元测试
- `Linter` → 静态检查器
- `Refactor` → 重构
- `Sandbox` → 沙箱
- `Permission` → 权限
- `Autonomy` → 自主性

## 结论
编码智能体已能端到端承担任务，但真正的杠杆来自工程师给出清晰的「怎么做」、把 CI/测试/类型系统接入反馈回路，并始终保留对最终代码的监督与所有权。
