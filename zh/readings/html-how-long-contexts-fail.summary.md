# 长上下文如何失效（导读）

> 来源：Drew Breunig（原文发布日期 Jun 22, 2025；tags：AGENTS / LLM / AI / PROMPTING / CONTEXT MANAGEMENT）· 文章 id：`html-how-long-contexts-fail` · 原文约 10.1K 字符

## 核心主张
随着前沿模型的上下文窗口（Context Window）增长到上百万 token，人们误以为只要把所有工具、文档与指令一股脑塞进提示词就能得到更强的智能体。本文反驳这一乐观假设：更长的上下文并不会带来更好的回答，反而会以出人意料的方式让智能体与应用失效。作者归纳出四类上下文失效：Context Poisoning（污染）、Context Distraction（分心）、Context Confusion（混淆）、Context Clash（冲突），并主张「Managing Your Context is the Key to Successful Agents」。

## 关键要点（原文引用）
- 正文开篇即定义四种失效：Context Poisoning: When a hallucination makes it into the context；Context Distraction: When the context overwhelms the training；Context Confusion: When superfluous context influences the response；Context Clash: When parts of the context disagree。
- Context Poisoning：当幻觉（hallucination）或其他错误进入上下文并被反复引用时发生。Gemini 2.5 在玩 Pokémon 时偶尔产生幻觉并污染上下文；一旦「goals」部分被污染，智能体会发展出无意义的策略、执着于无法达成的目标，且往往要很久才能恢复。
- Context Distraction：上下文增长到过长时，模型过度聚焦上下文而忽略训练所学。Gemini 2.5 Pro 支持 1M+ token 上下文，但在 context 显著超过 100k tokens 后，智能体倾向于重复海量历史中的动作，而非合成新计划。
- 对于较小的模型，分心上限更低：Databricks 的研究发现模型正确率在 Llama 3.1 405b 上约 32k 就开始下降，更小的模型则更早。
- Context Confusion：上下文中多余的内容会被模型用于生成低质量回答。Berkeley Function-Calling Leaderboard（现已第 3 版）显示，提供超过一个工具（more than one tool）时每个模型表现都更差，而且所有模型偶尔会调用并不相关的工具。
- 一个突出例子来自 GeoEngine 基准测试（含 46 种不同工具）：给量化（compressed）的 Llama 3.1 8b 提供全部 46 个工具时它失败了——尽管上下文远在 16k 窗口之内；而只给 19 个工具时它成功了。
- 「if you put something in the context the model has to pay attention to it」：哪怕是无关信息或多余的工具定义，模型也会将其纳入考量。
- Context Clash：新加入的信息或工具与上下文中已有信息相冲突。Microsoft 与 Salesforce 团队把多个 benchmark 的提示词「sharded」成多轮对话式输入，结果平均下降 39%，OpenAI 的 o3 得分从 98.1 跌到 64.1。
- 该论文指出模型常在早期轮次做出假设并过早给出最终解，一旦「take a wrong turn in a conversation, they get lost and do not recover」；错误的历史回答残留在上下文中，持续影响最终答案。
- 对智能体构建者尤为重要：智能体从文档、tool calls 以及其他负责子问题的模型处汇集上下文，这些来源彼此可能互相冲突；接入自己没编写的 MCP 工具时，其描述与指令更可能和提示词的其余部分 clash。
- 作者指出后续文章「How to Fix Your Context」将给出缓解/规避手法，例如 dynamically loading tools 与 context quarantines。

## 术语与译法
- `Context Window` → 上下文窗口
- `Long-context` → 长上下文
- `Token` → 词元
- `Hallucination` → 幻觉
- `Agent` → 智能体
- `Tool Use` → 工具调用
- `Benchmark` → 基准测试
- `MCP Server` → MCP 服务器
- `Retrieval-Augmented Generation` → 检索增强生成

## 结论
更大的上下文引入了新的失效模式：污染会累积并复利，分心让智能体重复旧动作，混淆导致无关的工具或文档被使用，冲突制造内部矛盾并破坏推理。这些失效对智能体打击最大，因为智能体恰好处在上下文膨胀的场景中——多来源汇集、连续工具调用、多轮推理与不断累积的历史。
