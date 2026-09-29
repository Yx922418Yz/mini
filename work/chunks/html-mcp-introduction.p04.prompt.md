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

Enabling AI-powered automation: In industries such as finance, healthcare, or manufacturing, MCP can automate tasks and processes, improving productivity and reducing errors.

MCP’s flexibility and adaptability make it an attractive solution for developers and organizations looking to leverage AI and machine learning in their applications.

By providing a standardized interface for AI models to interact with data sources and tools, MCP enables innovation and experimentation in the AI ecosystem.

This standardized approach not only simplifies the integration process but also ensures that AI models can access the data and tools they need to perform at their best.

In summary, MCP opens up a world of possibilities for AI applications, allowing developers to create more integrated, autonomous, and scalable solutions.

Whether it’s enhancing customer service with AI-powered chatbots or automating complex workflows in industrial settings, MCP provides the tools and framework needed to bring these innovations to life.

Conclusion
Model Context Protocol (MCP) is an exciting development in AI development because it allows developers to safely and efficiently connect our increasingly intelligent language models to the extensive world of software and data previously difficult to connect with.

By introducing a common protocol, MCP lets us build AI systems that are more integrated, autonomous, and easier to scale.

Instead of writing one-off plugins or giving the model brittle instructions for each new tool, we have a coherent framework where AI agents can discover and use tools on the fly, with proper oversight and security.

While the protocol is still evolving (authentication was a recent addition, and more features like standardized server discovery are on the horizon, it’s clear that MCP or something like it will play a key role in the next generation of AI applications.

For developers, now is a great time to familiarize yourself with MCP concepts.

Whether you’re enhancing a chatbot with company-specific knowledge or building an AI agent that automates workflows, MCP can save you time and headaches by handling the “plumbing” of tool integration.

And since it’s an open standard backed by a growing community (and companies like Anthropic), it’s likely to become a foundational piece of AI infrastructure moving forward.

In summary, Model Context Protocol enables a world where AI assistants are not siloed geniuses but well-equipped engineers and assistants – able to interface with many systems, follow procedures, and fetch or create information as needed, all through a unified, secure interface.

That’s a powerful vision, and one that is quickly becoming reality with MCP.

At Stytch, we’re focused on easily solving the remote MCP server auth problem for customers, so they can easily stand up MCP servers for their applications to allow end users to provide permissioned access to MCP clients.

MCP auth with Stytch
Use Stytch Connected Apps to build authentication with MCP servers
Read the docs
Share this article
LinkedIn
X
Facebook
Related Articles
Product
Feb 20, 2025
Stytch Connected Apps: Make any app an OAuth provider for integrations and AI agents
Auth & identity
Feb 8, 2025
The age of agent experience
Auth & identity
Feb 15, 2025
Detecting AI agent use & abuse
Get started
with Stytch
Start building for freeExplore our docs
Authentication & Authorization
For consumer applications
For B2B SaaS applications
Admin Portal
Connected Apps
Single sign-on
Fraud & Risk Prevention
Fingerprinting
Active risk assessment
Fine-grained enforcement
Why Stytch
Stytch vs.

Auth0
Stytch vs.

Firebase
Stytch vs.

Cognito
Stytch vs.

Fingerprint
Company
About us
Careers
Contact
Resources
Pricing
Docs
Changelog
Product roadmap
API status
Blog
Community
Slack community
Technical support
Customer stories
© 2020-2026 Stytch.

All rights reserved.

Terms of use
Privacy Policy