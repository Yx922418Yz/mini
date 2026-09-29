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

Claude Code for product
development
Team impact
Faster feature implementation
Successfully implemented complex features like Vim mode with 70% of
code written autonomously by Claude.
Improved development velocity
Can rapidly prototype features and iterate on ideas without getting
bogged down in implementation details.
Enhanced code quality through automated testing
Claude generates comprehensive tests and handles routine bug fixes,
maintaining high standards while reducing manual effort.
Better codebase exploration
Team members can quickly understand unfamiliar parts of the monorepo
without waiting for colleague responses.
Top tips from the
Claude Code team
Create self-sufficient loops
Set up Claude to verify its own work by running builds, tests, and lints
automatically. This allows Claude to work longer autonomously and catch
its own mistakes, especially effective when you ask Claude to generate
tests before writing code.
Develop task classification intuition
Learn to distinguish between tasks that work well asynchronously
(peripheral features, prototyping) versus those needing synchronous
supervision (core business logic, critical fixes). Abstract tasks on the
product’s edges can be handled with “auto-accept mode,” while core
functionality requires closer oversight.
Form clear, detailed prompts
When components have similar names or functions, be extremely specific
in your requests. The better and more detailed your prompt, the more you
can trust Claude to work independently without unexpected changes to
the wrong parts of the codebase.
6
Claude Code for product development
Claude Code for product
development
Team impact
Top tips from the
Claude Code team
6
Faster feature implementation
Successfully implemented complex features like Vim mode with 70% of
code written autonomously by Claude.
Improved development velocity
Can rapidly prototype features and iterate on ideas without getting
bogged down in implementation details.
Enhanced code quality through automated testing
Claude generates comprehensive tests and handles routine bug fixes,
maintaining high standards while reducing manual effort.
Better codebase exploration
Team members can quickly understand unfamiliar parts of the monorepo
without waiting for colleague responses.
Create self-sufficient loops
Set up Claude to verify its own work by running builds, tests, and lints
automatically. This allows Claude to work longer autonomously and catch
its own mistakes, especially effective when you ask Claude to generate
tests before writing code.
Develop task classification intuition
Learn to distinguish between tasks that work well asynchronously
(peripheral features, prototyping) versus those needing synchronous
supervision (core business logic, critical fixes). Abstract tasks on the
product's edges can be handled with "auto-accept mode," while core
functionality requires closer oversight.
Form clear, detailed prompts
When components have similar names or functions, be extremely specific
in your requests. The better and more detailed your prompt, the more you
can trust Claude to work independently without unexpected changes to
the wrong parts of the code base.
CLAUDE CODE FOR PRODUCT DEVELOPMENT

Claude Code for security
engineering
The Security Engineering team
focuses on securing the software
development lifecycle, supply
chain security, and development
environment security. They use
Claude Code extensively for
writing and debugging code.
Main Claude Code use cases
Complex infrastructure debugging
When working on incidents, they feed Claude Code stack traces and
documentation, asking it to trace control flow through the codebase. This
significantly reduces time-to-resolution for production issues, allowing
them to understand problems that would normally take 10-15 minutes of
manual code scanning in about 5 minutes.
Terraform code review and analysis
For infrastructure changes requiring security approval, they copy
Terraform plans into Claude Code to ask “what’s this going to do? Am I
going to regret this?” This creates tighter feedback loops and makes it
easier for the security team to quickly review and approve infrastructure
changes, reducing bottlenecks in the development process.
Documentation synthesis and runbooks
They have Claude Code ingest multiple documentation sources and
create markdown runbooks, troubleshooting guides, and overviews.
They use these condensed documents as context for debugging real
issues, creating a more efficient workflow than searching through full
knowledge bases.
Test-driven development workflow
Instead of their previous “design doc → janky code → refactor → give up
on tests” pattern, they now ask Claude Code for pseudocode, guide it
through test-driven development, and periodically check in to steer it
when stuck, resulting in more reliable and testable code.
Context switching and project onboarding
When contributing to existing projects like “dependant” (a web
application for security approval workflows), they use Claude Code
to write, review, and execute specifications written in markdown and
stored in the codebase, enabling meaningful contributions within days
instead of weeks.
7
Claude Code for security engineering
Claude Code for security
■
■
eng1neer1ng
7
The Security Engineering team
focuses on securing the software
development lifecycle, supply
chain security, and development
environment security. They use
Claude Code extensively for
writing and debugging code.
Main Claude Code use cases
Complex infrastructure debugging
When working on incidents, they feed Claude Code stack traces and
documentation, asking it to trace control flow through the code base. This
significantly reduces time-to-resolution for production issues, allowing
them to understand problems that would normally take 10-15 minutes of
manual code scanning in about 5 minutes.
Terraform code review and analysis
For infrastructure changes requiring security approval, they copy
Terraform plans into Claude Code to ask "what's this going to do? Am I
going to regret this?" This creates tighter feedback loops and makes it
easier for the security team to quickly review and approve infrastructure
changes, reducing bottlenecks in the development process.
Documentation synthesis and runbooks
They have Claude Code ingest multiple documentation sources and
create markdown run books, troubleshooting guides, and overviews.
They use these condensed documents as context for debugging real
issues, creating a more efficient workflow than searching through full
knowledge bases.
Test-driven development workflow
Instead of their previous "design doc - janky code - refactor - give up
on tests" pattern, they now ask Claude Code for pseudocode, guide it
through test-driven development, and periodically check in to steer it
when stuck, resulting in more reliable and testable code.
Context switching and project onboarding
When contributing to existing projects like "dependant" (a web
application for security approval workflows), they use Claude Code
to write, review, and execute specifications written in markdown and
stored in the codebase, enabling meaningful contributions within days
instead of weeks.
CLAUDE CODE FOR SECURITY ENGINEERING