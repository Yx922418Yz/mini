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

Invoke the Tool via MCP – The client now sends a tools/call request to the server with the chosen tool name and parameters.

We saw an example JSON for this earlier.

In code, using an SDK, it might look like:
const result = await mcpClient.request({
method: 'tools/call',
params: { name: toolName, arguments: toolArgs }
}, CallToolResultSchema);This will cause the server to execute the tool’s handler on its side.

The server might be calling an external API, performing a database query, or whatever logic that tool encapsulates.

The result (could be a simple value or a complex JSON object) is sent back in a result field of the MCP response.

5.

Return the Result to the LLM – The MCP client receives the tool’s output.

Now the host application can integrate that back into the AI’s response.

In many agent setups, the pattern is to inject the result into the conversation and ask the model to continue.

For example, the assistant might then present: “The current stock price of AAPL is $173.22 (USD).” If using an automated loop, the result can be given to the model (perhaps appended to the conversation as a system message like “Result of get_current_stock_price: ...”) and the model can continue answering the user’s query with that information in mind.

Here’s a simplified illustration of calling a tool and using the result in a conversation using Anthropic’s Claude (which natively supports tool use):
// 1.

Send user prompt to LLM with available tools context
const response = await anthropicClient.complete({
prompt: "User: Can you list my projects?\nAssistant: ",
model: "claude-3.5",
tools: tools // list of tools from MCP server
});
for (const msg of response.messages) {
if (msg.type === 'tool_use') {
// 2.

LLM decided to use a tool
const { name, args } = msg;
// 3.

Call the tool via MCP
const toolRes = await mcpClient.request({ method: 'tools/call', params: { name, arguments: args } });
// 4.

Inject tool result and resume LLM
await anthropicClient.send({ role: 'system', content: `Tool result: ${toolRes.result}` });
} else {
// 5.

Handle normal LLM reply (tool result likely integrated)
console.log("Assistant:", msg.content);
}
In reality, frameworks handle a lot of this for you, but the above pseudo-code sketches how MCP fits into the loop.

The key point is that MCP provides the standardized call/response layer for tool execution, which the AI agent code can hook into.

Whether you’re using OpenAI, Anthropic, or another LLM, MCP stays the same – it’s the glue between the model’s intents and the external actions.

By using MCP, developers get a clear, structured pipeline for extending AI capabilities.

The code becomes more maintainable (since you’re calling a generic mcpClient.request rather than service-specific code in each place) and the AI becomes more powerful (since it can tap into any MCP-connected service).

Debugging is also easier – you can monitor the JSON-RPC messages to see exactly what was requested and returned, rather than parsing model-generated text for clues.

Early limitations (no built-in authentication)
When MCP first emerged (late 2024), it offered the core protocol for tool and data exchange, but it lacked a standardized authentication mechanism for connecting to remote servers.

In practice, early MCP demos and implementations often required running the MCP server locally or in a trusted environment, where authentication wasn’t a big concern (since the AI and server ran on the same machine).

For example, developers could run an MCP server for Google Drive on their localhost with a pre-obtained token, then point their AI app to it.

But using MCP over the internet or with third-party services was tricky without a formal auth flow.

Many initial MCP servers assumed the user would manually provide credentials or API keys to the server at startup.

As an example, Anthropic’s quickstart suggested running pre-built servers by supplying your own credentials (API keys, tokens) via config or command-line.

That means the server itself had access to your keys and the MCP client just trusted that server.

While this works for personal or single-user scenarios, it doesn’t scale well for multi-user applications or cloud-hosted agents.

There was no standard handshake for an AI agent to say, “Hey, I’m allowed to access this service on behalf of User X; here are my credentials.”
Essentially, early MCP clients had no way to authenticate to an MCP server except by out-of-band means (like pre-sharing a token or running without auth).

This was a notable limitation – MCP was designed to be open and internet-based, but without an auth standard, secure remote use was handicapped.

The lack of authentication standard meant that MCP clients couldn’t safely connect to arbitrary servers on their own.

You either hard-coded a client ID/API key into the client (which is not ideal in distributed apps), or you had to run without auth and assume only authorized users could even reach the server (often by keeping it local).

Clearly, for MCP to reach its full potential (e.g.

connecting an AI agent to a cloud-hosted data source in a secure way), a better approach was needed.

The good news is that the community recognized this, and work was done to bake OAuth-based authentication into MCP.

OAuth 2.0 authentication flow
To address the initial authentication limitations and enhance secure connectivity, MCP adopted OAuth 2.0, a widely-recognized and robust authentication standard.

OAuth 2.0 provides a secure, scalable framework enabling MCP clients to interact safely with remote servers, cloud-hosted resources, and multi-user environments.

The key components and benefits of integrating OAuth 2.0 into MCP include:
Dynamic Client Registration (DCR): Model Context Protocol supports Dynamic Client Registration, allowing clients to register automatically with OAuth servers.

This removes the need for manual client setup or hard-coded credentials, significantly streamlining deployment for developers.

Automatic Endpoint Discovery: MCP utilizes standardized metadata URLs (following OAuth's discovery protocol) to allow clients to automatically discover OAuth endpoints.

This reduces configuration overhead and makes MCP deployments easier and more flexible.

Secure Authorization and Token Management: Clients securely obtain OAuth tokens tailored precisely to user permissions and access scopes.

This ensures that clients access only the resources explicitly permitted by the user, improving security and compliance, especially in multi-user and cloud environments.

Scalable and Secure Multi-User Support: OAuth 2.0's design inherently supports multiple concurrent users and services, addressing one of MCP's significant early limitations.

Applications can now seamlessly handle authorization flows for numerous users simultaneously, critical for widespread cloud adoption.

Debugging and troubleshooting
Debugging and troubleshooting are critical aspects of working with MCP servers and clients.

MCP provides various tools and techniques for debugging and troubleshooting, ensuring that developers can identify and resolve issues efficiently.

One of the key tools in this process is the MCP Inspector, an interactive debugging tool for MCP servers.

The MCP Inspector allows developers to test and inspect MCP servers, identifying and resolving issues with MCP server integrations.

This tool provides a detailed view of the interactions between MCP clients and servers, making it easier to pinpoint problems and understand the underlying causes.

Additionally, MCP provides a comprehensive debugging guide that outlines common issues and solutions, helping developers to troubleshoot and resolve problems quickly.

When debugging MCP servers, it’s essential to consider the architecture and design of the system.

Developers should identify the specific components or modules that are causing issues and use tools like the MCP Inspector to diagnose and resolve problems.

By focusing on a systematic approach to debugging and leveraging the available tools, developers can ensure that their MCP integrations are robust and reliable.

Real-world applications of MCP
The Model Context Protocol (MCP) has various real-world applications across industries and domains.

One of the primary use cases for MCP is in AI integrations, where MCP enables seamless communication and data exchange between AI models and external data sources or tools.

MCP can be used in various applications, such as:
Building AI-powered chatbots: These chatbots can access external data sources or tools, providing users with accurate and up-to-date information.

Creating AI-driven workflows: MCP enables the integration of AI models with external systems or data sources, automating complex workflows and improving efficiency.

Developing AI models: These models can interact with external tools or data sources, enhancing their capabilities and providing more accurate and relevant outputs.