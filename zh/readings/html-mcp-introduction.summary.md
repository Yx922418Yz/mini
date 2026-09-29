# 模型上下文协议（MCP）：面向开发者的全面入门（导读）

> 来源：Stytch（作者 Reed McGinley-Stempel，2025-03-28） · 文章 id：`html-mcp-introduction` · 原文约 31.1K 字符

## 核心主张
文章要解决 AI 应用接入外部工具/数据时「每个 API 都写一次性集成」的碎片化问题，主张用开源的 Model Context Protocol（MCP）充当 AI 应用与外部系统之间的「通用适配器」，以一套标准接口替代定制集成代码。MCP 基于 JSON-RPC 2.0、采用客户端-服务器架构，让大语言模型以结构化、安全的方式调用函数、获取数据或使用预定义提示词，并通过 OAuth 2.0 补上了早期缺失的远程认证能力。

## 关键要点（原文引用）
- MCP 是 "a universal adapter between AI applications and external tools or data sources"，类比 USB-C：一套接口连接多种系统；协议 "built on JSON-RPC 2.0"。
- 架构：AI 应用作为 host 运行 MCP client，每个外部集成作为 MCP server；server 暴露 tools（函数）、resources（数据）与 prompts（模板），模型不直接调用 API。
- 列工具请求示例：`{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}`；server 返回带 `name`、`description`、`schema` 的工具，例如 `get_weather`（`"description": "Retrieves weather data."`）。
- 核心收益：Rapid Tool Integration（Google Drive、SQL 数据库等现成 server 即可接入）、Autonomous Agents（示例多步流程：从 CRM 取数 → 发邮件 → 写数据库）、Reduced Friction and Setup、Consistency and Interoperability、Two-Way Context。
- 对比替代方案：MCP 在 Integration Speed（✅ Fast, plug-and-play）、Authentication（✅ OAuth standard）、Interaction Type（✅ Continuous & context-rich）、Open Standard（✅ Yes）上占优；Custom Integrations 为 ❌ Manual API keys，ChatGPT Plugins 为 ⚠️ proprietary 且多为单发调用。
- 与 LangChain 类框架互补：MCP 把标准化推向 "model-facing"，agent 可在运行时发现并使用未提前写进代码的工具；OpenAI 的 function calling 负责生成调用，MCP 负责标准化执行。
- 五步流程：Connect to the MCP Server（stdio 或 remote HTTP stream/SSE，发送 `initialize` 握手）→ Discover Tools（`tools/list`）→ LLM Chooses a Tool（如 `get_current_stock_price(company="AAPL", format="USD")`）→ Invoke via MCP（`tools/call`）→ Return the Result to the LLM（示例结果 "The current stock price of AAPL is $173.22 (USD)."）。
- SDK 调用片段：`const tools = await mcpClient.request({ method: 'tools/list' }, ListToolsResultSchema);` 与 `const result = await mcpClient.request({ method: 'tools/call', params: { name: toolName, arguments: toolArgs } }, CallToolResultSchema);`。
- 早期限制：MCP 于 2024 年末出现时没有标准化认证机制，只能本地运行或用预置 token，难以支撑多用户与云端 agent。
- OAuth 2.0 带来的能力：Dynamic Client Registration (DCR)、Automatic Endpoint Discovery、按用户权限裁剪的 scoped token 与多用户并发支持。
- 调试支持：MCP Inspector（交互式调试工具）与官方 debugging guide。
- 生态与商业动向：Cloudflare 提供部署 remote MCP server 的平台；Stytch 以 `Stytch Connected Apps` 解决 remote MCP server 的认证问题。

## 术语与译法
- `Model Context Protocol` → 模型上下文协议
- `MCP Server` → MCP 服务器
- `Tool Use` → 工具调用
- `Tool Definition` → 工具定义
- `LLM` → 大语言模型
- `Agent` → 智能体
- `Prompt` → 提示词
- `System Prompt` → 系统提示词
- `Permission` → 权限
- `Autonomy` → 自主性
- `Troubleshooting` → 排障
- `Repository` → 仓库

## 结论
MCP 用开放、模型无关的协议统一了 AI 与外部工具/数据的接入方式，并以 OAuth 2.0 补上远程认证这一关键短板。作者认为它很可能成为下一代 AI 应用的基础设施，开发者现在熟悉 MCP 概念、借助它承担工具集成的「管道」工作，正当时。
