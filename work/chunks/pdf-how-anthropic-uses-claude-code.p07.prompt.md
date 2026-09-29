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

Claude Code for API
Team impact
Increased confidence in tackling unfamiliar areas
Team members can independently debug bugs and investigate incidents
in unfamiliar codebases.
Significant time savings in context gathering
Eliminated the overhead of copying code snippets and dragging files into
Claude.ai, reducing mental context-switching burden.
Faster rotation onboarding
Engineers rotating to new teams can quickly navigate unfamiliar
codebases and contribute meaningfully without extensive colleague
consultation.
Enhanced developer happiness
Team reports feeling happier and more productive with reduced friction
in daily workflows.
Top tips from the
API Knowledge team
Treat it as an iterative partner, not a one-shot solution
Rather than expecting Claude to solve problems immediately, approach
it as a collaborator you iterate with. This works better than trying to get
perfect solutions on the first try.
Use it for building confidence in unfamiliar areas
Don’t hesitate to tackle bugs or investigate incidents outside your
expertise - Claude Code makes it feasible to work independently in areas
that would normally require extensive context building.
Start with minimal information
Begin with just the bare minimum of what you need and let Claude guide
you through the process, rather than front-loading extensive explanations.
14
Claude Code for API
Claude Code for API
Team impact
Top tips from the
API Knowledge team
14
Increased confidence in tackling unfamiliar areas
Team members can independently debug bugs and investigate incidents
in unfamiliar codebases.
Significant time savings in context gathering
Eliminated the overhead of copying code snippets and dragging files into
Claude.ai, reducing mental context-switching burden.
Faster rotation onboarding
Engineers rotating to new teams can quickly navigate unfamiliar
code bases and contribute meaningfully without extensive colleague
consultation.
Enhanced developer happiness
Team reports feeling happier and more productive with reduced friction
in daily workflows.
Treat it as an iterative partner, not a one-shot solution
Rather than expecting Claude to solve problems immediately, approach
it as a collaborator you iterate with. This works better than trying to get
perfect solutions on the first try.
Use it for building confidence in unfamiliar areas
Don't hesitate to tackle bugs or investigate incidents outside your
expertise - Claude Code makes it feasible to work independently in areas
that would normally require extensive context building.
Start with minimal information
Begin with just the bare minimum of what you need and let Claude guide
you through the process, rather than front-loading extensive explanations.
CLAUDE CODE FOR API

Claude Code for growth
marketing
The Growth Marketing
team focuses on building out
performance marketing channels
across paid search, paid social,
mobile app stores, email
marketing, and SEO. As a non-
technical team of one, they use
Claude Code to automate
repetitive marketing tasks and
create agentic workflows that
would traditionally require
significant engineering
resources.
Main Claude Code use cases
Automated Google Ads creative generation
The team built an agentic workflow that processes CSV files containing
hundreds of existing ads with performance metrics, identifies
underperforming ads for iteration, and generates new variations that
meet strict character limits (30 characters for headlines, 90 for
descriptions). Using two specialized sub-agents (one for headlines, one
for descriptions), the system can generate hundreds of new ads in
minutes instead of requiring manual creation across multiple campaigns.
This has enabled them to test and iterate at scale, something that would
have taken a significant amount of time to achieve previously.
Figma plugin for mass creative production
Instead of manually duplicating and editing static images for paid
social ads, they developed a Figma plugin that identifies frames and
programmatically generates up to 100 ad variations by swapping
headlines and descriptions, reducing what would take hours of copy-
pasting to half a second per batch. This enables 10x creative output,
allowing the team to test vastly more creative variations across key
social channels.
Meta Ads MCP server for campaign analytics
They created an MCP server integrated with Meta Ads API to query
campaign performance, spending data, and ad effectiveness directly
within the Claude Desktop app, eliminating the need to switch between
platforms for performance analysis, saving critical time where every
efficiency gain translates to better ROI.
Advanced prompt engineering with memory systems
They implemented a rudimentary memory system that logs hypotheses
and experiments across ad iterations, allowing the system to pull previous
test results into context when generating new variations, creating a self-
improving testing framework. This enables systematic experimentation
that would be impossible to track manually.
15
Claude Code for growth marketing
Claude Code for growth
marketing
15
The Growth Marketing
team focuses on building out
performance marketing channels
across paid search, paid social,
mobile opp stores, email
marketing, and SEO. As a non-
technical team of one, they use
Claude Code to automate
repetitive marketing tasks and
create agentic workflows that
would traditionally
require
significant engineering
resources.
Main Claude Code use cases
Automated Google Ads creative generation
The team built an agentic workflow that processes CSV files containing
hundreds of existing ads with performance metrics, identifies
underperforming ads for iteration, and generates new variations that
meet strict character limits (30 characters for headlines, 90 for
descriptions). Using two specialized sub-agents (one for headlines, one
for descriptions), the system can generate hundreds of new ads in
minutes instead of requiring manual creation across multiple campaigns.
This has enabled them to test and iterate at scale, something that would
have taken a significant amount of time to achieve previously.
Figma plugin for mass creative production
Instead of manually duplicating and editing static images for paid
social ads, they developed a Figma plugin that identifies frames and
programmatically generates up to 100 ad variations by swapping
headlines and descriptions, reducing what would take hours of copy-
pasting to half a second per batch. This enables l0x creative output,
allowing the team to test vastly more creative variations across key
social channels.
Meta Ads MCP server for campaign analytics
They created an MCP server integrated with Meta Ads API to query
campaign performance, spending data, and ad effectiveness directly
within the Claude Desktop app, eliminating the need to switch between
platforms for performance analysis, saving critical time where every
efficiency gain translates to better ROI.
Advanced prompt engineering with memory systems
They implemented a rudimentary memory system that logs hypotheses
and experiments across ad iterations, allowing the system to pull previous
test results into context when generating new variations, creating a self-
improving testing framework. This enables systematic experimentation
that would be impossible to track manually.
CLAUDE CODE FOR GROWTH MARKETING