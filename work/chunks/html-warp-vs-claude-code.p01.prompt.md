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

Warp is an Agentic Development Environment, a modern terminal combined with powerful agents that help you build, test, deploy, and debug code. Warp's AI is powered by Oz, the orchestration platform for cloud agents.
Warp combines a modern terminal with Oz, the orchestration platform for cloud agents
Warp
Warp is where you work — a fast, modern terminal built for coding with agents.
Key capabilities:
Agent Modality : Switch between a clean terminal for commands and a dedicated conversation view for multi-turn agent workflows.
Modern terminal UX: Cursor movement, block-based navigation, multi-line editing, syntax highlighting, and rich completions. Built with Rust for high performance.
Code editor: File tree, code editor with LSP support, and interactive code review experience.
Coding agent integrations : Features like voice input, and @-selection for working with terminal based images. Compatible with Oz or agents like Claude Code and Codex.
Deep dive into Warp's core features
Oz: The orchestration platform for cloud agents
Oz is the orchestration platform for cloud agents that powers all of Warp's intelligent features. Oz is designed to coordinate agents at scale—understanding your codebase, executing tasks autonomously, and adapting to your workflows. Oz is multi-model by design, giving you flexibility to choose the best LLM for each task.
Oz operates in two modes:
Local agents
Run directly in the Warp app for real-time, interactive coding assistance.
Write and refactor code across your codebase
Debug issues and fix errors
Run commands and interpret results
Plan and execute multi-step tasks
Local agents keep you in control. You can review changes, steer the agent mid-task, and approve actions before they execute.
→ Get started with local agents
Cloud agents
Oz Cloud Agents run in the background on Warp's infrastructure (or your own) for automation at scale.
Triggers: React to events from Slack, Linear, GitHub, or custom webhooks
Schedules: Run recurring tasks like dependency updates or dead code removal
Parallelism: Run many agents concurrently across repos or tasks
Observability: Every run is tracked, auditable, and shareable with your team
Cloud agents are ideal for work that doesn't need your immediate attention, like PR reviews, issue triage, routine maintenance, and integration-driven workflows.
→ Learn about cloud agents
How they work together
Warp and Oz provide a unified experience across local and cloud development:
Same agent, anywhere: Whether you're working interactively in Warp or running agents in the cloud, you're using the same underlying agent capabilities.
Seamless handoff: Start a task in the cloud and take over locally in Warp when you want hands-on control, without losing progress or context.
Shared context: Warp Drive, Rules , and MCP servers work across both local and cloud agents, so your team's knowledge and tools are always available.
Team collaboration: Share agent sessions, review agents' actions, and steer running tasks, regardless of who started them.
Multi-model support
Oz is multi-model by design. You can choose your preferred LLM from a curated set of top models.
Privacy and security
Warp is SOC 2 compliant and has Zero Data Retention policies with all contracted LLM providers. No customer AI data is retained, stored, or used for training.
Warp's AI features can be globally disabled in Settings > AI.
→ Read more about data privacy
Next steps
Quickstart Guide: Get Warp installed and start coding
Local Agents Overview : Explore all AI features available in Warp
Cloud Agents Overview : Set up background automation
Oz Platform : Learn about the CLI, API, SDK, and infrastructure
NextQuickstart
Last updated 3 days ago
Was this helpful?