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

Build a Remote MCP server
This guide will show you how to deploy your own remote MCP server on Cloudflare using Streamable HTTP transport, the current MCP specification standard.

You have two options:
Without authentication â anyone can connect and use the server (no login required).

With authentication and authorization â users sign in before accessing tools, and you can control which tools an agent can call based on the user's permissions.

Choosing an approach
The Agents SDK provides multiple ways to create MCP servers.

Choose the approach that fits your use case:
ApproachStateful?Requires Durable Objects?Best for
createMcpHandler()NoNoStateless tools, simplest setup
McpAgentYesYesStateful tools, per-session state, elicitation
Raw WebStandardStreamableHTTPServerTransportNoNoFull control, no SDK dependency
createMcpHandler() is the fastest way to get a stateless MCP server running.

Use it when your tools do not need per-session state.

McpAgent gives you a Durable Object per session with built-in state management, elicitation support, and both SSE and Streamable HTTP transports.

Raw transport gives you full control if you want to use the @modelcontextprotocol/sdk directly without the Agents SDK helpers.

Deploy your first MCP server
You can start by deploying a public MCP server â without authentication, then add user authentication and scoped authorization later.

If you already know your server will require authentication, you can skip ahead to the next section.

Via the dashboard
The button below will guide you through everything you need to do to deploy an example MCP server â to your Cloudflare account:
Once deployed, this server will be live at your workers.dev subdomain (for example, remote-mcp-server-authless.your-account.workers.dev/mcp).

You can connect to it immediately using the AI Playground â (a remote MCP client), MCP inspector â or other MCP clients.

A new git repository will be set up on your GitHub or GitLab account for your MCP server, configured to automatically deploy to Cloudflare each time you push a change or merge a pull request to the main branch of the repository.

You can clone this repository, develop locally, and start customizing the MCP server with your own tools.

Via the CLI
You can use the Wrangler CLI to create a new MCP Server on your local machine and deploy it to Cloudflare.

Open a terminal and run the following command:
npm create cloudflare@latest -- remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
yarn create cloudflare remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
pnpm create cloudflare@latest remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
During setup, select the following options: - For Do you want to add an AGENTS.md file to help AI coding tools understand
Cloudflare APIs?, choose No.

- For Do you want to use git for version control?, choose No.

- For Do you want to deploy your application?, choose No (we will be testing the server before deploying).

Now, you have the MCP server setup, with dependencies installed.

Move into the project folder:
Terminal windowcd remote-mcp-server-authless
In the directory of your new project, run the following command to start the development server:
Terminal windownpm start
â Starting local server...

[wrangler:info] Ready on http://localhost:8788
Check the command output for the local port.

In this example, the MCP server runs on port 8788, and the MCP endpoint URL is http://localhost:8788/mcp.

To test the server locally:
In a new terminal, run the MCP inspector â.

The MCP inspector is an interactive MCP client that allows you to connect to your MCP server and invoke tools from a web browser.

Terminal windownpx @modelcontextprotocol/inspector@latest
ð MCP Inspector is up and running at:
http://localhost:5173/?MCP_PROXY_AUTH_TOKEN=46ab..cd3
ð Opening browser...

The MCP Inspector will launch in your web browser.

You can also launch it manually by opening a browser and going to http://localhost:<PORT>.

Check the command output for the local port where MCP Inspector is running.

In this example, MCP Inspector is served on port 5173.

In the MCP inspector, enter the URL of your MCP server (http://localhost:8788/mcp), and select Connect.

Select List Tools to show the tools that your MCP server exposes.

You can now deploy your MCP server to Cloudflare.

From your project directory, run:
Terminal windownpx wrangler@latest deploy
If you have already connected a git repository to the Worker with your MCP server, you can deploy your MCP server by pushing a change or merging a pull request to the main branch of the repository.

The MCP server will be deployed to your *.workers.dev subdomain at https://remote-mcp-server-authless.your-account.workers.dev/mcp.

To test the remote MCP server, take the URL of your deployed MCP server (https://remote-mcp-server-authless.your-account.workers.dev/mcp) and enter it in the MCP inspector running on http://localhost:5173.

You now have a remote MCP server that MCP clients can connect to.

Connect from an MCP client via a local proxy
Now that your remote MCP server is running, you can use the mcp-remote local proxy â to connect Claude Desktop or other MCP clients to it â even if your MCP client does not support remote transport or authorization on the client side.

This lets you test what an interaction with your remote MCP server will be like with a real MCP client.

For example, to connect from Claude Desktop:
Update your Claude Desktop configuration to point to the URL of your MCP server:
{
"mcpServers": {
"math": {
"command": "npx",
"args": [
"mcp-remote",
"https://remote-mcp-server-authless.your-account.workers.dev/mcp"
]
}
Restart Claude Desktop to load the MCP Server.

Once this is done, Claude will be able to make calls to your remote MCP server.

To test, ask Claude to use one of your tools.

For example:
Could you use the math tool to add 23 and 19?

Claude should invoke the tool and show the result generated by the remote MCP server.

To learn how to use remote MCP servers with other MCP clients, refer to Test a Remote MCP Server.

Add Authentication
The public MCP server example you deployed earlier allows any client to connect and invoke tools without logging in.

To add user authentication to your MCP server, you can integrate Cloudflare Access or a third-party service as the OAuth provider.

Your MCP server handles secure login flows and issues access tokens that MCP clients can use to make authenticated tool calls.

Users sign in with the OAuth provider and grant their AI agent permission to interact with the tools exposed by your MCP server, using scoped permissions.

Cloudflare Access OAuth
You can configure your MCP server to require user authentication through Cloudflare Access.

Cloudflare Access acts as an identity aggregator and verifies user emails, signals from your existing identity providers (such as GitHub or Google), and other attributes such as IP address or device certificates.

When users connect to the MCP server, they will be prompted to log in to the configured identity provider and are only granted access if they pass your Access policies.

For a step-by-step deployment guide, refer to Secure MCP servers with Access for SaaS.

Third-party OAuth
You can connect your MCP server with any OAuth provider that supports the OAuth 2.0 specification, including GitHub, Google, Slack, Stytch, Auth0, WorkOS, and more.

The following example demonstrates how to use GitHub as an OAuth provider.

Step 1 â Create a new MCP server
Run the following command to create a new MCP server with GitHub OAuth:
npm create cloudflare@latest -- my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
yarn create cloudflare my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
pnpm create cloudflare@latest my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
Now, you have the MCP server setup, with dependencies installed.

Move into that project folder:
Terminal windowcd my-mcp-server-github-auth
You'll notice that in the example MCP server, if you open src/index.ts, the primary difference is that the defaultHandler is set to the GitHubHandler:
TypeScriptimport GitHubHandler from "./github-handler";
export default new OAuthProvider({
apiRoute: "/mcp",
apiHandler: MyMCP.serve("/mcp"),
defaultHandler: GitHubHandler,
authorizeEndpoint: "/authorize",
tokenEndpoint: "/token",
clientRegistrationEndpoint: "/register",
});
This ensures that your users are redirected to GitHub to authenticate.

To get this working though, you need to create OAuth client apps in the steps below.

Step 2 â Create an OAuth App
You'll need to create two GitHub OAuth Apps â to use GitHub as an authentication provider for your MCP server âÂ one for local development, and one for production.