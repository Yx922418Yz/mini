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

Claude Code for inference
Team impact
Accelerated ML concept learning
Research time reduced by 80% - what took an hour of Google searching
now takes 10-20 minutes.
Faster codebase navigation
Can find relevant files and understand system architecture in seconds
instead of asking colleagues.
Comprehensive test coverage
Claude automatically generates unit tests with edge cases, relieving
mental burden while maintaining code quality.
Language barrier elimination
Can implement functionality in unfamiliar languages like Rust without
needing to learn it.
Top tips from the
Inference team
Test knowledge base functionality first
Try asking various questions to see if Claude can answer faster than
Google search. If it’s faster and more accurate, it’s a valuable time-saving
tool for your workflow.
Start with code generation
Give Claude specific instructions and ask it to write logic, then verify
correctness. This helps build trust in the tool’s capabilities before using it
for more complex tasks.
Use it for test writing
Having Claude write unit tests relieves significant pressure from daily
development work. Leverage this feature to maintain code quality without
spending time thinking through all test cases manually.
10
Claude Code for inference
Claude Code for inference
Team impact
Top tips from the
Inference team
10
Accelerated ML concept learning
Research time reduced by 80% - what took an hour of Google searching
now takes 10-20 minutes.
Faster codebase navigation
Can find relevant files and understand system architecture in seconds
instead of asking colleagues.
Comprehensive test coverage
Claude automatically generates unit tests with edge cases, relieving
mental burden while maintaining code quality.
Language barrier elimination
Can implement functionality in unfamiliar languages like Rust without
needing to learn it.
Test knowledge base functionality first
Try asking various questions to see if Claude can answer faster than
Google search. If it's faster and more accurate, it's a valuable time-saving
tool for your workflow.
Start with code generation
Give Claude specific instructions and ask it to write logic, then verify
correctness. This helps build trust in the tool's capabilities before using it
for more complex tasks.
Use it for test writing
Having Claude write unit tests relieves significant pressure from daily
development work. Leverage this feature to maintain code quality without
spending time thinking through all test cases manually.
CLAUDE CODE FOR INFERENCE

Claude Code for data science
and visualization
Data Science and ML
Engineering teams need
sophisticated visualization
tools to understand model
performance, but building these
tools often requires expertise
in unfamiliar languages and
frameworks. Claude Code
enables these teams to build
production-quality analytics
dashboards without becoming
full-stack developers.
Main Claude Code use cases
Building JavaScript/TypeScript dashboard apps
Despite knowing “very little JavaScript and TypeScript,” the team uses
Claude Code to build entire React applications for visualizing RL model
performance and training data. They give Claude control to write full
applications from scratch, like a 5,000-line TypeScript app, without
needing to understand the code themselves. This is critical because
visualization apps are relatively low context and don’t require
understanding the entire monorepo, allowing rapid prototyping of tools
to understand model performance during training and evaluations.
Handling repetitive refactoring tasks
When faced with merge conflicts or semi-complicated file refactoring
that’s too complex for editor macros but not large enough for major
development effort, they use Claude Code like a “slot machine” - commit
their state, let Claude work autonomously for 30 minutes, and either
accept the solution or restart fresh if it doesn’t work.
Creating persistent analytics tools instead of throwaway notebooks
Instead of building one-off Jupyter notebooks that get discarded, the
team now has Claude build permanent React dashboards that can be
reused across future model evaluations. This is important because
understanding Claude’s performance is “one of the most important things
for the team” - they need to understand how models perform during
training and evaluations, which “is actually non-trivial and simple tools
can’t get too much signal from looking at a single number go up.”
Zero-dependency task delegation
For tasks in completely unfamiliar codebases or languages, they delegate
entire implementation to Claude Code, leveraging its ability to gather
context from the monorepo and execute tasks without their involvement
in the actual coding process. This allows productivity in areas outside
their expertise instead of spending time learning new technologies.
11
Claude Code for data science and visualization
Claude Code for data science
and visualization
11
Data Science and ML
Engineering teams need
sophisticated visualization
tools to understand model
performance, but building these
tools often requires expertise
in unfamiliar languages and
frameworks. Claude Code
enables these teams to build
production-quality
analytics
dashboards without becoming
full-stack developers.
Main Claude Code use cases
Building JavaScript/Typescript dashboard apps
Despite knowing "very little JavaScript and Typescript," the team uses
Claude Code to build entire React applications for visualizing RL model
performance and training data. They give Claude control to write full
applications from scratch, like a 5,000-line Typescript app, without
needing to understand the code themselves. This is critical because
visualization apps are relatively low context and don't require
understanding the entire monorepo, allowing rapid prototyping of tools
to understand model performance during training and evaluations.
Handling repetitive refactoring tasks
When faced with merge conflicts or semi-complicated file refactoring
that's too complex for editor macros but not large enough for major
development effort, they use Claude Code like a "slot machine" - commit
their state, let Claude work autonomously for 30 minutes, and either
accept the solution or restart fresh if it doesn't work.
Creating persistent analytics tools instead of throwaway notebooks
Instead of building one-off Jupyter notebooks that get discarded, the
team now has Claude build permanent React dashboards that can be
reused across future model evaluations. This is important because
understanding Claude's performance is "one of the most important things
for the team" - they need to understand how models perform during
training and evaluations, which "is actually non-trivial and simple tools
can't get too much signal from looking at a single number go up."
Zero-dependency task delegation
For tasks in completely unfamiliar codebases or languages, they delegate
entire implementation to Claude Code, leveraging its ability to gather
context from the monorepo and execute tasks without their involvement
in the actual coding process. This allows productivity in areas outside
their expertise instead of spending time learning new technologies.
CLAUDE CODE FOR DATA SCIENCE AND VISUALIZATION