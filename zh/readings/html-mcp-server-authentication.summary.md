# 在 Cloudflare 上构建远程 MCP 服务器（导读）

> 来源：Cloudflare（官方开发文档，remote MCP server 指南） · 文章 id：`html-mcp-server-authentication` · 原文约 12.2K 字符

## 核心主张
文章要解决「如何把 MCP server 从本地脚本变成可被任意 MCP client 连接的远程服务」这一问题，给出在 Cloudflare Workers 上用 Streamable HTTP transport 部署 remote MCP server 的完整路径。作者主张把服务器放在 Cloudflare 平台上即可获得全球分布式部署、零运维与按需扩展，并区分两条路线：无认证（authless）与带认证/授权（auth/authz），后者通过 GitHub OAuth 与 KV 存储实现。

## 关键要点（原文引用）
- 远程 MCP server 让任何支持 MCP 的客户端（如 Claude、Cursor、ChatGPT）通过 URL 连接，服务器可选择本地、云端或自托管部署。
- 两条路径：authless server（任何人可用，用 URL `remote-mcp-server-authless.your-account.workers.dev/mcp` 连接）与 authenticated server（需 OAuth 授权并支持按 scope 限定工具访问）。
- 脚手架命令：`npm create cloudflare@latest -- remote-mcp-server`（从官方模板创建项目）。
- 三种实现方式（Agents SDK）：`createMcpHandler()`——无状态、无需 Durable Objects，适合简单无状态 server；`McpAgent`——有状态、需要 Durable Objects，适合会话/状态场景；原始 `WebStandardStreamableHTTPServerTransport`——完全控制但无内置辅助。
- MCP server 定义工具，LLM/agent 据此决定可调用哪些工具；文章给出 `init()` 与 `this.server.tool(...)` 定义示例。
- 部署可用 CLI `npm run deploy`，也可在 Cloudflare dashboard 中创建与部署。
- 认证配置向 Wrangler 写入密钥：`npx wrangler secret put GITHUB_CLIENT_ID`、`npx wrangler secret put GITHUB_CLIENT_SECRET`、`npx wrangler secret put COOKIE_ENCRYPTION_KEY # add any random string here e.g. openssl rand -hex 32`。
- 用 KV 存 OAuth 状态：`npx wrangler kv namespace create "OAUTH_KV"`，并在 `wrangler.jsonc` 中配置 `"binding": "OAUTH_KV"` 与 `"id": "<YOUR_KV_NAMESPACE_ID>"`。
- GitHub OAuth App 的回调地址形如 `worker-name.account-name.workers.dev/callback`；客户端连接到 `worker-name.account-name.workers.dev/mcp` 后经 OAuth 流程授权。
- 无 OAuth 的 MCP server 用 `this.props` 读取声明，带认证的 server 可从 `this.props` 获取用户信息与 scopes，并据此限制可调用的工具。
- 调试可用 MCP Inspector；服务器日志可用 `npx wrangler tail` 实时查看。

## 术语与译法
- `MCP Server` → MCP 服务器
- `Agent` → 智能体
- `Tool Use` → 工具调用
- `Tool Definition` → 工具定义
- `Permission` → 权限
- `Repository` → 仓库

## 结论
把 MCP server 部署到 Cloudflare Workers 是让 AI 客户端「即插即用」接入自定义工具的低成本方式：无需认证时可分钟级上线，需要多用户安全访问时则用 GitHub OAuth + KV 补齐认证与授权。选型上，简单场景用 `createMcpHandler()`，需要会话状态时用 `McpAgent`，追求完全控制则用原始 transport。
