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

Use case 7
Exploration and ideation
Codex is also useful for open-ended work like finding alternative solutions or validating design
decisions. You can prompt for different ways of solving a problem, explore unfamiliar patterns, or
pressure-test assumptions. This helps surface tradeoffs, expand design options, and sharpen
implementation choices.
It’s also used to identify related bugs. Given a known issue or deprecated method, Codex can
identify similar patterns elsewhere in the code, making it easier to catch regressions or finish
cleanup work.
Anecdotes from our teams
Codex helps me solve the cold‑start
problem — I paste a spec and docs and it
scaffolds code or shows me what I forgot.
Product Engineer,
ChatGPT Desktop
After I fix a bug I ask Codex where similar
bugs might lurk, then spin follow‑up tasks.
Performance Engineer,
Retrieval Systems
Try using Codex for exploration and
ideation with these sample prompts
How would this work if the system were
event-driven instead of request/response?
Find all modules that manually build SQL
strings instead of using our query builder.
Rewrite this in a more functional style, avoid
mutation and side effects.
10
How OpenAI uses Codex

Best practices
Codex works best when it’s given structure, context, and room to iterate. Here are some of the
habits OpenAI teams are cultivating to get consistent value out of it in day-to-day work.
Start with Ask Mode
For large changes, start by prompting Codex for an
implementation plan using Ask mode, which then becomes the
input for follow-up prompts when you switch to Code Mode.
This two-step flow keeps Codex grounded and helps avoid
errors in its output. Codex works best with well-scoped tasks
that would take you or a teammate about an hour to complete
or a few hundred lines of code to implement. As models
improve, expect the size of the tasks it can take on to increase.
Iteratively improve Codex’s
development environment
Setting a startup script, environment variables, and internet
access significantly reduces Codex’s error rate. As you run
tasks, look for build errors that can be corrected in Codex’s
environment configuration. This may take a few iterations, but
gives significant efficiency gains in the long run.
Structure your prompt as if
you are writing a Github Issue
Codex responds better when prompts mirror how you’d
describe a change in a PR or issue. That means including file
paths, component names, diffs, and doc snippets when
relevant. Prompting with patterns like “Implement this the
same way it’s done in [module X]” improves results.
Use the Codex task queue
as a lightweight backlog
Fire off tasks to capture tangential ideas, partial work, or
incidental fixes. There’s no pressure to generate a full PR in one
go. Codex works well as a staging area you can return to when
you’re back in focus.
11
How OpenAI uses Codex

Best practices
Use AGENTS.md to
supply persistent context
Maintain an AGENTS.md file to help Codex operate more
effectively in your repo across prompts. These files typically
include naming conventions, business logic, known quirks, or
dependencies Codex can’t infer from the code alone. Learn
more on structuring your AGENTS.md file in the docs.
Leverage “Best of N”
to improve output
The Best-of-N feature lets you simultaneously generate
multiple responses for a single task to quickly explore multiple
solutions and pick the best one. For more complicated tasks,
you can review several iterations and combine parts of different
responses to get a stronger result.
Looking ahead
Codex is still in research preview, but it’s already making a real impact in how we build, helping us
move faster, write better code, and take on work that would’ve otherwise never been prioritized.
We’re excited by the potential ahead — as our models get better and Codex becomes more deeply
integrated into our workflows, we’re looking forward to unlocking even more powerful ways to
develop software with it. We’ll continue to share what we learn along the way.
12
How OpenAI uses Codex