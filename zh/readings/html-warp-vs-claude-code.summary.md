# Warp vs Claude Code（导读）

> 来源：Warp 官方站点 · 文章 id：`html-warp-vs-claude-code` · 原文约 3.7K 字符

## 定位
Warp 自称**「Agentic Development Environment（智能体开发环境）」**——把现代终端与强大的智能体结合，帮助用户构建、测试、部署与调试代码。Warp 的 AI 由 **Oz**（面向云端智能体的编排平台）驱动。

## Warp 的核心能力
- **Agent Modality**：在"纯命令终端"与"多轮智能体会话视图"之间切换。
- **现代终端体验**：光标移动、块（block）导航、多行编辑、语法高亮、富补全，用 **Rust** 构建、性能高。
- **代码编辑器**：文件树、支持 **LSP** 的编辑器、交互式代码评审体验。
- **编码智能体集成**：语音输入、`@` 选择（配合终端内图片），兼容 Oz 或 **Claude Code、Codex** 等智能体。

## Oz：面向云端智能体的编排平台
Oz 支持多模型（multi-model by design），可按任务选择最合适的 LLM，运行于两种模式：
- **本地智能体（Local agents）**：直接在 Warp 应用内运行，实时交互式编码；可编写/重构代码、调试修错、运行命令并解读结果、规划并执行多步任务。**用户始终掌控**——可审查改动、中途干预、执行前批准动作。
- **云端智能体（Oz Cloud Agents）**：在 Warp（或自有）基础设施后台运行，用于规模化自动化。支持 **Triggers**（Slack / Linear / GitHub / 自定义 webhook 事件）、**Schedules**（依赖更新、死代码清理等周期任务）、**Parallelism**（跨仓库/任务并发）、**Observability**（每次运行可追踪、可审计、可共享）。适合 PR 评审、issue 分诊、例行维护等无需即时关注的工作。

## 协作与安全
- **协同体验**：同一套智能体能力本地/云端通用；可从云端发起任务再本地接手（不丢进度与上下文）；**Warp Drive、Rules、MCP servers** 在本地与云端共享；支持共享会话、审查动作、干预运行中的任务。
- **隐私与安全**：Warp 符合 **SOC 2**，与所有签约 LLM 供应商实行**零数据保留（Zero Data Retention）**策略，不保留/存储/用于训练客户 AI 数据；可在 **Settings > AI** 全局关闭 AI 功能。

> 注：标题中的"vs Claude Code"在此页面指 Warp 环境与 Claude Code 等编码智能体**共存/兼容**（可作为编码智能体接入 Warp），而非逐项功能对比。
