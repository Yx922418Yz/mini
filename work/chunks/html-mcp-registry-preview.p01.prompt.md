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

Today, we’re launching the Model Context Protocol (MCP) Registry—an open catalog and API for publicly available MCP servers to improve discoverability and implementation. By standardizing how servers are distributed and discovered, we’re expanding their reach while making it easier for clients to get connected.
The MCP Registry is now available in preview. To get started:
Add your server by following our guide on Adding Servers to the MCP Registry (for server maintainers)
Access server data by following our guide on Accessing MCP Registry Data (for client maintainers)
Single source of truth for MCP servers#
In March 2025, we shared that we wanted to build a central registry for the MCP ecosystem. Today we are announcing that we’ve launched https://registry.modelcontextprotocol.io as the official MCP Registry. As part of the MCP project, the MCP Registry, as well as a parent OpenAPI specification, are open source—allowing everyone to build a compatible sub-registry.
Our goal is to standardize how servers are distributed and discovered, providing a primary source of truth that sub-registries can build upon. In turn, this will expand server reach and help clients find servers more easily across the MCP ecosystem.
Public and private sub-registries#
In building a central registry, it was important to us not to take away from existing registries that the community and companies have built. The MCP Registry serves as a primary source of truth for publicly available MCP servers, and organizations can choose to create sub-registries based on custom criteria. For example:
Public subregistries like opinionated “MCP marketplaces” associated with each MCP client are free to augment and enhance data they ingest from the upstream MCP Registry. Every MCP end-user persona will have different needs, and it is up to the MCP client marketplaces to properly serve their end-users in opinionated ways.
Private subregistries will exist within enterprises that have strict privacy and security requirements, but the MCP Registry gives these enterprises a single upstream data source they can build upon. At a minimum, we aim to share API schemas with these private implementations so that associated SDKs and tooling can be shared across the ecosystem.
In both cases, the MCP Registry is the starting point – it’s the centralized location where MCP server maintainers publish and maintain their self-reported information for these downstream consumers to massage and deliver to their end-users.
Community-driven mechanism for moderation#
The MCP Registry is an official MCP project maintained by the registry working group and permissively licensed. Community members can submit issues to flag servers that violate the MCP moderation guidelines—such as those containing spam, malicious code, or impersonating legitimate services. Registry maintainers can then denylist these entries and retroactively remove them from public access.
Getting started#
To get started:
Add your server by following our guide on Adding Servers to the MCP Registry (for server maintainers)
Access server data by following our guide on Accessing MCP Registry Data (for client maintainers)
This preview of the MCP Registry is meant to help us improve the user experience before general availability and does not provide data durability guarantees or other warranties. We advise MCP adopters to watch development closely as breaking changes may occur before the registry is made generally available.
As we continue to develop the registry, we encourage feedback and contributions on the modelcontextprotocol/registry GitHub repository: Discussion, Issues, and Pull Requests are all welcome.
Thanks to the MCP community#
The MCP Registry has been a collaborative effort from the beginning and we are incredibly grateful for the enthusiasm and support from the broader developer community.
In February 2025, it began as a grassroots project when MCP creators David Soria Parra and Justin Spahr-Summers asked the PulseMCP and Goose teams to help build a centralized community registry. Registry Maintainer Tadas Antanavicius from PulseMCP spearheaded the initial effort in collaboration with Alex Hancock from Block. They were soon joined by Registry Maintainer Toby Padilla, Head of MCP at GitHub, and more recently, Adam Jones from Anthropic joined as Registry Maintainer to drive the project towards the launch today. The initial announcement of the MCP Registry’s development lists 16 contributing individuals from at least 9 different companies.
Many others made crucial contributions to bring this project to life: Radoslav Dimitrov from Stacklok, Avinash Sridhar from GitHub, Connor Peet from VS Code, Joel Verhagen from NuGet, Preeti Dewani from Last9, Avish Porwal from Microsoft, Jonathan Hefner, and many Anthropic and GitHub employees that provided code reviews and development support. We are also grateful to everyone on the Registry’s contributors log and those who participated in discussions and issues.
We deeply appreciate everyone investing in this foundational open source infrastructure. Together, we’re helping developers and organizations worldwide to build more reliable, context-aware AI applications. On behalf of the MCP community, thank you.