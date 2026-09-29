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

As a reviewer, you might know that the code in
question crashes with negative integers, but it’s better to have
the developer intuit this themselves.

Questions like this might
also be indicative of a testing gap, or a need for further
specification of scope.

“This section is confusing to me, I don’t understand why class A
is talking to class B” If the developer hasn’t provided a helpful
description, and the code isn’t neatly structured, this kind of
comment helps drive for clarity of design and cleaner code.

“It looks like you broke an interface boundary here.

How will
that affect the user?” You’ve pointed out an issue you noticed,
giving them the benefit of the doubt that they meant to do it.

Now
they can think through the unseen ramifications of breaking the
interface boundary and either provide a rationale for their
decision, or choose to change it.

In general, framing feedback as questions is a good way to drive for
clarity, correctness, and at the same time help the developer improve
their designs in the future.

This is usually how quality creative
writing groups give each other feedback.

In a creative writing
setting, it’s harmful to say things like, “I don’t like this
character.” whereas the same comment can be reframed more clearly: “In
chapter one your character was warm and compassionate and now he’s
cold and icey.

He doesn’t seem like a real person to me.” Now there’s
specific feedback that can be clarified to suss out the problem.

Programmers like to solve problems and point out issues, so by nature
they like to discover and point out flaws.

It’s tempting to see code
reviews as a way to prove how smart you are by finding problems in
your peer’s code.

Don’t do it.

Code review is a way to get more eyes
on a change and suss out critical problems, but your goal should be to
review in a way that encourages your team members to improve their
skills while fixing the problems at hand.

Style Points
Brace positions, variable / function names, indentation and spacing
issues should be addressed, but they are not the central purpose of
good code review (notice that I put them at the top the code
review pyramid).

If you find that your team is spending 90% of it’s
time nitpicking indentation and variable names, you’re probably
wasting everyone’s time on something that could be mostly automated.

Write up a style guide, enforce indentation and spacing issues on
check-in and spend your time focusing on higher value issues.

I don’t
want to diminish the importance of a consistent style.

On the
contrary, having a consistent idiomatic style is one of the easiest
ways to make your codebase easy to read and comprehend.

Still, if you
spend all of your code review focused on these simplistic tasks, ask
yourself whether you’re avoiding the harder and more important work of
keeping your team mentally aligned and thinking about higher level
designs.

more posts
about the author
Blake Smith is a Principal
Software Engineer at Sprout
Social.