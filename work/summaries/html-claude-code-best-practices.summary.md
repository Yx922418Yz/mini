# Claude Code 概览（导读）

> 来源：Anthropic（Claude Code 官方文档） · 文章 id：`html-claude-code-best-practices` · 原文约 9.7K 字符

## 核心主张
这是 Claude Code 的官方概览页，回答「它是什么、怎么装、能做什么、能从哪些入口用」四个问题。核心论点是：Claude Code 是一个 AI 驱动的编码助手，能够理解整个代码库并跨多个文件与工具协同工作，帮助构建功能、修复缺陷、自动化开发任务；它是同一套引擎贯穿终端、IDE、桌面、Web 等多端，配置与 MCP 在各地一致。

## 关键要点（原文引用）
- 定位原文：`Claude Code is an AI-powered coding assistant that helps you build features, fix bugs, and automate development tasks. It understands your entire codebase and can work across multiple files and tools to get things done.`
- 安装（推荐 native install，后台自动更新）——macOS/Linux/WSL：`curl -fsSL https://claude.ai/install.sh | bash`；Windows PowerShell：`irm https://claude.ai/install.ps1 | iex`；Windows CMD：`curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`。Windows 需先装 Git for Windows。
- 其他安装方式：Homebrew `brew install --cask claude-code`、WinGet `winget install Anthropic.ClaudeCode`（两者不会自动更新，需手动 upgrade）。
- 启动：`cd your-project` 后运行 `claude`，首次使用会提示登录（log in）。
- 多端入口：Terminal、VS Code、Desktop app、Web、JetBrains；多数入口需要 Claude subscription 或 Anthropic Console account，Terminal CLI 与 VS Code 也支持第三方 provider。
- 自动化杂活：写测试、修 lint 错误、解决 merge conflicts、更新依赖、写 release notes，示例 `claude "write tests for the auth module, run them, and fix any failures"`。
- Git 集成：`claude "commit my changes with a descriptive message"`；可在 CI 中通过 GitHub Actions 或 GitLab CI/CD 自动化 code review 与 issue triage。
- 用 MCP 连接工具：`The Model Context Protocol (MCP) is an open standard for connecting AI tools to external data sources.`，可读取 Google Drive 设计文档、更新 Jira、拉取 Slack 数据。
- 定制能力：项目根目录的 `CLAUDE.md` 每次会话开始时读取；auto memory 自动记忆 build 命令与调试经验；custom commands 如 `/review-pr`、`/deploy-staging`；Hooks 在动作前后运行 shell 命令。
- 多智能体与自定义：可派生多个 Claude Code agent 并行协作，由 lead agent 协调；`Agent SDK` 支持构建自有 agent 并控制 orchestration、tool access 与 permissions。
- CLI 组合（Unix 风格）：`tail -200 app.log | claude -p "Slack me if you see any anomalies"`；`claude -p "translate new strings into French and raise a PR for review"`；`git diff main --name-only | claude -p "review these changed files for security issues"`。
- 定时任务：cloud scheduled tasks（在 Anthropic 基础设施上，关机也运行）、desktop scheduled tasks（本机）、`/loop` 轮询、CLI 中 `/schedule`。
- 跨端续作：Remote Control、`/desktop` 可视化 diff 复核、`claude --teleport`、在 Slack 中 `@Claude` 提 bug 拿回 PR。
- Next steps 指南：Quickstart、Store instructions and memories、Common workflows and best practices、Settings、Troubleshooting；产品细节见 `code.claude.com`。

## 术语与译法
- `Agent` → 智能体
- `Prompt` → 提示词
- `Model Context Protocol` → 模型上下文协议
- `MCP Server` → MCP 服务器
- `Tool Use` → 工具调用
- `Pull Request` → 拉取请求
- `Commit` → 提交
- `Code Review` → 代码评审
- `Permission` → 权限
- `Context Window` → 上下文窗口
- `Sandbox` → 沙箱

## 结论
Claude Code 以「一套引擎、多端入口」的形态融入日常开发，从安装、登录到写测试、提交 PR、CI 自动化均有覆盖。它的扩展性来自 `CLAUDE.md`、auto memory、custom commands、Hooks、MCP 与 `Agent SDK`，适合按团队工作流逐步定制。
