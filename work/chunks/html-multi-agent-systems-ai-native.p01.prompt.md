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

The role of multi agent systems in making software engineers AI-native 4 workflows to adopt AI agents, beyond code generation
Get the practical guide
Machines on call for humans
Contact us
Join the conversation
©Resolve.ai - All rights reserved
Terms of ServicePrivacy Policy
Back to Blog
Technology
The role of multi agent systems in making software engineers AI-native
03/20/2026
Share:
Generative AI has transformed software development so dramatically that you can spin up entire services in hours, yet understanding what went wrong with those services still demands painstaking work across fragmented tools.

From code generation to code review, coding agents handle the build side.

But production debugging?

That's still manual.

Take the following example:
CodingProduction
To write a service: You open an AI-native development environment and ask AI to "Create a payment service that handles retries and timeouts".

AI generates implementation with error handling, using context of your code baseWhen the same service is experiencing high latency: You start with a hypothesis → Check Datadog for metrics → Switch to Loki for logs → Cross-reference deployment history → Correlate timestamps →...

And so on
The problem isn't AI's capability; it's how we architect AI systems.

Most engineering teams still use AI-powered tools to execute the same workflows faster, not reimagining how software development and production operations should work end-to-end.

At Resolve AI, we've been building multi-agent systems for engineers to work on production systems.

We've been advocating that engineering should be AI-native (where engineers primarily interface with autonomous agents to work on production systems), while most gen AI conversations in software engineering were centered on writing AI generated code with copilots and coding assistants.

We recently presented our approach to Stanford's graduate AI program, diving deep into the AI agents and their architectural patterns that enable AI-native engineering workflows.

What is AI-native engineering?

Why is it important?

AI-Native Engineering is where engineers primarily interface with AI to orchestrate their work: be it writing code or working on production systems.

AI-native is a significant departure from just “using AI” where engineers are still interfacing with their systems and tools, but using AI to speed up individual steps of the process.

Here is an example workflow to showcase the distinction.

AI-Assisted: You use AI tools to work faster on complex tasks.

The workflow remains human-centric: Engineer → Systems and tools → Correlation → Action.

Engineers still interface with tools, just using AI to perform individual tasks faster
AI-Native: AI becomes your primary interface for production work.

The workflow becomes AI-led: Engineer → Natural Language Request → AI System → Response / Action.

Engineers set goals and let AI agents handle the operational work
Take incident response as an example.

In AI-assisted workflows, you're still generating hypotheses, deciding which evidence matters, and manually correlating signals across tools.

AI helps with data retrieval and analysis, but you're doing the heavy lifting in investigation.

AI-native incident response operates differently: AI agents perform real-time triage of investigation priorities, generate competing hypotheses in parallel, and refine theories through successive iterations based on cross-system evidence.

Instead of asking "Can you analyze these logs?" you say "Resolve this checkout failure" and agents coordinate the entire investigation.

This isn't just faster.

It changes what problems deserve engineering attention.

When AI agents handle log analysis, metric correlation, and deployment timeline reconstruction, engineers operate at a higher-level, focusing on architectural decision-making and system design rather than tactical investigation.

The shift requires persistent AI agents, not just AI tools.

While AI models like those from OpenAI or Anthropic can accelerate individual tasks, only stateful agents can maintain investigation context, coordinate across multiple tools, and execute complex tasks across the full incident lifecycle autonomously.

Why are multi-agent systems essential to make engineering AI-native?

Modern production systems exhibit what academics call "irreducible interdependence": understanding them requires specialized knowledge across domains that cannot be unified into a single coherent model.

This is the insight most builders miss: No single AI tool or set of AI models can maintain expert-level knowledge across all these domains while coordinating a real-time investigation.

For example: When API latency spikes 10x during a critical incident, the investigation requires simultaneous specialized agents performing real-time analysis: correlating traces across 50+ microservices, analyzing slow database queries and connection pool exhaustion, checking recent deployments and infrastructure changes, scanning auth logs for security anomalies, evaluating auto-scaling functions against current load patterns, and analyzing support tickets for customer impact with SLA context.

Each of these functions requires domain-specific expertise and contextual data that no single system could effectively maintain.

At large-scale, as system complexity increases, individual AI tools lack the adaptability to handle exponential growth in context requirements.

This is where multi-agent systems can scale by combining orchestration and individual domain specialization.

This matrix provides an overview for engineering leaders.

Find the row that matches your current state to understand its limitations:
This framework reveals the technical limitations at each level:
ApproachWhat it isWhere the approach breaksCause for limitation
LLMUse LLMs (such as ChatGPT) for individual tasks like explanations, analysis, and documentationEngineers still do majority of the operational workloadSingle-pass generation prone to hallucinations, with no feedback loops or real-world integration
LLM + ToolsAI can call functions to fetch data from monitoring systems on commandCognitive workload of correlation remains on humansLimited context windows, no persistent state management across tool interactions
Single AgentAI follows investigation workflows independentlySequential investigation, gets stuck on wrong hypotheses without validationCannot manage diverse reasoning strategies or parallel investigation paths
Multi-AgentThrough multi-agent collaboration, specialized AI agents coordinate parallel investigations and combine their output into a unified diagnosisRequires investment in coordination protocolsDistributed intelligence needs formal communication schemas and conflict resolution
The progression reveals a fundamental architectural truth: Each level hits a different scalability ceiling.

LLMs lack a persistent state.

Tool-augmented LLMs can't maintain investigation context across multiple chats.

Even with sophisticated prompt engineering, single agents become decision-making bottlenecks as system complexity grows.

Only multi-agent systems can break through the sequential reasoning constraint that limits all previous approaches.

They enable parallel hypothesis testing while single agents must investigate sequentially, making them fundamentally unsuitable for the temporal demands of production incidents.

Building multi-agent systems is a hard engineering problem
No off-the-shelf agent framework like LangChain solves this alone.

Building production-ready multi-agent systems requires a rare combination of deep domain expertise and AI engineering prowess.

Most attempts fail because teams have expertise in one area but not both.

Here’s why this dual expertise is needed:
Domain expertise determines architecture: You can't architect agents without understanding production realities.

Only someone who's debugged production at 3 AM in a DevOps or SRE role knows that log patterns and metric anomalies require fundamentally different investigation strategies.

When payment failures spike, you need both database expertise and infrastructure expertise to determine the root cause.

Decisions like this aren’t AI problems.

They're production decisions that shape how you build your multi agent system.

AI expertise makes agents work together: Once you've decomposed the problem, you hit the hard part of computer science.

Context propagation between agents isn't intuition.

It is managing directed acyclic graphs of information flow where each agent's output feeds into the next agent's input.

Orchestrating parallel agents requires formal coordination protocols to prevent race conditions and deadlocks.

The system needs to learn continuously both from interactions and ephemeral failure modes.

Get one step wrong in coordinating agents and your system gets progressively worse, not better.

The intersection creates breakthrough systems: Domain knowledge without AI architecture is just expensive consulting.