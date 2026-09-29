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
4.2
Suppressing Outdated Best Practices
After launching AutoCommenter to around 3 thousand voluntary
first-adopters, we noticed a large number of issues being filed by
users within a few days. Many of these corresponded to a single
URL2, which describes best practices related to Python imports.
However, the canonical source for some type names had changed
in Python 3.9, and the best practice had also changed in early 2022.
Since our training data stretches before 2022, it contained a num-
ber of best practice comments that were no longer applicable. We
realized that this is a recurring pattern: as languages evolve, or
new libraries are introduced, best practices evolve as well. One
way of mitigating the problem is to filter out such data (whenever
a rule changes), and retrain the model. This is however time and
resource-consuming: it requires full data regeneration, model train-
ing, evaluation, and rollout. In the meantime, the “outdated” model
needs to be either switched off, causing downtime of the system, or
affected predictions need to be suppressed. Otherwise, the system
could quickly lose developer trust. We opted for suppression of spe-
cific best-practice predictions, using conditional filtering (matching
regular expressions on the source code) for two reasons. First, it
can be dynamically deployed and immediately applied. Second, it
allows for granular filtering of predictions.
4.3
Independent Rating of Selected Comments
After several months of early usage, we observed that the useful
ratio plateaued at around 54%. To understand the reasons, iden-
tify areas for improvement, and prepare for a wider deployment,
we conducted an independent human rating study in April 2023,
analyzing a sample of around 370 posted comments that received
developer feedback during our first-adopters deployment.
To gather diverse perspectives on the usefulness of comments we
recruited 15 raters—developers from partner teams. We asked them
to rate AutoCommenter’s comments that received explicit user
feedback. We did not show the original user feedback to the rater, to
avoid biasing their evaluation. The raters assessed each comment’s
usefulness based on the linked best practice and the surrounding
code. We instructed them to focus on comment correctness, but also
whether the comment would be actionable to them as an author
(e.g., would they resolve a comment that is technically correct but
does not seem worth resolving in a specific instance). They were
encouraged to provide free-form feedback on each comment.
The useful ratio from the rater evaluation was 60%, slightly
higher than the 54% from the developer feedback on the same
comments, but well below our target of 80% for wider deployment.
The most interesting finding from this study was that there were
clear patterns of not useful comments. Here are some examples:
Several topics or complex topic: For example, one URL points
to a section that describes multiple guidelines for interacting with
the Python linter, including cases where it often triggers and ways
to suppress it. An author may struggle to understand what specific
guideline a posted comment is referring to and how to resolve it.
Similarly, the guidance on writing good function documentation in
C++ is a full page of dense text. Raters frequently noted a disconnect
between a best practice (and AutoCommenter’s concise summary)
and the actual code, even when it contained a relevant violation.
2https://github.com/google/styleguide/blob/gh-pages/pyguide.md#22-imports
Importance of high-quality summaries: Raters often found
that AutoCommenter’s summary, which was generated by scraping
the document source and sometimes missing, failed to adequately
explain the relevance of the cited guideline to the comment/code.
Subjective and potentially contentious topic: One example
is avoiding flags in library code. Flags can cause problems when
used in libraries, but some libraries are specifically designed to
have many features configurable via flags. Additionally, legacy code
may not adhere to this guideline and reviewers will not enforce it.
The model did not learn these nuances and sometimes predicted a
violation when an author added a new flag to an existing library.
Systematic model error for some guidelines: One interesting
example is a guideline that promotes the use of the member function
push_back over emplace_back for C++ vectors when both functions
can be used with the same arguments to achieve the same effect.
The model had learned to predict this, but it would also predict
it in cases where emplace_back is warranted, and also when an
unrelated type had a member function called push_back.
Correct but low-value comments: A missing period at the
end of a sentence in a code comment is often allowed by human
reviewers. While technically correct, asking the author to go back
to their IDE and fix the issue may provide net negative value.
The insights from the rater study informed two changes to Auto-
Commenter. First, the rater study identified 17 non-actionable URLs,
whose suppression increased the historical useful ratio from 54% to
66% on developer feedback, and from 60% to 74% on rater feedback.
We further analyzed comments linked to similar, unrated URLs
and suppressed an additional 5. Second, we reviewed and manually
updated summaries for all frequently posted URLs. Together, these
changes were sufficient to reach our target useful ratio of 80% for
the next stage of deployment.
4.4
A/B Experiment
In July 2023, we deployed AutoCommenter to about half of all devel-
opers in the context of an A/B experiment. We randomly assigned
developers to a an experiment group (AutoCommenter enabled)
and a control group (AutoCommenter disabled). We randomized
based on the last few digits of the SHA256 hash of the developers
email address, and we verified that both groups did not differ in
size and composition, including distribution of tenure, seniority,
programming languages and business units. We also confirmed that
none of the variables measured during the experiment differed be-
tween the control and the experiment group before the experiment
began. The comment posting frequency during the experiment was
in line with expectations (section 4.1).
We did not detect any statistically significant change in any
of the following: total duration of code reviews, time developers
actively spent on the code review, the number of comment-response
iterations between the author and the reviewer. We did, however,
detect a slight improvement in coding speed. We conjecture that
the reduction in context switches to documentation leads to this
positive effect. We leave a deeper investigation for future work.
Based on the results, we concluded that there are no adverse effects,
and deployed AutoCommenter to all developers in October 2023.