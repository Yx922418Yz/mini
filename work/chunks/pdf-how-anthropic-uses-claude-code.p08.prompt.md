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

Claude Code for growth
marketing
Team impact
Dramatic time savings on repetitive tasks
Ad copy creation reduced from 2 hours to 15 minutes, freeing up time for
strategic work.
10x increase in creative output
The team can now test vastly more ad variations across channels with
automated generation and Figma integration.
Operating like a larger team
The team can handle tasks that traditionally required dedicated
engineering resources.
Strategic focus shift
The team can spend more time on overall strategy and building agentic
automation rather than manual execution.
Top tips from the
Growth Marketing
team
Identify API-enabled repetitive tasks
Look for workflows involving repetitive actions with tools that have
APIs (like ad platforms, design tools, analytics platforms). These are
prime candidates for automation and where Claude Code provides the
most value.
Break complex workflows into specialized sub-agents
Instead of trying to handle everything in one prompt or workflow, create
separate agents for specific tasks (like their headline agent vs. description
agent). This makes debugging easier and improves output quality when
dealing with complex requirements.
Thoroughly brainstorm and prompt plan before coding
Spend significant time upfront using Claude.ai to think through your
entire workflow, then have Claude.ai create a comprehensive prompt and
code structure for Claude Code to reference. Also, work step-by-step
rather than asking for one-shot solutions to avoid Claude getting
overwhelmed by complex tasks.
16
Claude Code for growth marketing
Claude Code for growth
marketing
Team impact
Top tips from the
Growth Marketing
team
16
Dramatic time savings on repetitive tasks
Ad copy creation reduced from 2 hours to 15 minutes, freeing up time for
strategic work.
10x increase in creative output
The team can now test vastly more ad variations across channels with
automated generation and Figma integration.
Operating like a larger team
The team can handle tasks that traditionally required dedicated
engineering resources.
Strategic focus shift
The team can spend more time on overall strategy and building agentic
automation rather than manual execution.
Identify API-enabled repetitive tasks
Look for workflows involving repetitive actions with tools that have
APis (like ad platforms, design tools, analytics platforms). These are
prime candidates for automation and where Claude Code provides the
most value.
Break complex workflows into specialized sub-agents
Instead of trying to handle everything in one prompt or workflow, create
separate agents for specific tasks (like their headline agent vs. description
agent). This makes debugging easier and improves output quality when
dealing with complex requirements.
Thoroughly brainstorm and prompt plan before coding
Spend significant time upfront using Claude.ai to think through your
entire workflow, then have Claude.ai create a comprehensive prompt and
code structure for Claude Code to reference. Also, work step-by-step
rather than asking for one-shot solutions to avoid Claude getting
overwhelmed by complex tasks.
CLAUDE CODE FOR GROWTH MARKETING

Claude Code for product design
The Product Design team
supports Claude Code, Claude.ai
and the Anthropic API,
specializing in building AI
products. Even non-developers
can use Claude Code to bridge
the traditional gap between
design and engineering, enabling
direct implementation of their
design vision without extensive
back-and-forth with engineers.
Main Claude Code use cases
Front-end polish and state management changes
Instead of creating extensive design documentation and going through
multiple rounds of feedback with engineers for visual tweaks (typefaces,
colors, spacing), they now directly implement these changes using Claude
Code. Engineers noted they’re making “large state management changes
that you typically wouldn’t see a designer making,” enabling them to
achieve the exact quality they envision.
GitHub Actions automated ticketing
Using Claude Code’s GitHub integration, they can simply file issues/
tickets describing needed changes, and Claude automatically proposes
code solutions without having to open Claude Code, creating a seamless
bug-fixing and feature refinement workflow for their persistent backlog
of polish tasks.
Rapid interactive prototyping
By pasting mockup images into Claude Code, they generate fully
functional prototypes that engineers can immediately understand and
iterate on, replacing the traditional cycle of static Figma designs that
required extensive explanation and translation to working code.
Edge case discovery and system architecture understanding
They use Claude Code to map out error states, logic flows, and different
system statuses, allowing them to identify edge cases during design rather
than discovering them later in development, fundamentally improving
the quality of their initial designs.
Complex copy changes and legal compliance
For tasks like removing “research preview” messaging across the entire
codebase, they used Claude Code to find all instances, review surrounding
copy, coordinate changes with legal in real-time, and implement updates -
a process that took two 30-minute calls instead of a week of back-and-
forth coordination.
17
Claude Code for product design
Claude Code for product design
17
The Product Design team
supports Claude Code, Claude.ai
and the Anthropic API,
specializing in building Al
products. Even non-developers
can use Claude Code to bridge
the traditional
gap between
design and engineering, enabling
direct implementation
of their
design vision without extensive
back-and-forth
with engineers.
Main Claude Code use cases
Front-end polish and state management changes
Instead of creating extensive design documentation and going through
multiple rounds of feedback with engineers for visual tweaks (typefaces,
colors, spacing), they now directly implement these changes using Claude
Code. Engineers noted they're making "large state management changes
that you typically wouldn't see a designer making," enabling them to
achieve the exact quality they envision.
GitHub Actions automated ticketing
Using Claude Code's GitHub integration, they can simply file issues/
tickets describing needed changes, and Claude automatically proposes
code solutions without having to open Claude Code, creating a seamless
bug-fixing and feature refinement workflow for their persistent backlog
of polish tasks.
Rapid interactive prototyping
By pasting mockup images into Claude Code, they generate fully
functional prototypes that engineers can immediately understand and
iterate on, replacing the traditional cycle of static Figma designs that
required extensive explanation and translation to working code.
Edge case discovery and system architecture understanding
They use Claude Code to map out error states, logic flows, and different
system statuses, allowing them to identify edge cases during design rather
than discovering them later in development, fundamentally improving
the quality of their initial designs.
Complex copy changes and legal compliance
For tasks like removing "research preview" messaging across the entire
code base, they used Claude Code to find all instances, review surrounding
copy, coordinate changes with legal in real-time, and implement updates -
a process that took two 30-minute calls instead of a week ofback-and-
forth coordination.
CLAUDE CODE FOR PRODUCT DESIGN