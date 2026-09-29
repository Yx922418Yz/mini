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

Experiment#
From each haystack topic (PG essays and arXiv papers), we take a needle with high needle-question similarity (second highest out of eight), and manually write 4 distractors:
Question: "What was the best writing advice I got from my college classmate?"
Needle: "I think the best writing tip I received from my college classmate was to write every week."
Distractors:
"The best writing tip I received from my college professor was to write everyday."
"The worst writing advice I got from my college classmate was to write each essay in five different styles."
"The best writing advice I got from my classmate was to write each essay in three different styles, this was back in high school."
"I thought the best writing advice I got from my college classmate was to write each essay in four different styles, but not anymore."
Distractors for Paul Graham Essay Topic & Needle with High Needle-Question SimilarityInstead of testing all eight needles with distractors, we use one needle with high needle-question similarity to create a condition in which the needle should be relatively easy to identify.

We see from previous results that models generally perform well on this needle across input lengths due to high needle-question similarity, which allows us to better isolate and measure the impact of distractors alone.

We run three test conditions:
No distractors (baseline): Needle only
Single distractor: Needle + one distractor (randomly positioned)
Multiple distractors: Needle + all four distractors, randomly positioned throughout the haystack
Impact of Distractors - Three Conditions
Results#
Even a single distractor reduces performance relative to the baseline (needle only), and adding four distractors compounds this degradation further.

Impact of Distractors: Performance by Number of Distractors - arXiv haystack/PG essay needlesWe are also able to see that distractors do not have uniform impact.

For example, in our arXiv haystack and PG essay needle combination, we can see that distractor 3 (red) causes greater performance decline relative to the other distractors.

Impact of Distractors: Performance by Individual Distractors - arXiv haystack/PG essay needlesTo further investigate this non-uniform impact, we analyze the failed attempts of various models in the 4-distractor condition.

For the arXiv haystack and PG essay needle combination, we see that distractors 2 and 3 appear most frequently in hallucinated responses across models.

Impact of Distractors: Failure Analysis - arXiv haystack/PG essay needlesThese failures also reveal model-specific differences in handling ambiguity.

Claude models consistently exhibit the lowest hallucination rates.

Specifically, Claude Sonnet 4 and Opus 4 are particularly conservative and tend to abstain when uncertain, explicitly stating that no answer can be found.

In contrast, GPT models show the highest rates of hallucination, often generating confident but incorrect responses when distractors are present.

Needle-Haystack Similarity#
In long-context tasks, irrelevant context is often treated as a neutral placeholder to scale up input length.

It’s typically assumed that the content of this irrelevant context doesn't matter, as long as it doesn’t directly interfere with the task.

However, a natural question arises: does the needle-haystack similarity influence task difficulty at all?

Intuitively, if the needle blends in with the content of the haystack, the model may have greater difficulty in extracting the needle.

Our findings reveal that needle-haystack similarity has a non-uniform effect on model performance.

Experiment#
Using the needles from our needle-question similarity experiment, we set up our experiment to test the impact of needle-haystack similarity.

We measure needle-haystack similarity by embedding the haystack and retrieving the top five most similar chunks for each needle, then averaging their cosine similarity scores.

This process is repeated across five different embedding models for robustness.

In the PG essay haystack, PG essay needles have an average needle-haystack similarity score of 0.529 with a variation of 0.101, while arXiv needles average 0.368 needle-haystack similarity with a variation of 0.111.

Conversely, in the arXiv haystack, arXiv needles average 0.654 needle-haystack similarity with a variation of 0.0858, whereas PG-essay needles score lower at 0.394 needle-haystack similarity with a variation of 0.105.

On each haystack, we test semantically similar needles against unrelated needles.

For instance, we place both PG essay and arXiv needles within a Paul Graham essay haystack to compare the two conditions:
Needle-Haystack Similarity: Experimental Setup
Results#
We test both PG essay and arXiv needles in two haystack types: Paul Graham essays and arXiv papers.

In the Paul Graham essay haystack, arXiv needles perform significantly better relative to the PG essay needles; in other words, models perform better when the needle does not semantically blend in with its haystack.

In the arXiv haystack, however, we observe only minimal performance differences between our arXiv and PG essay needles.

Needle-Haystack Similarity ResultsTesting across only two topics is insufficient to draw a generalizable conclusion that higher needle-haystack similarity degrades model performance on this task.

This does highlight, however, the non-uniform nature of long-context processing.

Even when task structure and needle-question similarity are held constant, changing the semantic similarity between the needle and the haystack can influence results.

This points to an underexplored area in long-context benchmarks and a meaningful direction for future research.

Haystack Structure#
Aside from needle-haystack similarity, we also consider the structural pattern of the haystack.

If the haystack is composed of coherent essays, a randomly inserted needle may disrupt the logical flow of ideas, making it more noticeable.

In contrast, in a shuffled haystack of randomly ordered sentences, the needle may blend in more easily since the overall context lacks structure.

This follows the assumption that models are sensitive to the logical flow of context—processing it in a structured, order-sensitive manner.

Surprisingly, we find that structural coherence consistently hurts model performance.

Although it seems counterintuitive, models perform worse when the haystack preserves a logical flow of ideas.

Shuffling the haystack and removing local coherence consistently improves performance.

Experiment#
To assess the impact of haystack structure, we create two variants:
Original: preserves the natural flow of ideas within each excerpt
Shuffled: sentences are randomly reordered throughout the haystack to maintain the same overall topic but without logical continuity
Haystack Structure: Sample Experimental Setup
Results#
Across all 18 models and needle-haystack configurations, we observe a consistent pattern that models perform better on shuffled haystacks than on logically structured ones.

Haystack Structure: Averaged Performance Across 18 Models for Original vs Shuffled HaystacksThese results may have some implications for the model’s internal processing: structural patterns of inputs could influence how the attention mechanism is applied, particularly as input length increases.

While out of scope for this report, this points to a potential direction for interpretability research in how attention is influenced by input structure.

Understanding these structural influences that arise with increased input length could help explain these long context failure patterns.

LongMemEval#
To evaluate these models in a more realistic setting, we use LongMemEval, a long-context benchmark for conversational question-answering.

Using long inputs for chat assistants is a common approach for maintaining relevant history for subsequent chats.

To incorporate “memory” into a chat assistant, a naive approach would be to include the full chat history into the prompt for following chats.

This requires the model to perform two tasks, typically performed in one call: find relevant parts of the conversation history (retrieval), then synthesize them in a way that is useful to an incoming query (reasoning).

In an ideal case, the model would be given only the relevant parts so it can focus solely on reasoning.

Adding irrelevant context adds the additional step of identifying what is relevant, forcing the model to perform two tasks simultaneously.

We systematically test the effect of adding this additional step with increased input length through two conditions:
Focused input, containing only the relevant parts and so the model just has to do simple reasoning.

Full input, which utilizes the full 113k token LongMemEval input that includes irrelevant context.

In this case, the model has to perform retrieval across the long context in addition to reasoning.