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

AI-Assisted Assessment of Coding Practices in Modern Code Review
AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
Figure 3: Example comment posted by AutoCommenter.
4
DEPLOYMENT
We deployed AutoCommenter to all developers at Google over a
period of time between July 2022 and October 2023:
• until Jul. 2022—teamfooding: this paper’s authors.
• Jul. 2022—early adopters: around 3 thousand volunteers.
• Jul. 2023—A/B experiment: about half of all developers.
• since Oct. 2023—general availability: all developers.
Note that due to industrial confidentiality reasons we are unable
to disclose absolute numbers of code reviews, developers, files,
comments, or distribution of duration of code reviews. We report
on relative measures, where appropriate, and relevant trends.
We continuously evaluated and improved the performance of
AutoCommenter, using an iterative refinement approach:
• Evaluation on historical data (section 3.3) to get directional
insight into how well the model does at the task and to define
thresholds and select a decoding strategy.
• Monitoring and analysis of user interaction and direct feed-
back through feedback buttons and issue reports.
• Targeted human evaluation based on patterns observed dur-
ing other evaluation steps.
Figure 4 shows the ratio of positive to negative developer feed-
back on posted code review comments and IDE diagnostics over
time. The dashed line shows the total count of feedback clicks de-
velopers provided per month. As is expected, this count is much
lower during the early-adopter stage. Additionally, the volatility is
higher in this stage because we actively refined AutoCommenter.
Recall the three feedback buttons within the code review system
(figure 3), which allow developers to express positive and negative
sentiment about a posted comment. We consider comments with a
thumbs up or “Please fix” as positive, and comments with a thumbs
down as negative; we define the useful ratio as the ratio of positive
comments to all comments with feedback.
The remainder of this section describes specific observations
and corresponding refinements that we made during deployment.
4.1
Selecting Threshold and Decoding Strategy
4.1.1
Threshold. During initial deployment we wanted to carefully
manage the trust developers had in AutoCommenter and started
with a high confidence threshold of 𝑡= 0.98. We manually sampled
Figure 4: Developer feedback throughout deployment.
several hundred results and observed that around 80% of predictions
below the threshold were still correct—that is, the false-negative
rate was very high at 𝑡= 0.98. Additionally, we observed that
predictions in Python showed a significantly different distribution
of confidence scores, which were disproportionately impacted by
thresholding. We conjecture that the training dataset composition
(number of distinct URLs and URL frequencies) and specificity of the
best practice documents are reasons, but leave a deeper investiga-
tion to future work. An attempt to deploy per-language thresholds
proved ineffective as a single threshold per language still did not
adequately capture the model’s ability to correctly predict hundreds
of diverse best practices. This led to a lack of diversity in predicted
URLs as the model tended to produce higher scores for some URLs
vs. others, irrespective of correctness. These observations led to the
first major change to AutoCommenter: per-URL thresholds com-
puted based on the intrinsic evaluation on the validation dataset.
4.1.2
Decoding. An evaluation using per-URL thresholds with
greedy decoding on full historical code reviews revealed that Auto-
Commenter detects violations in 6% of all changed files. However,
80% of comments would have been posted on lines of code not
modified by the author. Developers typically do not take action on
unchanged code. Consequently, AutoCommenter filters generated
comments on unchanged lines of code, reducing the ratio of com-
ments in changed files to 1.3%. In order to increase this ratio, we
experimented with different decoding strategies: greedy (default),
beam search, top-k, and top-p sampling. We settled on beam search
(generating 𝑛= 4 potential responses), which tripled the posting
frequency to 3.9%. It also yielded a substantially higher URL diver-
sity: the 10 most-frequently posted URLs accounted for 41% of all
comments, compared to 80% for greedy search.
Latency is another important aspect when choosing a decoding
strategy for deployment. While beam search increased the posting
frequency and diversity, inference became noticeably slower (me-
dian latency of 2 seconds). Given that this latency is prohibitive
for interactive use in the IDE, we ultimately decided to use beam
search for the code review system and greedy search for the IDE.