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

AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
Manushree Vijayvergiya et al.
URL, we inspected its best practice document and determined (1) the
best-practice type (section 1) and (2) whether a linter that detects a
corresponding violation exists or can be easily built. Specifically,
three authors, each with over 10 years of experience in building
static analysis tools, read the documentation and independently
categorized the URLs. There were no disagreements on the best-
practice type, but there were disagreements on whether a linter
can be easily built for about 15% of URLs. The three authors re-
solved these disagreements through majority vote and discussion.
Disagreements stemmed from ambiguous best practices, and those
with multiple guidelines. For example, while checking the pres-
ence of code documentation is relatively straightforward, reasoning
about justified exceptions and clarity of content may not.
Figure 6 shows the distribution of the 50 sampled URLs, broken
down by type and whether violations can be detected by a linter.
For 33/50 (66%) of these best practices, violation detection is beyond
the scope of traditional static analysis.
6
LESSONS LEARNED
Based on our experience developing and deploying AutoCommenter,
we summarize a few key lessons learned:
• Complementing traditional analyses: AutoCommenter’s
LLM-backed approach generates comments for 68% of best
practices frequently referenced by human reviewers. Many
of these are out of scope for traditional static analyses.
• Intrinsic evaluation vs. real-world performance: Intrin-
sic evaluations and real-world performance can diverge sig-
nificantly: our intrinsic evaluation, using a dataset of real-
world human comments together with a state of the art
model architecture and training process, indicated a promis-
ing model, but our extrinsic evaluations and system improve-
ments proved essential for a successful deployment.
• Monitoring user acceptance is critical: Even a few nega-
tive user experiences can erode trust in an automated system.
Continuously monitoring and analyzing real-world feedback
was crucial in detecting such instances and identifying reme-
dies. In the case of AutoCommenter, a simple suppression
mechanism was sufficient to strongly improve user accep-
tance to over 80% without major sacrifices in efficacy.
7
RELATED WORK
Johnson [15] introduced the C linter almost 50 years ago in 1977. In
those 50 years, a considerable body of research on automated static
analysis was produced: a recent literature review by Heckman and
Williams [10] identified 17,571 papers. Many studies explore how
developers interact with static analysis. Johnson et al. [14] explore
challenges developers face when trying to use static analysis. The
results of their study highlights the importance of good integration
into existing developer workflows and the importance of develop-
ing and maintaining trust in the tool. Vassallo et al. [27] explore
how developers interact with static analysis in different contexts,
including coding and code review. They too find that integration
into existing workflows plays a major role in developers willing-
ness to use the tools and that high quality of results is extremely
important. Beller et al. [6] studied usage of static code analysis in a
large number of open source projects. Among other findings, they
highlight that how automated analysis is and should be used varies
based on the programming language.
In contrast, using machine learning for code analysis is a compar-
atively new and less understood field. A number of recent publica-
tions (e.g., Hong et al. [11], Li et al. [16], Li et al. [17], Thongtanunam
et al. [24], Tufano et al. [25], and Tufano et al. [26]) report on model
evaluations and propose tools for automated code review. While
these models and the review comment generation task are very sim-
ilar to the model presented in this paper, evaluations largely focused
on historical datasets. As discussed in section 3.3.1 an intrinsic eval-
uation on only historical comments is somewhat limited and can
sometimes fail to predict real-world performance. Another recent
publication by Frömmgen et al. [9] presents an evaluation of a live
system, but for the opposite task: creating code from comments
rather than comments from code.
8
CONCLUSION
Verifying that code adheres to best practices is a common task in
modern code review processes. While some best practices can be
automatically verified with traditional tools such as linters, many
require the knowledge and judgement of experienced developers,
which requires time and effort.
This paper reports on our experience developing, deploying, and
evaluating AutoCommenter, an LLM-backed code review assistant
system. Specifically, it lays out the entire process from task and
model design, over intrinsic evaluations and system calibrations,
to a staged roll out and end-user evaluation.
The evaluation results show that it is feasible to develop an
end-to-end system with capabilities well beyond traditional tools
while achieving a high degree of end-user acceptance. These results
are a promising first step towards the deployment of sophisticated
code-review assistants and automated code reviews.
Our priority was to ensure a positive developer experience by
designing AutoCommenter to have very high precision. While recall
was not the primary focus, we recognize its significance and plan
to explore what changes in the model and system architecture can
improve recall. For example, the model we used in 2022 was state of
the art at the time. However, it has a limited context window of 2048
tokens which suffices for only around 200 lines of code. Current
state of the art models have context windows of tens of thousands of
tokens during training and over a million tokens during inference.
This leap opens up opportunities for new features and significant
improvement in existing ones.
9
ACKNOWLEDGEMENTS
This work is the result of years of collaboration between teams in
Google Core Systems and Google DeepMind. We are grateful for the
support and advice of all our team members and leadership, includ-
ing Alberto Elizondo, Alexander Frömmgen, Ballie Sandhu, Chandu
Thekkath, Chris Gorgolewski, David Tattersall, Ilya Cherny, Jacob
Austin, Katja Grünwedel, Kristóf Molnár, Lera Kharatyan, Luka Ri-
manić, Madhura Dudhgaonkar, Marc Brockschmidt, Marcus Revaj,
Maxim Tabachnyk, Nina Chen, Niranjan Tulpule, Nitya Ramani,
Paige Bailey, Pavel Sychev, Pierre-Antoine Manzagol, Quinn Madi-
son, Roger Fleig, Satish Chandra, Savinee Dancs, Stoyan Nikolov,
Subhodeep Moitra, and Vaibhav Tulsyan.