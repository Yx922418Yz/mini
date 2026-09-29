# 为智能体编写高效工具——用智能体的方式来写（导读）

> 来源：Engineering at Anthropic（作者 Ken Aizawa） · 文章 id：`html-writing-effective-tools-for-agents` · 原文约 22.0K 字符

## 核心主张
这篇 Anthropic 工程博客（发布于 `Sep 11, 2025`）指出：智能体的能力上限取决于我们给它什么工具（Agents are only as effective as the tools we give them）。作者主张不要凭直觉设计工具，而要用智能体本身来迭代工具：先做原型，再构建评估（evaluation），用智能体跑真实任务、分析原始轨迹，据此不断优化工具定义与实现。其核心方法论是「以智能体为中心的评估驱动设计」。

## 关键要点（原文引用）
- 基本判断：agents 只能和其工具一样有效——工具设计直接决定智能体表现。
- 工具可能被以 MCP 形式暴露，数量可达数百个，因此命名与结构至关重要。
- 实践流程：先做原型（prototype），再构建测试与评估，用智能体运行真实任务来验证。
- 用智能体创建并运行评估（create/run evals with agents），可与 `Claude Code` 协作来优化工具。
- 评估设计要点：验证器（verifier）不应仅因表达不同就拒绝语义正确的答案，需容忍合理的替代措辞。
- 可构建程序化的智能体循环（programmatic agentic loops），批量收集推理过程、反馈与 chain-of-thought（CoT）。
- 需要采集的指标至少包括：accuracy、runtime、call count、tokens、tool errors。
- 工具返回应只保留高信号信息（high signal information），减少无关上下文。
- 令牌效率可通过分页（pagination）、范围（range）、过滤（filter）、截断（truncation）来实现。
- 命名应避免无意义 token：不推荐 `uuid`、`256px_image_url`、`mime_type`；推荐 `name`、`image_url`、`file_type`。
- 用命名空间（namespacing）减少歧义，如 `asana_search`、`jira_search`、`asana_projects_search`、`asana_users_search`。
- 返回格式可按场景切换，原文示例代码：`enum ResponseFormat { DETAILED = "detailed", CONCISE = "concise" }`（DETAILED 约 `206` tokens，CONCISE 约 `72` tokens）。

## 术语与译法
- `Model Context Protocol` → 模型上下文协议
- `MCP Server` → MCP 服务器
- `Tool Use` → 工具调用
- `Tool Definition` → 工具定义
- `Agent` → 智能体
- `Coding Agent` → 编码智能体
- `Evaluation` → 评估
- `Benchmark` → 基准测试
- `Token` → 词元
- `Context Window` → 上下文窗口
- `Prompt` → 提示词
- `Hallucination` → 幻觉
- `Latency` → 延迟

## 结论
编写高效工具的关键不是拍脑袋设计，而是以评估为闭环、让智能体参与验证与迭代；在命名、返回格式与令牌效率上做对取舍，才能在 MCP 生态中真正放大智能体的能力。
