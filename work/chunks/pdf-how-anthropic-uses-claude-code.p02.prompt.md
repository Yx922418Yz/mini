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

Claude Code for data
infrastructure
Team impact
Resolved infrastructure problems without specialized expertise
Resolved Kubernetes cluster issues that would normally require pulling in
systems or networking team members, using Claude Code to diagnose
problems and provide exact fixes.
Accelerated onboarding
New data analysts and team members can quickly understand complex
systems and contribute meaningfully without extensive guidance.
Enhanced support workflow
Can process much larger data volumes and identify anomalies (like
monitoring 200 dashboards) that would be impossible for humans to
review manually.
Enabled cross-team self-service
Finance teams with no coding experience can now execute complex data
workflows independently.
Top tips from the
Data Infrastructure
team
Write detailed Claude.md files
The better you document your workflows, tools, and expectations in
Claude.md files, the better Claude Code performs. This made Claude Code
excel at routine tasks like setting up new data pipelines when you have
existing patterns.
Use MCP servers instead of CLI for sensitive data
They recommend using MCP servers rather than the BigQuery CLI to
maintain better security control over what Claude Code can access,
especially for handling sensitive data that requires logging or has
potential privacy concerns.
Share team usage sessions
The team held sessions where members demonstrated their Claude Code
workflows to each other. This helped spread best practices and showed
different ways to use the tool they might not have discovered on
their own.
4
Claude Code for data infrastructure
Claude Code for data
infrastructure
Team impact
Top tips from the
Data Infrastructure
team
4
Resolved infrastructure problems without specialized expertise
Resolved Kubernetes cluster issues that would normally require pulling in
systems or networking team members, using Claude Code to diagnose
problems and provide exact fixes.
Accelerated onboarding
New data analysts and team members can quickly understand complex
systems and contribute meaningfully without extensive guidance.
Enhanced support workflow
Can process much larger data volumes and identify anomalies (like
monitoring 200 dashboards) that would be impossible for humans to
review manually.
Enabled cross-team self-service
Finance teams with no coding experience can now execute complex data
workflows independently.
Write detailed Claude.md files
The better you document your workflows, tools, and expectations in
Claude.md files, the better Claude Code performs. This made Claude Code
excel at routine tasks like setting up new data pipelines when you have
existing patterns.
Use MCP servers instead of CLI for sensitive data
They recommend using MCP servers rather than the BigQuery CLI to
maintain better security control over what Claude Code can access,
especially for handling sensitive data that requires logging or has
potential privacy concerns.
Share team usage sessions
The team held sessions where members demonstrated their Claude Code
workflows to each other. This helped spread best practices and showed
different ways to use the tool they might not have discovered on
their own.
CLAUDE CODE FOR DATA INFRASTRUCTURE

Claude Code for product
development
The Claude Code team uses their
own product to build updates to
Claude Code, expanding the
product’s enterprise capabilities
and agentic loop functionalities.
Main Claude Code use cases
Fast prototyping with auto-accept mode
Engineers use Claude Code for rapid prototyping by enabling “auto-
accept mode” (shift+tab) and setting up autonomous loops where Claude
writes code, runs tests, and iterates continuously. They give Claude
abstract problems they’re unfamiliar with, let it work autonomously, then
review the 80% complete solution before taking over for final refinements.
Teams emphasize starting from a clean git state and committing
checkpoints regularly so they can easily revert any incorrect changes
if Claude goes off track.
Synchronous coding for core features
For more critical features touching the application’s business logic, the
team works synchronously with Claude Code, giving detailed prompts
with specific implementation instructions. They monitor the process in
real-time to ensure code quality, style guide compliance, and proper
architecture while letting Claude handle the repetitive coding work.
Building Vim mode
One of their most successful async projects was implementing Vim
key bindings for Claude Code. They asked Claude to build the entire
feature (despite it not being a priority), and roughly 70% of the final
implementation came from Claude’s autonomous work, requiring
only a few iterations to complete.
Test generation and bug fixes
They use Claude Code to write comprehensive tests after implementing
features and handle simple bug fixes identified in pull request reviews.
They also leverage GitHub Actions integration to have Claude
automatically address Pull Request comments like formatting issues
or function renaming.
Codebase exploration
When working with unfamiliar codebases (like the monorepo or API
side), the team uses Claude Code to quickly understand how systems
work. Instead of waiting for Slack responses, they ask Claude directly
for explanations and code references, saving significant time in
context switching.
5
Claude Code for product development
Claude Code for product
development
5
The Claude Code team uses their
own product to build updates to
Claude Code, expanding the
product's enterprise capabilities
and agentic loop functionalities.
Main Claude Code use cases
Fast prototyping with auto-accept mode
Engineers use Claude Code for rapid prototyping by enabling "auto-
accept mode" (shift+tab) and setting up autonomous loops where Claude
writes code, runs tests, and iterates continuously. They give Claude
abstract problems they're unfamiliar with, let it work autonomously, then
review the 80% complete solution before taking over for final refinements.
Teams emphasize starting from a clean git state and committing
checkpoints regularly so they can easily revert any incorrect changes
if Claude goes off track.
Synchronous coding for core features
For more critical features touching the application's business logic, the
team works synchronously with Claude Code, giving detailed prompts
with specific implementation instructions. They monitor the process in
real-time to ensure code quality, style guide compliance, and proper
architecture while letting Claude handle the repetitive coding work.
Building Vim mode
One of their most successful async projects was implementing Vim
key bindings for Claude Code. They asked Claude to build the entire
feature (despite it not being a priority), and roughly 70% of the final
implementation came from Claude's autonomous work, requiring
only a few iterations to complete.
Test generation and bug fixes
They use Claude Code to write comprehensive tests after implementing
features and handle simple bug fixes identified in pull request reviews.
They also leverage GitHub Actions integration to have Claude
automatically address Pull Request comments like formatting issues
or function renaming.
Codebase exploration
When working with unfamiliar codebases (like the monorepo or API
side), the team uses Claude Code to quickly understand how systems
work. Instead of waiting for Slack responses, they ask Claude directly
for explanations and code references, saving significant time in
context switching.
CLAUDE CODE FOR PRODUCT DEVELOPMENT