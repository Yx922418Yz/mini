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
addition to reviewing (and learning about) the code contributions
and their implications.
Static analysis tools such as linters [15] can automatically verify
that code adheres to some best practices (e.g., formatting rules), and
some tools can even automatically fix violations. However, nuanced
guidelines or those with exceptions are difficult to automatically
verify in their entirety (e.g., naming conventions and justified devi-
ations in legacy code), and some guidelines cannot be captured by
precise rules at all (e.g., clarity and specificity of code comments)
and rely on human judgement and collective developer knowledge.
As a result, it is generally expected that human reviewers check
code changes for best practice violations.
The biggest cost of the code-review process is the time required,
especially from expert developers. Even with significant automa-
tion in place, and keeping the process as lightweight as possible, a
developer can easily dedicate several hours daily to this task [23].
Recent advances in machine learning, capabilities of large lan-
guage models (LLMs) in particular, suggest that LLMs are suitable
for code-review automation (e.g., [11, 16, 17, 24–26]). However, the
software engineering challenges around deploying an end-to-end
system at scale remain unexplored. Likewise, extrinsic evaluations
of such systems on overall efficacy and user acceptance are missing.
This paper investigates whether it is possible to partially au-
tomate the code-review process, specifically the detection of best
practice violations, thereby providing timely feedback for code
authors and allowing reviewers to focus on overall functionality.
Specifically, this paper reports on our experience of developing,
deploying, and evaluating AutoCommenter—an automated code-
review assistant—in an industrial setting at Google, where it is
currently used by tens of thousands of developers every day.
In summary, the contributions of this paper are:
• A general architecture of an LLM-based code-review assis-
tant system (section 3).
• A description of tool calibration and deployment to tens of
thousands of developers (section 4).
• An evaluation of the system (section 5).
• A summary and discussion of lessons learned (section 6).
2
BACKGROUND
AutoCommenter was developed in a large industrial setting at
Google. The modern code review practices at Google are similar to
those of other industrial and open source projects [23].
2.1
Code Review Process
The code review process at Google is well established, change-
based, and tool-assisted. Ivanković et al. [12] and Petrović et al.
[18] provide a detailed summary of the process. Each change to the
codebase must be reviewed by at least one other developer. Every
day, tens of thousands of changes to the codebase go through the
review process and tens of thousands of developers participate in
the process, as both code authors and reviewers.
Authors and reviewers exchange comments through the code
review system, and a review progresses through snapshots of files
affected by the change. Each reviewer comment is attached to a
specific line and column range in a specific file snapshot. To resolve
a comment, the author typically modifies the file in their local copy
Figure 1: Example comment posted by a human reviewer.
and exports a new snapshot for the next round of code review.
When the author and all reviewers are satisfied and no automated
analysis is blocking the merge, the code is merged into the codebase.
The most expensive part of the code review process is the time
spent by code authors and reviewers “shepherding” a change (from
initial coding, through addressing reviewer comments and ensur-
ing all automated analyses pass, to finally merging the change
into the codebase). While the process is optimized with automated
systems analyzing the code before the review (notably automatic
code formatting without human intervention), code reviews still
cost thousands of developer-years per year. Thus, even single-digit
percentage savings translate into significant business impact.
2.2
Best Practices
A best practice is a specific use of programming language that is
considered superior, and a best practice document describes how
it should be applied and what benefits it brings. Best practice URL
refers to a best practice document or specific section therein, and
best practice violation refers to a specific piece of code that does not
adhere to a best practice, but can be changed to do so. If clear from
context, we use the terms URL and violation to refer to best practice
URL and best practice violation, respectively.
Google’s central code repository contains code in many lan-
guages, with C++, Java, Python and Go exceeding 100 million lines
each [19]. For 15 different languages there are formal style guides
readily available to all developers. Many of these languages have
additional language primers, documentation for core libraries, and
tip-of-the-week style newsletters. While these materials are not
as strictly enforced as style guides, they are frequently referenced
in code reviews. Some languages boast hundreds of pages of such
documentation. Both code authors and reviewers are expected to
verify that the code follows all best practices.
A formal mechanism called “readability”, introduced more than
a decade ago, ensures that best practices are followed consistently.
Dedicated style experts in a given language, called “readability
mentors”, guide inexperienced developers towards proficiency in
the language [23]. Readability mentors commonly summarize a
best practice in a few sentences and at the end of the comment
include a URL for the change author as a reference. Figure 1 shows
an example of a comment posted by a readability mentor.