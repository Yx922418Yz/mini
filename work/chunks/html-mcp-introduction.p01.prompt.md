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

Back to blog
Model Context Protocol (MCP): A comprehensive introduction for developers
Auth & identity
Mar 28, 2025
Author: Reed McGinley-Stempel
Executive summary
Model Context Protocol (MCP) is an open standard that bridges AI models with external data and services, allowing Large Language Models (LLMs) to make structured API calls in a consistent, secure way.

This post will introduce MCP, explain why it’s valuable for connecting AI systems, compare it to existing approaches like ChatGPT plugins and manual API integrations, and dive into its recent support for OAuth-based authentication.

We’ll also explore a bit of code to see MCP in action.

MCP acts as a universal adapter between AI tools and external services, eliminating the need for custom integration code for each tool or API.

Much like USB-C simplifies connectivity across diverse devices, MCP provides a uniform method for AI models to invoke external functions, retrieve data, or use predefined prompts.

At its core, MCP offers one interface that connects to many different systems.

What is Model Context Protocol MCP?

MCP is essentially a universal adapter between AI applications and external tools or data sources.

It defines a common protocol (built on JSON-RPC 2.0) that lets an AI assistant invoke functions, fetch data, or use predefined prompts from external services in a structured manner.

Instead of every LLM app needing custom code for each API or database, MCP provides one standardized “language” for all interactions.

The MCP layer enables AI applications to securely access and interact with external data sources and tools.

It serves as a bridge between large language models (LLMs) and various databases, applications, or APIs, facilitating seamless integration and functionality without the need for extensive custom coding.

MCP uses a client-server architecture to achieve this.

The AI-powered application (e.g.

a chatbot, IDE assistant, or agent) acts as the host and runs an MCP client component, while each external integration runs as an MCP server.

The server exposes capabilities (like functions, data resources, or prompt templates) over the MCP protocol, and the client connects to it to utilize those capabilities.

This separation means the AI model doesn’t talk to APIs directly; instead, it goes through the MCP client/server handshake, which structures the exchange.

Source
Why MCP is Valuable
In traditional setups, connecting an AI model to external data or actions was tedious and ad-hoc.

Developers often had to write one-off integrations for each API or database they wanted the model to use, dealing with different auth, data formats, and error handling for each.

MCP changes the game by standardizing these interactions.

Key benefits include:
Rapid Tool Integration: With MCP, you can plug in new capabilities without custom-coding each from scratch.

If an MCP server exists for, say, Google Drive or a SQL database, any MCP-compatible AI app can connect to it and immediately gain that ability.

This is a huge win for automation—AI agents can fetch documents, query databases, or call APIs as needed, just by adding the appropriate server.

It’s like having a library of ready-made “plugins” that all speak the same language.

MCP servers serve as lightweight programs that expose specific capabilities through a standardized protocol, acting as intermediaries between the Cursor and various external tools or data sources.

Autonomous Agents: MCP empowers more autonomous AI behavior.

Agents are not limited to their built-in knowledge; they can actively retrieve information or perform actions in multi-step workflows.

For example, a sophisticated agent might use MCP to gather data from a CRM, then send an email via a communications tool, then log a record in a database – all in one seamless chain.

By enabling fluid, context-aware, multi-step interactions, MCP helps AI agents move closer to true autonomous task execution.

As one observer noted, MCP turns an AI from an isolated “brain” into a versatile “doer” by giving it standardized access to real-world tools and data.

Reduced Friction and Setup: Because MCP acts as a universal interface, developers avoid the fragmentation of maintaining separate integrations.

Once an application supports MCP, it can connect to any number of services through a single mechanism .

This dramatically reduces the manual setup required each time you want your AI to use a new API.

Teams can focus on higher-level logic rather than reinventing connection code for the 10th time.

As Anthropic put it, MCP replaces fragmented integrations with a simpler, more reliable single protocol for data access.

Consistency and Interoperability: MCP enforces a consistent request/response format across tools.

This means your AI app doesn’t have to handle one HTTP response for Service A, another XML for Service B, etc.

The model’s outputs (function calls) and the tool results are all passed in a uniform JSON structure.

That consistency makes it easier to debug and scale.

It also future-proofs your integration logic – even if you switch underlying model vendors, MCP’s interface to the tools remains the same.

Two-Way Context: Unlike simple API calls, MCP supports maintaining context and ongoing dialogue between the model and the tool.

An MCP server can provide Prompts (predefined prompt templates for certain tasks) and Resources (data context like documents) in addition to tools.

This means the AI can not only “call an API” but also ingest reference data or follow complex workflows guided by the server.

The protocol was designed to support rich interactions, not just one-off queries.

This is especially useful in applications like coding assistants (where an AI might iterate with a development environment via MCP) or complex decision-making tasks that require back-and-forth with various data sources.

In short, MCP brings a scalable, plug-and-play approach to enhancing LLMs.

It lets AI systems securely tap into the “live” data and actions they need, without each developer having to reinvent the wheel.

Early adopters of MCP have already built servers for tools like Google Drive, Slack, GitHub, databases, and more – showcasing how AI agents can use MCP to work with enterprise content repositories, dev ops tools, and other real-world systems.

The MCP architecture – How it works at-a-glance
Client-Server structure
MCP follows a clear client-server architecture:
MCP Client: Embedded in AI applications (chatbots, IDE assistants, automation agents).

MCP Server: Exposes external capabilities such as functions (tools), resources (data), and prompts (templates).

All interactions occur through standardized JSON-RPC messages, maintaining a secure, structured exchange:
Example JSON-RPC Request:
For example, to list available tools, an MCP client sends a request like this:
{
"jsonrpc": "2.0",
"id": 1,
"method": "tools/list",
"params": {}
}The server would reply with a structured JSON listing the tools (each with a name, description, and input schema).

For instance, a server might advertise a get_weather tool and describe what inputs it needs.

{
"jsonrpc": "2.0",
"id": 1,
"result": [
{ "name": "get_weather", "description": "Retrieves weather data.", "schema": { "location": "string" } }
]
}Later, when the LLM decides to use a tool, the client invokes a call to do so.

The MCP server executes the function and returns the result in a structured JSON response.

The MCP client (within the host app) can then feed that result back into the model’s context or response.

In practice, the host application mediates this process: it translates the LLM’s intent (often via the model’s function call output) into an MCP request, and then passes the server’s structured result back to the LLM .

This two-way exchange is secure and controlled – the model can only call the specific tools the server exposes, and all data passing in/out goes through the defined protocol.

Building and deploying MCP servers
Building and deploying MCP servers is a crucial step in leveraging the Model Context Protocol (MCP) for AI integrations.

MCP servers act as intermediaries between AI models and external data sources or tools, enabling seamless communication and data exchange.

One of the standout features of MCP is its flexibility in server development.

Developers can use any programming language that can print to stdout or serve an HTTP endpoint, allowing them to choose their preferred language and technology stack.

When building an MCP server, it’s essential to consider the architecture and design.

MCP follows a client-server architecture, where a host application can connect to multiple servers.

This architecture enables scalability and flexibility, allowing developers to design MCP servers that handle various tasks and functions, such as data processing, tool integration, or AI model management.

Deploying MCP servers can be done in various environments, including local development environments, cloud platforms, or on-premises infrastructure.