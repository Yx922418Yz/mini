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

Step 2.1 â Create a new OAuth App for local development
Navigate to github.com/settings/developers â to create a new OAuth App with the following settings:
Application name: My MCP Server (local)
Homepage URL: http://localhost:8788
Authorization callback URL: http://localhost:8788/callback
For the OAuth app you just created, add the client ID of the OAuth app as GITHUB_CLIENT_ID and generate a client secret, adding it as GITHUB_CLIENT_SECRET to a .env file in the root of your project, which will be used to set secrets in local development.

Terminal windowtouch .env
echo 'GITHUB_CLIENT_ID="your-client-id"' >> .env
echo 'GITHUB_CLIENT_SECRET="your-client-secret"' >> .env
cat .env
Run the following command to start the development server:
Terminal windownpm start
Your MCP server is now running on http://localhost:8788/mcp.

In a new terminal, run the MCP inspector â.

The MCP inspector is an interactive MCP client that allows you to connect to your MCP server and invoke tools from a web browser.

Terminal windownpx @modelcontextprotocol/inspector@latest
Open the MCP inspector in your web browser:
Terminal windowopen http://localhost:5173
In the inspector, enter the URL of your MCP server, http://localhost:8788/mcp
In the main panel on the right, click the OAuth Settings button and then click Quick OAuth Flow.

You should be redirected to a GitHub login or authorization page.

After authorizing the MCP Client (the inspector) access to your GitHub account, you will be redirected back to the inspector.

Click Connect in the sidebar and you should see the "List Tools" button, which will list the tools that your MCP server exposes.

Step 2.2 â Create a new OAuth App for production
You'll need to repeat Step 2.1 to create a new OAuth App for production.

Navigate to github.com/settings/developers â to create a new OAuth App with the following settings:
Application name: My MCP Server (production)
Homepage URL: Enter the workers.dev URL of your deployed MCP server (ex: worker-name.account-name.workers.dev)
Authorization callback URL: Enter the /callback path of the workers.dev URL of your deployed MCP server (ex: worker-name.account-name.workers.dev/callback)
For the OAuth app you just created, add the client ID and client secret, using Wrangler CLI:
Terminal windownpx wrangler secret put GITHUB_CLIENT_ID
Terminal windownpx wrangler secret put GITHUB_CLIENT_SECRET
npx wrangler secret put COOKIE_ENCRYPTION_KEY # add any random string here e.g.

openssl rand -hex 32
Set up a KV namespace
a.

Create the KV namespace:
Terminal windownpx wrangler kv namespace create "OAUTH_KV"
b.

Update the wrangler.jsonc file with the resulting KV ID:
{
"kvNamespaces": [
{
"binding": "OAUTH_KV",
"id": "<YOUR_KV_NAMESPACE_ID>"
}
]
}
Deploy the MCP server to your Cloudflare workers.dev domain:
Terminal windownpm run deploy
Connect to your server running at worker-name.account-name.workers.dev/mcp using the AI Playground â, MCP Inspector, or other MCP clients, and authenticate with GitHub.

Next steps
MCP Tools Add tools to your MCP server.

Authorization Customize authentication and authorization.