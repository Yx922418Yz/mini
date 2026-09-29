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
3.2.2
Dataset curation. Dataset curation is a single, on-demand
processing step, implemented as a Beam1 pipeline. It converts each
relevant code comment, based on the input/target format described
in section 3.1, into the standard TensorFlow Example data structure.
3.2.3
Training and fine-tuning. The curated examples are used
directly for model training and evaluation. We use the T5X frame-
work [22] on a fleet of TPUs, store the model checkpoints every
1000 steps, and use Tensorboard for monitoring the training.
3.3
Model Selection
Two intrinsic evaluations on historical data inform our selection of
a model checkpoint, confidence thresholds, and a decoding strategy.
First, an evaluation on the validation and test datasets provides
estimates of precision and recall on a per-file basis. Second, an
evaluation on full historical code reviews provides an estimate of
the total number of comments per code review, indicating how
often developers would interact with AutoCommenter.
3.3.1
Evaluation on Validation and Test Datasets. We temporally
split the dataset to ensure that the model has not been trained on
future code-review snapshots of the code comments in the valida-
tion and test datasets. In our dataset, 85% of files have exactly one
relevant code comment, 11% have two, and 4% have three or more.
We define a prediction to be correct if the predicted code location(s)
and URL(s) match the expected values, regardless of order.
Recall that the model provides a confidence score for each pre-
diction, which introduces another parameter: a prediction can be
suppressed if its confidence score is below some threshold 𝑡. We
define 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑡as the number of correct predictions whose confi-
dence score is greater than𝑡divided by the number of all predictions
whose confidence score is greater than 𝑡; we define 𝑅𝑒𝑐𝑎𝑙𝑙𝑡analo-
gously. These definitions allow us to estimate how many (in)correct
results would be shown to a user, as a function of 𝑡. 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑡and
𝑅𝑒𝑐𝑎𝑙𝑙𝑡are used for model checkpoint comparisons during training.
While this evaluation avoids data leakage and allow us to auto-
matically evaluate model performance, it has a limitation: while
it is reasonable to assume that the human comments for a given
code-review snapshot are correct, they are not exhaustive. In other
words, it is possible that the code in a given code-review snapshot
could be improved according to multiple best practices, but a hu-
man reviewer did not post comments (with URLs) for all of them.
This can happen for several reasons:
• Missing references: A reviewer may comment on an issue,
but did not include a URL as a reference.
• Selective commenting: A reviewer may comment on an issue
once, expecting the author to apply a fix throughout.
• Varied expertise or focus: A reviewer may not be familiar with
all best practices, or simply choose not to comment on an
issue in the context of a given code review (e.g., focusing
only on changed code).
While most files in our dataset have only one relevant comment,
anecdotal evidence based on manually inspecting “incorrect” pre-
dictions suggests that multiple best-practice comments are typically
possible due to the reasons stated above. Given that our ground-
truth data is incomplete, our precision and recall measures are noisy.
1https://beam.apache.org/
Therefore, we employ a complementary evaluation, described next,
to increase confidence in overall model performance.
3.3.2
Evaluation on Full Historical Code Reviews. To accurately
gauge potential comment volume in a live setting, we evaluate
AutoCommenter on a set of historical code reviews, using a specific
model checkpoint and threshold. The predicted comments are not
retroactively posted in the code review system, but rather logged
in a database for analysis. This allows us to estimate the expected
posting frequency—both at per-file and per-code-review granularity.
Because developers interact with AutoCommenter for an entire
set of code changes subject to code review, this evaluation is an
important step before production deployment. As an added benefit,
this step allows for further optimizations and assessment of posting
frequencies for different user groups, programming languages, etc.
3.4
Inference Infrastructure
The core of AutoCommenter is a central best practice analysis ser-
vice. This service takes as input one or more source files for analysis.
For each file, it constructs a model input (section 3.1), encodes it
in the standard TensorFlow Example data structure, and queries
the model. The model itself is served by a model service that uses
TensorFlow’s Example data structure as a domain agnostic input-
output format. Finally, the best practice analysis service performs
a series of filtering steps (section 4), which suppress low-quality
predictions, and returns the remaining predictions.
3.5
IDE and Code Review Integration
Developers interact with AutoCommenter’s analysis service in
two ways—directly through an IDE plugin, or indirectly through
the code review system. The code review system is used by all
developers at Google, and the IDE by almost all of them.
AutoCommenter’s comments appear in the IDE as diagnostics
marked with a blue curly underline, spanning the relevant code snip-
pet. Hovering over the underlined code reveals the full comment
with a concise summary of the best practice, including a clickable
link to the relevant best practice document. This embedded infor-
mation streamlines the workflow for developers by eliminating the
need to switch between the IDE and a web browser for unfamiliar
best practices. Since comments in the IDE need to be generated in
real-time, we aim to generate comments with sub-second latency.
In the code review system, AutoCommenter runs after each
update (i.e., on each new code-review snapshot), automatically
posting comments if it detects any violations. Comments produced
by automated tools are visually similar to comments produced by
humans, but have a differently colored background.
Figure 3 shows an example comment generated and posted by
AutoCommenter in the code review system. Note the thumbs up
and thumbs down buttons (right), which authors and reviewers can
click if they find a comment particularly useful or not. Also note
the “Please fix” button (left), which is visible to reviewers. If clicked,
a new comment is generated indicating that the reviewer believes
the comment is significant and must be addressed before the code
is merged into the codebase. These feedback buttons are standard
in the code review system, present on all comments generated by
automated tools (e.g., [7, 13]), and provide a signal for a tool’s user
acceptance. The IDE provides a similar feedback mechanism.