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

Coding
Autonomous agents get started on tasks based on initial plans and creating first draft solutions
Human developer reviews the draft PRs, gives feedback, and adds manual refinements before merging
🛑 Remember, large tasks aren't completely hands-free (yet).

Expect multiple feedback cycles for more challenging assignments, and anticipate some manual refinements for polish.

A realistic goal is around 80% time savings, not complete automation, with your expertise remaining vital for verification and final quality assurance.

Co-develop a PRD
For tasks that are complex or vaguely defined, collaborating with your autonomous agent to create a detailed plan can be highly effective.

It's perfectly okay if you initially don't know every nuance or requirement.

Start by prompting your agent to explore discovery questions, like "How does our authentication system function?" or "Which services might be impacted?" You can also ask the agent to identify specific relevant code targets for you to confirm early on.

Certain agents, such as Devin and Claude Code, offer dedicated planning modes that focus on reading and exploring existing code rather than immediately modifying it.

If you'd prefer deeper preparation before delegating a task, specialized codebase search tools like deepwiki.com and Devin Search can quickly provide insights into your codebase, helping streamline the process.

Set checkpoints
For multi-part tasks, especially those involving multiple codebases, establish clear checkpoints along the way:
Plan → Implement chunk → Test → Fix → Checkpoint review → Next chunk
Explicitly request pauses after each significant phase, particularly for complex features built across multiple layers (e.g., database, backend, frontend).

Use these checkpoints to ensure implementation aligns with your expectations, clarify doubts (ex.

"Explain the auth process and confirm its security"), and correct course early to avoid cascading issues.

Example:
"I want you to implement this feature that will span our database, backend, and multiple frontend interfaces.

Please first plan out the database schema changes needed, and let me know when that is done so I can apply the migration." -> "Now please implement the backend changes and add tests to make sure XYZ works.

Let me know when that is done" -> "Now implement the changes in both our web and mobile interfaces to call the new backend endpoint"
Teach it to verify its own work
When giving feedback, go beyond simply pointing out issues ("This function isn't working").

Clearly articulate your testing process to enable the agent to independently verify future tasks.

For testing patterns you'll frequently repeat, integrate these into your agent's permanent knowledge base (See Add to your agent's knowledge base).

Example:
In Devin, we actively prompt users to save essential testing procedures to the agent's ongoing memory, streamlining future interactions.

Increase test coverage in AI hot spots
Currently, agents aren't fully capable of interactively testing all scenarios thoroughly.

Enhancing test coverage in areas heavily modified by AI ensures greater confidence in the agent's output.

Solid tests mean that code that appears correct can be confidently merged without worry.

Example:
Our team strengthened unit tests in a critical section of our codebase before entrusting our AI to translate the implementation from Python to C.

(Advanced)
Automating Workflows
Agents can respond to incoming events much faster than humans, and they're a lot more willing to do boring, repetitive work, than their human counterparts.

Create Shortcuts for Your Most Repetitive Work
Engineering teams frequently encounter repetitive, routine tasks.

These are perfect candidates for automation with agents.

Common examples include:
feature flag removal
dependency upgrades
fixing and adding tests on new feature PRs
To set this up efficiently, an experienced engineer typically creates a robust, reusable prompt template [2] In Devin, these are called playbooks that can run repeatedly for these scenarios.

Example:
One of our customers automatically triggers three agents dedicated to writing unit tests whenever new features are developed.

Intelligent Code Review & Enforcement
While specialized tools for fast code review exist [3] Such as Greptile and CodeRabbit , autonomous agents can be an interesting option to deliver more accurate insights, particularly if they've already indexed the functionality of your repositories.

Example:
At Cognition, we like to maintain a list of the most common mistakes engineers make and we commit this list to the codebase.

Then, instead of writing classical lint rules to catch these (which is often not possible), we have an agent run on every new PRs to check for these mistakes.

Hook into incidents and alerts
You can also set up autonomous agents to trigger automatically in response to specific events.

For example, Devin provides an accessible API, and other agents can be integrated into custom workflows via CLI commands.

These setups work especially well alongside MCPs to ingest third-party error logs.

⚠️When it comes to triaging issues in production services, AI's debugging skills are not that great.

Instead of asking the AI to fix bugs end-to-end as they come up, it is often more practical to ask the AI to just flag the most suspicious errors, changes, etc.

(Advanced)
Customization & Improving Performance
Environment Setup
Nothing slows down an agent faster than an incomplete or mismatched environment.

To keep things running smoothly, align your agent's setup exactly with your team's.

This includes language versions, package dependencies, and automated checks.

For example, pre-commit should be installed in the agent's environment and environment configurations (secrets, language versions, virtual environments, browser logins) should be sourced automatically using tools like .envrc or custom configuration of .bashrc
Example:
We set up our agent's browser with pre-authenticated logins, removing the hassle of manual authentication and making testing much easier.

Build Custom CLI Tools and MCPs
MCPs are widely available and are quick to set up and experiment with connecting your agent to external tools [4] In Devin, MCPs are still in beta as we're figuring out the best way to support them.

Please contact us for access!.

But many people overlook setting up simple CLI scripts for your agents.

As a simple example, you could give your agent a script to pull information about a linear ticket given a ticket ID.

You might also want to give your agent a tool to perform common parts of a workflow reliably, such as a script for restarting the local development environment.

Example:
We have a customer who has had a lot of success with creating a CLI tool that surfaces only the first failing test in a test suite.

The CLI prompts the agent to focus on only that test with detailed error information, and this CLI leads the agent to have higher success and faster completion rates on long tasks.

Add to your agent's knowledge base
If your agent makes some common mistakes, it's a great time to codify your feedback in the agent's knowledge base.

In Devin, there is a dedicated knowledge management system.

Many products offer .rules files, .md files for the agent to permanently ingest.

Don't just give it guidelines on the framework you're using, but also tell it about the overall architecture of your project.

Tell it what type of testing is common for different kinds of tasks, how to run important commands and which tools you recommend using.

Example:
We give our agent knowledge about the specific procedure it should follow when adding a new service route.

The information includes every place it needs to add boilerplate in the frontend and backend.

As a result, these tasks are now easily delegated to our AI.

Practical Considerations
Limitations of Autonomous Agents
Limited debugging skills
Bugs reports can be deceptively simple.

But many bugs often require not only access to databases and logs, but also a level of debugging that is greater than most AI agents today.

If using AI to aid in debugging, we recommend asking for a list of probable root causes rather than trying to debug and fix everything itself.

Then, a human can decide based on their own experience which one is the real root cause.

But once the cause is known, agents can still be quite helpful at implementing the fix.

Poor fine-grained visual reasoning
Generally models today don't have great visual reasoning capabilities at the level of details needed to match screenshots of designs or Figma mockups.

They are most reliable on visuals that can be described at the level of code (ex.

giving it code from Figma).

If you want it to match your visual style, you should use a good design system with reusable components.

Knowledge Cutoffs
Whenever you want to work with a new library, you should explicitly point it to the latest docs.