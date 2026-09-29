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

Claude Code for legal
Work style and impact
Planning in Claude.ai, building in Claude Code
They use a two-step process where they brainstorm and plan with
Claude.ai first, then move to Claude Code for implementation, asking it
to slow down and work step-by-step rather than outputting everything
at once.
Visual-first approach
They frequently use screenshots to show Claude Code what they want
interfaces to look like, then iterate based on visual feedback rather than
describing features in text.
Prototype-driven innovation
They emphasize overcoming the fear of sharing “silly” or “toy”
prototypes, as these demonstrations inspire others to see possibilities
they hadn’t considered.
Security and
compliance awareness
MCP integration concerns
As product lawyers, they immediately identify security implications of
deep MCP integrations, noting how conservative security postures will
create barriers as AI tools access more sensitive systems.
Compliance tooling priorities
They advocate for building compliance tools quickly as AI
capabilities expand, recognizing the balance between innovation
and risk management.
Top tips from the
Legal Department
Plan extensively in Claude.ai first
Use Claude’s conversational interface to flesh out your entire idea before
moving to Claude Code. Then ask Claude to summarize everything into a
step-by-step prompt for implementation.
Work incrementally and visually
Ask Claude Code to slow down and implement one step at a time so you
can copy-paste without getting overwhelmed. Use screenshots liberally to
show what you want interfaces to look like.
Share prototypes despite imperfection
Overcome the urge to hide “toy” projects or unfinished work - sharing
prototypes helps others see possibilities and sparks innovation across
departments that don’t typically interact.
22
Claude Code for legal
Claude Code for legal
Work style and impact
Security and
compliance awareness
Top tips from the
Legal Department
22
Planning in Claude.ai, building in Claude Code
They use a two-step process where they brainstorm and plan with
Claude.ai first, then move to Claude Code for implementation, asking it
to slow down and work step-by-step rather than outputting everything
at once.
Visual-first approach
They frequently use screenshots to show Claude Code what they want
interfaces to look like, then iterate based on visual feedback rather than
describing features in text.
Prototype-driven innovation
They emphasize overcoming the fear of sharing "silly" or "toy"
prototypes, as these demonstrations inspire others to see possibilities
they hadn't considered.
MCP integration concerns
As product lawyers, they immediately identify security implications of
deep MCP integrations, noting how conservative security postures will
create barriers as AI tools access more sensitive systems.
Compliance tooling priorities
They advocate for building compliance tools quickly as AI
capabilities expand, recognizing the balance between innovation
and risk management.
Plan extensively in Claude.ai first
Use Claude's conversational interface to flesh out your entire idea before
moving to Claude Code. Then ask Claude to summarize everything into a
step-by-step prompt for implementation.
Work incrementally and visually
Ask Claude Code to slow down and implement one step at a time so you
can copy-paste without getting overwhelmed. Use screenshots liberally to
show what you want interfaces to look like.
Share prototypes despite hnperfection
Overcome the urge to hide "toy" projects or unfinished work - sharing
prototypes helps others see possibilities and sparks innovation across
departments that don't typically interact.
CLAUDE CODE FOR LEGAL