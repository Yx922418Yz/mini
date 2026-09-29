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

AI-Assisted Assessment of Coding Practices
in Modern Code Review
Manushree Vijayvergiya
manushree@google.com
Google
Zurich, Switzerland
Małgorzata Salawa
magorzata@google.com
Google
Zurich, Switzerland
Ivan Budiselić
ibudiselic@google.com
Google
Zurich, Switzerland
Dan Zheng
danielzheng@google.com
Google
Mountain View, USA
Pascal Lamblin
lamblinp@google.com
Google
Montreal, Canada
Marko Ivanković
markoi@google.com
Google
Zurich, Switzerland
Juanjo Carin
juanjocarin@google.com
Google
Sunnyvale, USA
Mateusz Lewko
mlewko@google.com
Google
Zurich, Switzerland
Jovan Andonov
jandonov@google.com
Google
Zurich, Switzerland
Goran Petrović
goranpetrovic@google.com
Google
Zurich, Switzerland
Daniel Tarlow
dtarlow@google.com
Google
Montreal, Canada
Petros Maniatis
maniatis@google.com
Google
Mountain View, USA
René Just∗
rjust@cs.washington.edu
University of Washington
Seattle, USA
ABSTRACT
Modern code review is a process in which an incremental code con-
tribution made by a code author is reviewed by one or more peers
before it is committed to the version control system. An important
element of modern code review is verifying that code contributions
adhere to best practices. While some of these best practices can be
automatically verified, verifying others is commonly left to human
reviewers. This paper reports on the development, deployment,
and evaluation of AutoCommenter, a system backed by a large
language model that automatically learns and enforces coding best
practices. We implemented AutoCommenter for four programming
languages (C++, Java, Python, and Go) and evaluated its perfor-
mance and adoption in a large industrial setting. Our evaluation
shows that an end-to-end system for learning and enforcing coding
best practices is feasible and has a positive impact on the devel-
oper workflow. Additionally, this paper reports on the challenges
associated with deploying such a system to tens of thousands of
developers and the corresponding lessons learned.
CCS CONCEPTS
• Software and its engineering →Software verification and
validation.
∗Work done at Google.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0685-1/24/07
https://doi.org/10.1145/3664646.3665664
KEYWORDS
Artificial Intelligence, Code Review, Coding Best Practices
ACM Reference Format:
Manushree Vijayvergiya, Małgorzata Salawa, Ivan Budiselić, Dan Zheng,
Pascal Lamblin, Marko Ivanković, Juanjo Carin, Mateusz Lewko, Jovan An-
donov, Goran Petrović, Daniel Tarlow, Petros Maniatis, and René Just. 2024.
AI-Assisted Assessment of Coding Practices in Modern Code Review. In
Proceedings of the 1st ACM International Conference on AI-Powered Software
(AIware ’24), July 15–16, 2024, Porto de Galinhas, Brazil. ACM, New York,
NY, USA, 9 pages. https://doi.org/10.1145/3664646.3665664
1
INTRODUCTION
Modern code review [21, 23] (compared to holistic code review [8])
has grown organically over the years in open-source and industrial
settings. A set of common peer-review criteria have emerged [5, 20,
21], which include coding best practices. Many companies, projects,
and even programming languages formally define them in the form
of “style guides” [1–4] that commonly cover the following aspects:
• Formatting: line limits, use of whitespaces and indentation,
placement of parentheses and brackets, etc.;
• Naming: capitalization, brevity, descriptiveness, etc.;
• Documentation: expected placement and content of file-level,
function-level, and other comments;
• Language features: use of specific language features in differ-
ent (code) contexts;
• Code idioms: use of code idioms to improve code clarity,
modularity, and maintainability.
Developers generally report high satisfaction with modern code
review processes [23, 28]. One of their main benefits is the learning
experience for code authors who are not familiar with the codebase,
specific language features, or common code idioms. During a review,
an expert developer educates the code author on best practices, in
arXiv:2405.13565v1 [cs.SE] 22 May 2024