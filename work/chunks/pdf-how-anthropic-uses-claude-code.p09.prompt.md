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

Claude Code for product design
Team impact
Transformed core workflow
Claude Code becomes a primary design tool, with Figma and Claude Code
open 80% of the time.
2-3x faster execution
Visual and state management changes that previously required extensive
back-and-forth with engineers now implemented directly.
Weeks to hours cycle time
Complex projects like GA launch messaging that would take a week of
coordination now completed in two 30-minute calls.
Two distinct user experiences
Developers get “augmented workflow” (faster execution), while non-
technical users get “holy crap, I’m a developer workflow” (entirely new
capabilities previously impossible).
Improved design-engineering collaboration
Better communication and faster problem-solving because designers
understand system constraints and possibilities upfront.
Top tips from the
Product Design team
Get proper setup help from engineers
Have engineering teammates help with initial repository setup and
permissions - the technical onboarding is challenging for non-developers,
but once configured, it becomes transformative for daily workflow.
Use custom memory files to guide Claude’s behavior
Create specific instructions telling Claude you’re a designer with little
coding experience who needs detailed explanations and smaller,
incremental changes, dramatically improving the quality of Claude’s
responses and making it less intimidating.
Leverage image pasting for prototyping
Use Command+V to paste screenshots directly into Claude Code - it excels
at reading designs and generating functional code, making it invaluable
for turning static mockups into interactive prototypes that engineers can
immediately understand and build upon.
18
Claude Code for product design
Claude Code for product design
Team impact
Top tips from the
Product Design team
18
Transformed core workflow
Claude Code becomes a primary design tool, with Figma and Claude Code
open 80% of the time.
2-3x faster execution
Visual and state management changes that previously required extensive
back-and-forth with engineers now implemented directly.
Weeks to hours cycle time
Complex projects like GA launch messaging that would take a week of
coordination now completed in two 30-minute calls.
Two distinct user experiences
Developers get "augmented workflow" (faster execution), while non-
technical users get "holy crap, I'm a developer workflow" ( entirely new
capabilities previously impossible).
Improved design-engineering collaboration
Better communication and faster problem-solving because designers
understand system constraints and possibilities upfront.
Get proper setup help from engineers
Have engineering teammates help with initial repository setup and
permissions - the technical onboarding is challenging for non-developers,
but once configured, it becomes transformative for daily workflow.
Use custom memory files to guide Claude's behavior
Create specific instructions telling Claude you're a designer with little
coding experience who needs detailed explanations and smaller,
incremental changes, dramatically improving the quality of Claude's
responses and making it less intimidating.
Leverage image pasting for prototyping
Use Command+V to paste screenshots directly into Claude Code - it excels
at reading designs and generating functional code, making it invaluable
for turning static mockups into interactive prototypes that engineers can
immediately understand and build upon.
CLAUDE CODE FOR PRODUCT DESIGN

Claude Code for RL engineering
The RL Engineering team
focuses on efficient sampling in
RL and weight transfers across
the cluster. They use Claude
Code primarily for writing small
to medium features, debugging,
and understanding complex
codebases, with an iterative
approach that includes frequent
checkpointing and rollbacks.
Main Claude Code use cases
Feature development with supervised autonomy
The team lets Claude Code write most of the code for small to medium
features while providing oversight, such as implementing authentication
mechanisms for weight transfer components. They work interactively,
allowing Claude to take the lead but steering it when it goes off track.
Test generation and code review
After implementing changes themselves, they ask Claude Code to add
tests or review their code. This automated testing workflow saves
significant time on routine but important quality assurance tasks.
Debugging and error investigation
They use Claude Code to debug errors with mixed results - sometimes it
identifies issues immediately and adds relevant tests, while other times
it struggles to understand the problem, but overall provides value when
it works.
Codebase comprehension and call stack analysis
One of the biggest changes in their workflow is using Claude Code to get
quick summaries of relevant components and call stacks, replacing
manual code reading or extensive debugging output generation.
Kubernetes operations guidance
They frequently ask Claude Code about Kubernetes operations that would
otherwise require extensive Googling, getting immediate answers for
configuration and deployment questions.
19
Claude Code for RL engineering
Claude Code for RL engineering
19
The RL Engineering team
focuses on efficient sampling in
RL and weight transfers across
the cluster. They use Claude
Code primarily for writing small
to medium features, debugging,
and understanding complex
codebases, with an iterative
approach that includes frequent
checkpointing and rollbacks.
Main Claude Code use cases
Feature development with supervised autonomy
The team lets Claude Code write most of the code for small to medium
features while providing oversight, such as implementing authentication
mechanisms for weight transfer components. They work interactively,
allowing Claude to take the lead but steering it when it goes off track.
Test generation and code review
After implementing changes themselves, they ask Claude Code to add
tests or review their code. This automated testing workflow saves
significant time on routine but important quality assurance tasks.
Debugging and error investigation
They use Claude Code to debug errors with mixed results - sometimes it
identifies issues immediately and adds relevant tests, while other times
it struggles to understand the problem, but overall provides value when
it works.
Codebase comprehension and call stack analysis
One of the biggest changes in their workflow is using Claude Code to get
quick summaries of relevant components and call stacks, replacing
manual code reading or extensive debugging output generation.
Kubernetes operations guidance
They frequently ask Claude Code about Kubemetes operations that would
otherwise require extensive Googling, getting immediate answers for
configuration and deployment questions.
CLAUDE CODE FOR RL ENGINEERING