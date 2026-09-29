# 多智能体系统与「AI 原生」软件工程（导读）

> 来源：Resolve AI Blog（Resolve AI 官方博客，Technology 分类） · 作者：Spiros Xanthos（Founder and CEO）、Gabor Angeli（Research Engineer）、Bharat Khandelwal（Research Engineer） · 发布 `03/20/2026` · 文章 id：`html-multi-agent-systems-ai-native` · 原文约 14.2K 字符

## 核心主张
生成式 AI 已把"写服务"变成几小时的事，但**理解生产环境出了什么问题依然要跨工具做苦工**：编码智能体接管了构建侧（代码生成、代码审查），生产调试却仍是手工的。作者认为问题不在 AI 能力，而在**我们如何设计 AI 系统**——多数团队只是用 AI 工具把旧流程跑得更快，而没有重新想象软件研发与生产运维端到端该怎么做。文章区分 **AI-Assisted（AI 辅助）** 与 **AI-Native（AI 原生）**，主张只有**有状态的多智能体系统**才能撑起 AI 原生工程，并给出四级能力矩阵与失败原因。

## 关键要点（原文引用）
- 两种范式的流程差异：`AI-Assisted: ... The workflow remains human-centric: Engineer → Systems and tools → Correlation → Action.`（工程师仍在与工具打交道，只是用 AI 更快地完成单个任务）；`AI-Native: AI becomes your primary interface for production work. The workflow becomes AI-led: Engineer → Natural Language Request → AI System → Response / Action.`（工程师设定目标，由智能体承担操作性工作）。
- 以事故响应为例：AI 辅助下你仍在生成假设、判断哪些证据重要、手工跨工具关联信号；AI 原生的做法是智能体自行 `perform real-time triage of investigation priorities, generate competing hypotheses in parallel, and refine theories through successive iterations based on cross-system evidence`。交互方式随之改变：`Instead of asking "Can you analyze these logs?" you say "Resolve this checkout failure" and agents coordinate the entire investigation.`
- 为什么必须是智能体而非工具：`The shift requires persistent AI agents, not just AI tools.`——模型能加速单个任务，但只有**有状态（stateful）**的智能体才能维持调查上下文、跨多工具协同，并自主执行完整事故生命周期中的复杂任务。
- 理论基础 `irreducible interdependence`（不可约的相互依赖）：理解现代生产系统需要跨领域的专门知识，而它们无法被统一进单一模型；`No single AI tool or set of AI models can maintain expert-level knowledge across all these domains while coordinating a real-time investigation.`
- 具体场景：API 延迟在关键事故中飙升 10 倍时，需要**同时**运行的专门智能体：跨 50+ 微服务关联 traces、分析慢查询与连接池耗尽、核查近期部署与基础设施变更、扫描鉴权日志中的安全异常、按当前负载评估自动扩缩函数、结合 SLA 分析支持工单的客户影响。
- **四级能力矩阵（原文表格要点）**：`LLM`（用于解释、分析、文档等单点任务——工程师仍承担大部分操作性工作；受限于"Single-pass generation prone to hallucinations, with no feedback loops or real-world integration"）；`LLM + Tools`（可按命令取数，但关联成本仍压在人类身上；受限于上下文窗口与"no persistent state management across tool interactions"）；`Single Agent`（独立遵循调查流程，但"Sequential investigation, gets stuck on wrong hypotheses without validation"）；`Multi-Agent`（专门智能体并行调查、汇总为统一诊断；代价是"Requires investment in coordination protocols"，分布式智能需要"formal communication schemas and conflict resolution"）。作者结论是"Each level hits a different scalability ceiling"，只有多智能体能突破顺序推理的限制。
- 构建难点——**双重要专长**：`Domain expertise determines architecture`（只有真正在 DevOps/SRE 岗位上凌晨三点调过生产的人，才知道日志模式与指标异常需要根本不同的调查策略；这类决定"aren't AI problems. They're production decisions."）；`AI expertise makes agents work together`（智能体之间的上下文传播是"managing directed acyclic graphs of information flow"，并行编排需要正式的协调协议来避免竞态与死锁，且系统要持续从交互与短暂故障模式中学习——"Get one step wrong in coordinating agents and your system gets progressively worse, not better."）。
- 一句话总结这一交叉：`Domain knowledge without AI architecture is just expensive consulting. AI architecture without domain knowledge produces output that investigates the wrong things.`
- 团队背景与背书：团队含二十年以上生产系统经验的工程师、OpenTelemetry 的共同创造者，以及 Google DeepResearch 与 Gemini Agents 背后的研究者；客户如 Salesforce、Zscaler、Coinbase。文章自述内容曾 `presented our approach to Stanford's graduate AI program`。

## 术语与译法
- `AI-Native Engineering` → AI 原生工程
- `AI-Assisted` → AI 辅助
- `Agent` / `Multi-Agent System` → 智能体 / 多智能体系统
- `Agentic AI` → 智能体式 AI
- `Stateful / Persistent Agent` → 有状态（常驻）智能体
- `Orchestration` → 编排
- `Irreducible Interdependence` → 不可约的相互依赖
- `Context Propagation` → 上下文传播
- `Directed Acyclic Graph` → 有向无环图
- `Race Condition` / `Deadlock` → 竞态 / 死锁
- `Hypothesis` → 假设
- `Triage` → 分诊 / 优先排序
- `MTTR` → 平均修复时长
- `SLA` → 服务等级协议（SLA）
- `Observability` → 可观测性
- `Microservices` → 微服务
- `SRE` → 站点可靠性工程（SRE）
- `OpenTelemetry` → OpenTelemetry（保留原文）

## 结论
本文是 C1 阅读材料中**理论密度最高**的一篇：它把「AI 原生」从口号落成可判定的流程差异（谁是与系统对话的主语），再用 `irreducible interdependence` 说明为什么单模型、单智能体在规模上必然撞墙，最后用双专长（领域 × AI 工程）解释为什么多智能体系统难做。对 C1 的价值在于：它同时提供了**概念框架**（辅助 vs 原生、四级矩阵）与**失败模式清单**（幻觉、无状态、顺序推理瓶颈、协调协议缺失），可直接支撑译文质量与 AAR 中关于「AI 协作边界」的讨论。

