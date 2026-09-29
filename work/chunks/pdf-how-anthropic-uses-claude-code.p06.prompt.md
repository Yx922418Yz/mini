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

Claude Code for data science
and visualization
Team impact
Achieved 2-4x time savings
Routine refactoring tasks that were tedious but manageable manually
are now completed much faster.
Built complex applications in unfamiliar languages
Created 5,000-line TypeScript applications despite having minimal
JavaScript/TypeScript experience.
Shifted from throwaway to persistent tools
Instead of disposable Jupyter notebooks, now building reusable React
dashboards for model analysis.
Direct model improvement insights
Firsthand Claude Code experience informs development of better
memory systems and UX improvements for future model iterations.
Enabled visualization-driven decision making
Better understanding of Claude’s performance during training and
evaluations through advanced data visualization tools.
Top tips from the
Data Science and
ML Engineering teams
Treat it like a slot machine
Save your state before letting Claude work, let it run for 30 minutes,
then either accept the result or start fresh rather than trying to wrestle
with corrections. Starting over often has a higher success rate than trying
to fix Claude’s mistakes.
Interrupt for simplicity when needed
While supervising, don’t hesitate to stop Claude and ask “why are
you doing this? Try something simpler.” The model tends toward
more complex solutions by default but responds well to requests for
simpler approaches.
12
Claude Code for data science and visualization
Claude Code for data science
and visualization
Team impact
Top tips from the
Data Science and
ML Engineering teams
12
Achieved 2-4x time savings
Routine refactoring tasks that were tedious but manageable manually
are now completed much faster.
Built complex applications in unfamiliar languages
Created 5,000-line Typescript applications despite having minimal
JavaScript/Typescript experience.
Shifted from throwaway to persistent tools
Instead of disposable Jupyter notebooks, now building reusable React
dashboards for model analysis.
Direct model improvement insights
Firsthand Claude Code experience informs development of better
memory systems and UX improvements for future model iterations.
Enabled visualization-driven decision making
Better understanding of Claude's performance during training and
evaluations through advanced data visualization tools.
Treat it like a slot machine
Save your state before letting Claude work, let it run for 30 minutes,
then either accept the result or start fresh rather than trying to wrestle
with corrections. Starting over often has a higher success rate than trying
to fix Claude's mistakes.
Interrupt for simplicity when needed
While supervising, don't hesitate to stop Claude and ask "why are
you doing this? Try something simpler." The model tends toward
more complex solutions by default but responds well to requests for
simpler approaches.
CLAUDE CODE FOR DATA SCIENCE AND VISUALIZATION

Claude Code for API
The API Knowledge team works
on features like PDF support,
citations, and web search that
bring additional knowledge into
Claude’s context window.
Working across large, complex
codebases means constantly
encountering unfamiliar code
sections, spending significant
time understanding which files to
examine for any given task, and
building context before making
changes. Claude Code improves
this experience by serving as a
guide that can help them
understand system architecture,
identify relevant files, and
explain complex interactions.
Main Claude Code use cases
First-step workflow planning
The team uses Claude Code as their “first stop” for any task, asking it
to identify which files to examine for bug fixes, feature development,
or analysis. This replaces the traditional time-consuming process of
manually navigating the codebase and gathering context before
starting work.
Independent debugging across codebases
The team now has the confidence to tackle bugs in unfamiliar parts of the
codebase instead of asking others for help. They can ask Claude “Do you
think you can fix this bug? This is the behavior I’m seeing” and often get
immediate progress, which wasn’t feasible before given the time
investment required.
Model iteration testing through dogfooding
Claude Code automatically uses the latest research model snapshots,
making it their primary way of experiencing model changes. This gives
them direct feedback on model behavior changes during development
cycles, which they hadn’t experienced during previous launches.
Eliminating context-switching overhead
Instead of copying code snippets and dragging files into Claude.ai
while explaining problems extensively, they can ask questions directly in
Claude Code without additional context gathering, significantly reducing
mental overhead.
13
Claude Code for API
Claude Code for API
13
The API Knowledge team works
on features like PDF support,
citations, and web search that
bring additional knowledge into
Claude's context window.
Working across large, complex
codebases means constantly
encountering unfamiliar code
sections, spending significant
time understanding which files to
examine for any given task, and
building context before making
changes. Claude Code improves
this experience by serving as a
guide that can help them
understand system architecture,
identify relevant files, and
explain complex interactions.
Main Claude Code use cases
First-step workflow planning
The team uses Claude Code as their "first stop" for any task, asking it
to identify which files to examine for bug fixes, feature development,
or analysis. This replaces the traditional time-consuming process of
manually navigating the codebase and gathering context before
starting work.
Independent debugging across codebases
The team now has the confidence to tackle bugs in unfamiliar parts of the
code base instead of asking others for help. They can ask Claude "Do you
think you can fix this bug? This is the behavior I'm seeing" and often get
immediate progress, which wasn't feasible before given the time
investment required.
Model iteration testing through dogfooding
Claude Code automatically uses the latest research model snapshots,
making it their primary way of experiencing model changes. This gives
them direct feedback on model behavior changes during development
cycles, which they hadn't experienced during previous launches.
Eliminating context-switching overhead
Instead of copying code snippets and dragging files into Claude.ai
while explaining problems extensively, they can ask questions directly in
Claude Code without additional context gathering, significantly reducing
mental overhead.
CLAUDE CODE FOR API