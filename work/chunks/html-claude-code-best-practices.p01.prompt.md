你是资深技术译者，正在翻译斯坦福 CS146S《The Modern Software Developer》课程材料。
把下面的英文原文翻译成简体中文。要求：
1. 忠实、通顺，术语前后一致；保留原文的 Markdown 结构（标题/列表/表格/代码块）。
2. 代码、命令行、文件名、API/产品名、URL 一律保持原文，不要翻译。
3. 严格使用下方术语表给出的译法；术语表未覆盖的专业词，首次出现时写成「中文（English）」。
4. 只输出译文本身，不要输出任何说明、致谢或前后缀。

术语表（英文 = 中文）：
- Vibe Coding = 氛围编程
- Scaffolding = 脚手架
- Context Engineering = 上下文工程
- Context Rot = 上下文腐化
- Agent = 智能体
- Agentic AI = 智能体式 AI
- Coding Agent = 编码智能体
- LLM = 大语言模型
- Prompt = 提示词
- Prompt Engineering = 提示工程
- System Prompt = 系统提示词
- Token = 词元
- Context Window = 上下文窗口
- Long-context = 长上下文
- Hallucination = 幻觉
- Code Review = 代码评审
- Pull Request = 拉取请求
- Commit = 提交
- Repository = 仓库
- Monorepo = 单体仓库
- Refactor = 重构
- Linter = 静态检查器
- Static Analysis = 静态分析
- SAST = 静态应用安全测试（SAST）
- DAST = 动态应用安全测试（DAST）
- Vulnerability = 漏洞
- Injection = 注入
- Prompt Injection = 提示注入
- Remote Code Execution = 远程代码执行
- Supply Chain Attack = 供应链攻击
- OWASP Top Ten = OWASP 十大安全风险
- Model Context Protocol = 模型上下文协议
- MCP Server = MCP 服务器
- Tool Use = 工具调用
- Tool Definition = 工具定义
- Observability = 可观测性
- Telemetry = 遥测
- Distributed Tracing = 分布式链路追踪
- On-call = 值班
- Incident = 事故
- Site Reliability Engineering = 站点可靠性工程
- Service Level Agreement = 服务等级协议
- Multi-agent System = 多智能体系统
- Orchestration = 编排
- Sandbox = 沙箱
- Permission = 权限
- Approval Flow = 审批流
- Spec = 规格说明
- Spec-driven Development = 规格驱动开发
- Unit Test = 单元测试
- Continuous Integration = 持续集成
- Troubleshooting = 排障
- Retrieval-Augmented Generation = 检索增强生成
- Embedding = 嵌入向量
- Vector Database = 向量数据库
- Benchmark = 基准测试
- Evaluation = 评估
- Guardrail = 护栏
- Human-in-the-loop = 人在回路
- Autonomy = 自主性
- Latency = 延迟
- Throughput = 吞吐量
- Regression = 回归
- Pair Programming = 结对编程
- Technical Debt = 技术债
- Deterministic = 确定性的
- Rubber Duck Debugging = 小黄鸭调试法


--- 待翻译原文 ---

Claude Code overview - Claude Code Docs
Skip to main content
Claude Code Docs home page
Getting started
Build with Claude Code
Deployment
Administration
Configuration
Reference
Resources
Getting started
Overview
Quickstart
Changelog
Core concepts
How Claude Code works
Extend Claude Code
Explore the .claude directory
Explore the context window
Use Claude Code
Store instructions and memories
Permission modes
Common workflows
Best practices
Platforms and integrations
Overview
Remote Control
Chrome extension (beta)
Computer use (preview)
Visual Studio Code
JetBrains IDEs
Claude Code in Slack
Get started
What you can do
Use Claude Code everywhere
Next steps
Claude Code is an AI-powered coding assistant that helps you build features, fix bugs, and automate development tasks.

It understands your entire codebase and can work across multiple files and tools to get things done.

​
Get started
Choose your environment to get started.

Most surfaces require a Claude subscription or Anthropic Console account.

The Terminal CLI and VS Code also support third-party providers.

Terminal
VS Code
Desktop app
Web
JetBrains
The full-featured CLI for working with Claude Code directly in your terminal.

Edit files, run commands, and manage your entire project from the command line.To install Claude Code, use one of the following methods: Native Install (Recommended)
Homebrew
WinGet
macOS, Linux, WSL:
curl -fsSL https://claude.ai/install.sh | bash
Windows PowerShell:
irm https://claude.ai/install.ps1 | iex
Windows CMD:
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
If you see The token '&&' is not a valid statement separator, you’re in PowerShell, not CMD.

Use the PowerShell command above instead.

Your prompt shows PS C:\ when you’re in PowerShell.Windows requires Git for Windows.

Install it first if you don’t have it.

Native installations automatically update in the background to keep you on the latest version.

brew install --cask claude-code
Homebrew installations do not auto-update.

Run brew upgrade claude-code periodically to get the latest features and security fixes.

winget install Anthropic.ClaudeCode
WinGet installations do not auto-update.

Run winget upgrade Anthropic.ClaudeCode periodically to get the latest features and security fixes.

Then start Claude Code in any project:
cd your-project
claude
You’ll be prompted to log in on first use.

That’s it!

Continue with the Quickstart →
See advanced setup for installation options, manual updates, or uninstallation instructions.

Visit troubleshooting if you hit issues.

The VS Code extension provides inline diffs, @-mentions, plan review, and conversation history directly in your editor.

Install for VS Code
Install for Cursor
Or search for “Claude Code” in the Extensions view (Cmd+Shift+X on Mac, Ctrl+Shift+X on Windows/Linux).

After installing, open the Command Palette (Cmd+Shift+P / Ctrl+Shift+P), type “Claude Code”, and select Open in New Tab.Get started with VS Code →
A standalone app for running Claude Code outside your IDE or terminal.

Review diffs visually, run multiple sessions side by side, schedule recurring tasks, and kick off cloud sessions.Download and install:
macOS (Intel and Apple Silicon)
Windows (x64)
Windows ARM64 (remote sessions only)
After installing, launch Claude, sign in, and click the Code tab to start coding.

A paid subscription is required.Learn more about the desktop app →
Run Claude Code in your browser with no local setup.

Kick off long-running tasks and check back when they’re done, work on repos you don’t have locally, or run multiple tasks in parallel.

Available on desktop browsers and the Claude iOS app.Start coding at claude.ai/code.Get started on the web →
A plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs with interactive diff viewing and selection context sharing.Install the Claude Code plugin from the JetBrains Marketplace and restart your IDE.Get started with JetBrains →
​
What you can do
Here are some of the ways you can use Claude Code:
Automate the work you keep putting off
Claude Code handles the tedious tasks that eat up your day: writing tests for untested code, fixing lint errors across a project, resolving merge conflicts, updating dependencies, and writing release notes.

claude "write tests for the auth module, run them, and fix any failures"
Build features and fix bugs
Describe what you want in plain language.

Claude Code plans the approach, writes the code across multiple files, and verifies it works.For bugs, paste an error message or describe the symptom.

Claude Code traces the issue through your codebase, identifies the root cause, and implements a fix.

See common workflows for more examples.

Create commits and pull requests
Claude Code works directly with git.

It stages changes, writes commit messages, creates branches, and opens pull requests.

claude "commit my changes with a descriptive message"
In CI, you can automate code review and issue triage with GitHub Actions or GitLab CI/CD.

Connect your tools with MCP
The Model Context Protocol (MCP) is an open standard for connecting AI tools to external data sources.

With MCP, Claude Code can read your design docs in Google Drive, update tickets in Jira, pull data from Slack, or use your own custom tooling.

Customize with instructions, skills, and hooks
CLAUDE.md is a markdown file you add to your project root that Claude Code reads at the start of every session.

Use it to set coding standards, architecture decisions, preferred libraries, and review checklists.

Claude also builds auto memory as it works, saving learnings like build commands and debugging insights across sessions without you writing anything.Create custom commands to package repeatable workflows your team can share, like /review-pr or /deploy-staging.Hooks let you run shell commands before or after Claude Code actions, like auto-formatting after every file edit or running lint before a commit.

Run agent teams and build custom agents
Spawn multiple Claude Code agents that work on different parts of a task simultaneously.

A lead agent coordinates the work, assigns subtasks, and merges results.For fully custom workflows, the Agent SDK lets you build your own agents powered by Claude Code’s tools and capabilities, with full control over orchestration, tool access, and permissions.

Pipe, script, and automate with the CLI
Claude Code is composable and follows the Unix philosophy.

Pipe logs into it, run it in CI, or chain it with other tools:
# Analyze recent log output
tail -200 app.log | claude -p "Slack me if you see any anomalies"
# Automate translations in CI
claude -p "translate new strings into French and raise a PR for review"
# Bulk operations across files
git diff main --name-only | claude -p "review these changed files for security issues"
See the CLI reference for the full set of commands and flags.

Schedule recurring tasks
Run Claude on a schedule to automate work that repeats: morning PR reviews, overnight CI failure analysis, weekly dependency audits, or syncing docs after PRs merge.

Cloud scheduled tasks run on Anthropic-managed infrastructure, so they keep running even when your computer is off.

Create them from the web, the Desktop app, or by running /schedule in the CLI.

Desktop scheduled tasks run on your machine, with direct access to your local files and tools
/loop repeats a prompt within a CLI session for quick polling
Work from anywhere
Sessions aren’t tied to a single surface.

Move work between environments as your context changes:
Step away from your desk and keep working from your phone or any browser with Remote Control
Message Dispatch a task from your phone and open the Desktop session it creates
Kick off a long-running task on the web or iOS app, then pull it into your terminal with claude --teleport
Hand off a terminal session to the Desktop app with /desktop for visual diff review
Route tasks from team chat: mention @Claude in Slack with a bug report and get a pull request back
​
Use Claude Code everywhere
Each surface connects to the same underlying Claude Code engine, so your CLAUDE.md files, settings, and MCP servers work across all of them.

Beyond the Terminal, VS Code, JetBrains, Desktop, and Web environments above, Claude Code integrates with CI/CD, chat, and browser workflows:
I want to…Best option
Continue a local session from my phone or another deviceRemote Control
Push events from Telegram, Discord, iMessage, or my own webhooks into a sessionChannels
Start a task locally, continue on mobileWeb or Claude iOS app
Run Claude on a recurring scheduleCloud scheduled tasks or Desktop scheduled tasks
Automate PR reviews and issue triageGitHub Actions or GitLab CI/CD
Get automatic code review on every PRGitHub Code Review
Route bug reports from Slack to pull requestsSlack
Debug live web applicationsChrome
Build custom agents for your own workflowsAgent SDK
​
Next steps
Once you’ve installed Claude Code, these guides help you go deeper.