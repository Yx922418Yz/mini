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

Claude Code for security
engineering
Team impact
Reduced incident resolution time
Infrastructure debugging that normally takes 10-15 minutes of manual
code scanning now takes about 5 minutes.
Improved security review cycle
Terraform code reviews for security approval happen much faster,
eliminating developer blocks while waiting for security team approval.
Enhanced cross-functional contribution
Team members can meaningfully contribute to projects within days
instead of weeks of context building.
Better documentation workflow
Synthesized troubleshooting guides and runbooks from multiple sources
create more efficient debugging processes.
Top tips from the
Security Engineering
team
Use custom slash commands extensively
Security engineering uses 50% of all custom slash command
implementations in the entire monorepo. These custom commands
streamline specific workflows and speed up repeated tasks.
Let Claude talk first
Instead of asking targeted questions for code snippets, they now
tell Claude Code to “commit your work as you go” and let it work
autonomously with periodic check-ins, resulting in more
comprehensive solutions.
Leverage it for documentation
Beyond coding, Claude Code excels at synthesizing documentation and
creating structured outputs. They provide writing samples and formatting
preferences to get documents they can immediately use in Slack, Google
Docs, and other tools to avoid interface switching fatigue.
8
Claude Code for security engineering
Claude Code for security
■
■
eng1neer1ng
Team impact
Top tips from the
Security Engineering
team
8
Reduced incident resolution time
Infrastructure debugging that normally takes 10-15 minutes of manual
code scanning now takes about 5 minutes.
Improved security review cycle
Terraform code reviews for security approval happen much faster,
eliminating developer blocks while waiting for security team approval.
Enhanced cross-functional contribution
Team members can meaningfully contribute to projects within days
instead of weeks of context building.
Better documentation workflow
Synthesized troubleshooting guides and runbooks from multiple sources
create more efficient debugging processes.
Use custom slash commands extensively
Security engineering uses 50% of all custom slash command
implementations in the entire monorepo. These custom commands
streamline specific workflows and speed up repeated tasks.
Let Claude talk first
Instead of asking targeted questions for code snippets, they now
tell Claude Code to "commit your work as you go" and let it work
autonomously with periodic check-ins, resulting in more
comprehensive solutions.
Leverage it for documentation
Beyond coding, Claude Code excels at synthesizing documentation and
creating structured outputs. They provide writing samples and formatting
preferences to get documents they can immediately use in Slack, Google
Docs, and other tools to avoid interface switching fatigue.
CLAUDE CODE FOR SECURITY ENGINEERING

Claude Code for inference
The Inference team manages
the memory system that stores
information while Claude reads
your prompt and generates its
response. Team members,
especially those who are new to
machine learning, can use Claude
Code extensively to bridge that
knowledge gap and accelerate
their work.
Main Claude Code use cases
Codebase comprehension and onboarding
The team relies heavily on Claude Code to quickly understand the
architecture when joining a complex codebase. Instead of manually
searching GitHub repos, they ask Claude to find which files call specific
functionalities, getting results in seconds rather than asking colleagues or
searching manually.
Unit test generation with edge case coverage
After writing core functionality, they ask Claude to write comprehensive
unit tests. Claude automatically includes missed edge cases, completing
what would normally take significant mental energy in minutes, acting
like a coding assistant they can review.
Machine learning concept explanation
Without a machine learning background, team members depend on
Claude to explain model-specific functions and settings. What would
require an hour of Google searching and reading documentation now
takes 10-20 minutes, reducing research time by 80%.
Cross-language code translation
When testing functionality in different programming languages, they
explain what they want to test and Claude writes the logic in the required
language (like Rust), eliminating the need to learn new languages just for
testing purposes.
Command recall and Kubernetes management
Instead of remembering complex Kubernetes commands, they ask Claude
for the correct syntax, like “how to get all pods or deployment status,” and
receive the exact commands needed for their infrastructure work.
9
Claude Code for inference
Claude Code for inference
9
The Inference team manages
the memory system that stores
information while Claude reads
your prompt and generates its
response. Team members,
especially those who are new to
machine learning, can use Claude
Code extensively to bridge that
knowledge gap and accelerate
their work.
Main Claude Code use cases
Codebase comprehension and onboarding
The team relies heavily on Claude Code to quickly understand the
architecture when joining a complex codebase. Instead of manually
searching GitHub repos, they ask Claude to find which files call specific
functionalities, getting results in seconds rather than asking colleagues or
searching manually.
Unit test generation with edge case coverage
After writing core functionality, they ask Claude to write comprehensive
unit tests. Claude automatically includes missed edge cases, completing
what would normally take significant mental energy in minutes, acting
like a coding assistant they can review.
Machine learning concept explanation
Without a machine learning background, team members depend on
Claude to explain model-specific functions and settings. What would
require an hour of Google searching and reading documentation now
takes 10-20 minutes, reducing research time by 80%.
Cross-language code translation
When testing functionality in different programming languages, they
explain what they want to test and Claude writes the logic in the required
language (like Rust), eliminating the need to learn new languages just for
testing purposes.
Command recall and Kubemetes management
Instead of remembering complex Kubernetes commands, they ask Claude
for the correct syntax, like "how to get all pods or deployment status," and
receive the exact commands needed for their infrastructure work.
CLAUDE CODE FOR INFERENCE