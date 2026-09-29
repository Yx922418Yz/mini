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

Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context.

arXiv preprint arXiv:2403.05530.

Link
[4] OpenAI, Kumar, A., Yu, J., Hallman, J., Pokrass, M., Goucher, A., Ganesh, A., Cheng, B., McKinzie, B., Zhang, B., Koch, C., et al.

(2025).

Introducing GPT-4.1 in the API.

Link
[5] Meta AI, (2025).

The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation.

Link
[6] Modarressi, A., Deilamsalehy, H., Dernoncourt, F., Bui, T., Rossi, R.

A., Yoon, S., and Schütze, H.

(2025).

NoLiMa: Long-Context Evaluation Beyond Literal Matching.

arXiv preprint arXiv:2502.05167.

Link
[7] Fu, H.

Y., Shrivastava, A., Moore, J., West, P., Tan, C., and Holtzman, A.

(2025).

AbsenceBench: Language Models Can't Tell What's Missing.

arXiv preprint arXiv:2506.11440.

Link
[8] Vodrahalli, K., Ontanon, S., Tripuraneni, N., Xu, K., Jain, S., Shivanna, R., Hui, J., Dikkala, N., Kazemi, M., Fatemi, B., et al.

(2024).

Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries.

arXiv preprint arXiv:2409.12640.

Link
[9] openai.

(2025).

mrcr [Dataset].

Hugging Face.

Link
[10] openai.

(2025).

graphwalks [Dataset].

Hugging Face.

Link
[11] Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N., and Zhou, D.

(2023).

Large Language Models Can Be Easily Distracted by Irrelevant Context.

arXiv preprint arXiv:2302.00093.

Link
[12] jamescalam.

(2024).

ai-arxiv2 [Dataset].

Hugging Face.

Link
[13] Peng, B., Quesnelle, J., Fan, H., and Shippole, E.

(2023).

YaRN: Efficient Context Window Extension of Large Language Models.

arXiv preprint arXiv:2309.00071.

Link
[14] McInnes, L., Healy, J., and Melville, J.

(2020).

UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction.

arXiv preprint arXiv:1802.03426.

Link
[15] Campello, R.

J.

G.

B., Moulavi, D., and Sander, J.

(2013).

Density-Based Clustering Based on Hierarchical Density Estimates.

In Pei, J., Tseng, V.

S., Cao, L., Motoda, H., and Xu, G.

(Eds.), Advances in Knowledge Discovery and Data Mining (PAKDD 2013), Lecture Notes in Computer Science, vol 7819.

Springer, Berlin, Heidelberg.

Link
Appendix#
Cleaned LongMemEval datasets and needles/distractors used can be downloaded here.

LLM judge alignment:#
We employ LLM judges to evaluate outputs for our NIAH and LongMemEval experiments.

These judges are calibrated to human judgment through the following process:
A subset of model outputs are manually labeled as incorrect/correct (~500 outputs for NIAH, ~600 outputs for LongMemEval)
GPT-4.1 is used to label the same subset of model outputs as incorrect/correct.

An alignment score is calculated by measuring the proportion of human-model aligned judgements.

The prompt is iterated on based on manual inspection of misalignments.

Steps 2-4 are repeated until an alignment score > 0.99 is achieved.

Models Tested#
Not all 18 models are included in each experiement due to context window or thinking_budget constraints.

Anthropic#
Claude Opus 4
Claude Sonnet 4
Claude Sonnet 3.7
Claude Sonnet 3.5
Claude Haiku 3.5
OpenAI#
o3
GPT-4.1
GPT-4.1 mini
GPT-4.1 nano
GPT-4o
GPT-4 Turbo
GPT-3.5 Turbo
Google#
Gemini 2.5 Pro
Gemini 2.5 Flash
Gemini 2.0 Flash
Alibaba#
Qwen3-235B-A22B
Qwen3-32B
Qwen3-8B
Embedding Models Used#
text-embedding-3-small
text-embedding-3-large
jina-embeddings-v3 (input_type='text-matching')
voyage-3-large (input_type=None)
all-MiniLM-L6-v2
Needle-Question Similarity#
Note: thinking/non-thinking modes of the same model are treated separately
Needle-Question Similarity - arXiv haystack/PG essay needles
Needle-Question Similarity - PG essay haystack/PG essay needles
Needle-Question Similarity - PG essay haystack/arXiv needlesAs mentioned in our Needle-Haystack Similarity results, we note this one occurance in which models perform exceptionally well compared to the other needle-haystack combinations.

On its own, it may seem that the high performance models have uniform performance.

However, such uniformity for these models does not hold across the rest of the experiments.

Impact of Distractors#
Impact of Distractors: Performance by Number of Distractors - arXiv haystack/arXiv needles
Impact of Distractors: Performance by Individual Distractors - arXiv haystack/arXiv needles
Impact of Distractors: Performance by Number of Distractors - PG essay haystack/PG essay needles
Impact of Distractors: Performance by Individual Distractors - PG essay haystack/PG essay needles
Impact of Distractors: Performance by Number of Distractors - PG essay haystack/arXiv needles
Impact of Distractors: Performance by Individual Distractors - PG essay haystack/arXiv needles
Impact of Distractors: Failure Analysis - arXiv haystack/arXiv needles
Impact of Distractors: Failure Analysis - PG essay haystack/PG essay needles
Impact of Distractors: Failure Analysis - PG essay haystack/arXiv needles
Repeated Words#
Repeated Words: Position Accuracy - GPT Family
Repeated Words: Position Accuracy - Gemini Family
Repeated Words: Position Accuracy - Qwen Family
Repeated Words: Word Count Difference - GPT Family
Repeated Words: Word Count Difference - Gemini Family
Repeated Words: Word Count Difference - Qwen Family
© 2026
Product
DatabaseSyncEnterprisePackage Search MCPDocsStatusContact
Follow
GitHubXYouTube
Company
AboutChangelogCareers
Legal
PrivacyTermsSecurity