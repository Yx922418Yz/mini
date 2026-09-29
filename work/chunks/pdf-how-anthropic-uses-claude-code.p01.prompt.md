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

How Anthropic teams
use Claude Code
Anthropic’s internal teams are transforming their workflows with Claude Code, enabling
developers and non-technical staff to tackle complex projects, automate tasks, and bridge
skill gaps that previously limited their productivity.
Through interviews with our own Claude Code power users, we’ve gathered insights on how
different departments leverage Claude Code, its impact on their work, and tips for other
organizations considering adoption.
ANTHROP\C
How Anthropic teams
use Claude Code
</>
Anthropic's internal teams are transforming their workflows with Claude Code, enabling
developers and non-technical staff to tackle complex projects, automate tasks, and bridge
skill gaps that previously limited their productivity.
Through interviews with our own Claude Code power users, we've gathered insights on how
different departments leverage Claude Code, its impact on their work, and tips for other
organizations considering adoption.

Contents
Claude Code for data infrastructure
3
Claude Code for product development
5
Claude Code for security engineering
7
Claude Code for inference
9
Claude Code for data science and visualization
11
Claude Code for API
13
Claude Code for growth marketing
15
Claude Code for product design
17
Claude Code for RL engineering
19
Claude Code for legal
21
2
How Anthropic teams use Claude Code
Contents
2
Claude Code for data infrastructure
Claude Code for product development
Claude Code for security engineering
Claude Code for inference
Claude Code for data science and visualization
Claude Code for API
Claude Code for growth marketing
Claude Code for product design
Claude Code for RL engineering
Claude Code for legal
3
5
7
9
11
13
15
17
19
21
HOW ANTHROPIC TEAMS USE CLAUDE CODE

Claude Code for data
infrastructure
The Data Infrastructure team
organizes all business data for
teams across the company. They
use Claude Code for automating
routine data engineering tasks,
troubleshooting complex
infrastructure issues, and
creating documented workflows
for technical and non-technical
team members to access and
manipulate data independently.
Main Claude Code use cases
Kubernetes debugging with screenshots
When Kubernetes clusters went down and weren’t scheduling new pods,
the team used Claude Code to diagnose the issue. They fed screenshots of
dashboards into Claude Code, which guided them through Google Cloud’s
UI menu by menu until they found a warning indicating pod IP address
exhaustion. Claude Code then provided the exact commands to create a
new IP pool and add it to the cluster, bypassing the need to involve
networking specialists.
Plain text workflows for finance team
The team showed finance team members how to write plain text files
describing their data workflows, then load them into Claude Code to get
fully automated execution. Employees with no coding experience could
describe steps like “query this dashboard, get information, run these
queries, produce Excel output,” and Claude Code would execute the entire
workflow, including asking for required inputs like dates.
Codebase navigation for new hires
When new data scientists join the team, they’re directed to use Claude
Code to navigate their massive codebase. Claude Code reads their
Claude.md files (documentation), identifies relevant files for specific
tasks, explains data pipeline dependencies, and helps newcomers
understand which upstream sources feed into dashboards. This replaces
traditional data catalogs and discoverability tools.
End-of-session documentation updates
The team asks Claude Code to summarize completed work sessions and
suggest improvements at the end of each task. This creates a continuous
improvement loop where Claude Code helps refine the Claude.md
documentation and workflow instructions based on actual usage, making
subsequent iterations more effective.
Parallel task management across multiple instances
When working on long-running data tasks, they open multiple instances
of Claude Code in different repositories for different projects. Each
instance maintains full context, so when they switch back after hours or
days, Claude Code remembers exactly what they were doing and where
they left off, enabling true parallel workflow management without
context loss.
3
Claude Code for data infrastructure
Claude Code for data
infrastructure
3
The Data Infrastructure
team
organizes all business data for
teams across the company. They
use Claude Code for automating
routine data engineering tasks,
troubleshooting
complex
infrastructureissues,and
creating documented workflows
for technical and non-technical
team members to access and
manipulate data independently.
Main Claude Code use cases
Kubernetes debugging with screenshots
When Kubernetes clusters went down and weren't scheduling new pods,
the team used Claude Code to diagnose the issue. They fed screenshots of
dashboards into Claude Code, which guided them through Google Cloud's
UI menu by menu until they found a warning indicating pod IP address
exhaustion. Claude Code then provided the exact commands to create a
new IP pool and add it to the cluster, bypassing the need to involve
networking specialists.
Plain text workflows for finance team
The team showed finance team members how to write plain text files
describing their data workflows, then load them into Claude Code to get
fully automated execution. Employees with no coding experience could
describe steps like "query this dashboard, get information, run these
queries, produce Excel output," and Claude Code would execute the entire
workflow, including asking for required inputs like dates.
Codebase navigation for new hires
When new data scientists join the team, they're directed to use Claude
Code to navigate their massive codebase. Claude Code reads their
Claude.md files (documentation), identifies relevant files for specific
tasks, explains data pipeline dependencies, and helps newcomers
understand which upstream sources feed into dashboards. This replaces
traditional data catalogs and discoverability tools.
End-of-session documentation updates
The team asks Claude Code to summarize completed work sessions and
suggest improvements at the end of each task. This creates a continuous
improvement loop where Claude Code helps refine the Claude.md
documentation and workflow instructions based on actual usage, making
subsequent iterations more effective.
Parallel task management across multiple instances
When working on long-running data tasks, they open multiple instances
of Claude Code in different repositories for different projects. Each
instance maintains full context, so when they switch back after hours or
days, Claude Code remembers exactly what they were doing and where
they left off, enabling true parallel workflow management without
context loss.
CLAUDE CODE FOR DATA INFRASTRUCTURE