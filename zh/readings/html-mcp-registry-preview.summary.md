# MCP Registry 预览发布（导读）

> 来源：MCP 官方公告 · 文章 id：`html-mcp-registry-preview` · 原文约 5.3K 字符

## 核心事件
发布 **Model Context Protocol（MCP）Registry**——一个面向**公开可用的 MCP 服务器**的开放目录与 API，用于改善"可发现性"与"可接入性"。通过标准化服务器的分发与发现方式，扩大服务器触达范围，让客户端更容易连接。**目前为预览（preview）阶段**。

## 关键设计
- **单一事实来源（Single source of truth）**：官方注册表地址为 `https://registry.modelcontextprotocol.io`。作为 MCP 项目的一部分，Registry 及其父级 **OpenAPI 规范**均为开源，任何人可构建兼容的子注册表（sub-registry）。
- **公有 / 私有子注册表**：
  - *公有子注册表*：与各 MCP 客户端绑定的"MCP 应用市场"可对上游数据做增强与取舍，以不同画像的用户需求为导向。
  - *私有子注册表*：面向有严格隐私/安全要求的企业，Registry 提供单一上游数据源；至少会共享 API schema，使 SDK 与工具链可跨生态复用。
  - 两者之上，Registry 都是**起点**：服务器维护者在此发布并维护自报信息，下游消费方再加工并交付给最终用户。
- **社区驱动的审核机制**：Registry 由 registry working group 维护、采用宽松许可。社区成员可提交 issue 标记违规服务器（垃圾信息、恶意代码、仿冒合法服务等），维护者可**拉黑（denylist）**并追溯性地将其从公开访问中移除。

## 上手与免责
- 服务器维护者：按《Adding Servers to the MCP Registry》指南添加服务器。
- 客户端维护者：按《Accessing MCP Registry Data》指南接入数据。
- 预览版旨在正式发布（GA）前改进体验，**不提供数据持久性保证或其他担保**；建议关注开发进展，GA 前可能发生破坏性变更。

## 致谢
项目自 2025 年 2 月作为草根项目起步：MCP 作者 **David Soria Parra** 与 **Justin Spahr-Summers** 请 PulseMCP 与 Goose 团队协助建设社区注册表；PulseMCP 的 **Tadas Antanavicius** 牵头，与 Block 的 **Alex Hancock** 合作，随后 GitHub 的 MCP 负责人 **Toby Padilla**、Anthropic 的 **Adam Jones** 加入。初始公告列出**来自至少 9 家公司、共 16 位贡献者**，另有 Stacklok、GitHub、VS Code、NuGet、Last9、Microsoft 及 Anthropic/GitHub 众多同事参与代码评审与开发。
