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

Engineering at Anthropic
Writing effective tools for agents — with agents
Published Sep 11, 2025
Agents are only as effective as the tools we give them.

We share how to write high-quality tools and evaluations, and how you can boost performance by using Claude to optimize its tools for itself.

The Model Context Protocol (MCP) can empower LLM agents with potentially hundreds of tools to solve real-world tasks.

But how do we make those tools maximally effective?

In this post, we describe our most effective techniques for improving performance in a variety of agentic AI systems1.

We begin by covering how you can:
Build and test prototypes of your tools
Create and run comprehensive evaluations of your tools with agents
Collaborate with agents like Claude Code to automatically increase the performance of your tools
We conclude with key principles for writing high-quality tools we’ve identified along the way:
Choosing the right tools to implement (and not to implement)
Namespacing tools to define clear boundaries in functionality
Returning meaningful context from tools back to agents
Optimizing tool responses for token efficiency
Prompt-engineering tool descriptions and specs
Building an evaluation allows you to systematically measure the performance of your tools.

You can use Claude Code to automatically optimize your tools against this evaluation.

What is a tool?

In computing, deterministic systems produce the same output every time given identical inputs, while non-deterministic systems—like agents—can generate varied responses even with the same starting conditions.

When we traditionally write software, we’re establishing a contract between deterministic systems.

For instance, a function call like getWeather(“NYC”) will always fetch the weather in New York City in the exact same manner every time it is called.

Tools are a new kind of software which reflects a contract between deterministic systems and non-deterministic agents.

When a user asks "Should I bring an umbrella today?,” an agent might call the weather tool, answer from general knowledge, or even ask a clarifying question about location first.

Occasionally, an agent might hallucinate or even fail to grasp how to use a tool.

This means fundamentally rethinking our approach when writing software for agents: instead of writing tools and MCP servers the way we’d write functions and APIs for other developers or systems, we need to design them for agents.

Our goal is to increase the surface area over which agents can be effective in solving a wide range of tasks by using tools to pursue a variety of successful strategies.

Fortunately, in our experience, the tools that are most “ergonomic” for agents also end up being surprisingly intuitive to grasp as humans.

How to write tools
In this section, we describe how you can collaborate with agents both to write and to improve the tools you give them.

Start by standing up a quick prototype of your tools and testing them locally.

Next, run a comprehensive evaluation to measure subsequent changes.

Working alongside agents, you can repeat the process of evaluating and improving your tools until your agents achieve strong performance on real-world tasks.

Building a prototype
It can be difficult to anticipate which tools agents will find ergonomic and which tools they won’t without getting hands-on yourself.

Start by standing up a quick prototype of your tools.

If you’re using Claude Code to write your tools (potentially in one-shot), it helps to give Claude documentation for any software libraries, APIs, or SDKs (including potentially the MCP SDK) your tools will rely on.

LLM-friendly documentation can commonly be found in flat llms.txt files on official documentation sites (here’s our API’s).

Wrapping your tools in a local MCP server or Desktop extension (DXT) will allow you to connect and test your tools in Claude Code or the Claude Desktop app.

To connect your local MCP server to Claude Code, run claude mcp add <name> <command> [args...].

To connect your local MCP server or DXT to the Claude Desktop app, navigate to Settings > Developer or Settings > Extensions, respectively.

Tools can also be passed directly into Anthropic API calls for programmatic testing.

Test the tools yourself to identify any rough edges.

Collect feedback from your users to build an intuition around the use-cases and prompts you expect your tools to enable.

Running an evaluation
Next, you need to measure how well Claude uses your tools by running an evaluation.

Start by generating lots of evaluation tasks, grounded in real world uses.

We recommend collaborating with an agent to help analyze your results and determine how to improve your tools.

See this process end-to-end in our tool evaluation cookbook.

Held-out test set performance of our internal Slack tools
Generating evaluation tasks
With your early prototype, Claude Code can quickly explore your tools and create dozens of prompt and response pairs.

Prompts should be inspired by real-world uses and be based on realistic data sources and services (for example, internal knowledge bases and microservices).

We recommend you avoid overly simplistic or superficial “sandbox” environments that don’t stress-test your tools with sufficient complexity.

Strong evaluation tasks might require multiple tool calls—potentially dozens.

Here are some examples of strong tasks:
Schedule a meeting with Jane next week to discuss our latest Acme Corp project.

Attach the notes from our last project planning meeting and reserve a conference room.

Customer ID 9182 reported that they were charged three times for a single purchase attempt.

Find all relevant log entries and determine if any other customers were affected by the same issue.

Customer Sarah Chen just submitted a cancellation request.

Prepare a retention offer.

Determine: (1) why they're leaving, (2) what retention offer would be most compelling, and (3) any risk factors we should be aware of before making an offer.

And here are some weaker tasks:
Schedule a meeting with jane@acme.corp next week.

Search the payment logs for purchase_complete and customer_id=9182.

Find the cancellation request by Customer ID 45892.

Each evaluation prompt should be paired with a verifiable response or outcome.

Your verifier can be as simple as an exact string comparison between ground truth and sampled responses, or as advanced as enlisting Claude to judge the response.

Avoid overly strict verifiers that reject correct responses due to spurious differences like formatting, punctuation, or valid alternative phrasings.

For each prompt-response pair, you can optionally also specify the tools you expect an agent to call in solving the task, to measure whether or not agents are successful in grasping each tool’s purpose during evaluation.

However, because there might be multiple valid paths to solving tasks correctly, try to avoid overspecifying or overfitting to strategies.

Running the evaluation
We recommend running your evaluation programmatically with direct LLM API calls.

Use simple agentic loops (while-loops wrapping alternating LLM API and tool calls): one loop for each evaluation task.

Each evaluation agent should be given a single task prompt and your tools.

In your evaluation agents’ system prompts, we recommend instructing agents to output not just structured response blocks (for verification), but also reasoning and feedback blocks.

Instructing agents to output these before tool call and response blocks may increase LLMs’ effective intelligence by triggering chain-of-thought (CoT) behaviors.

If you’re running your evaluation with Claude, you can turn on interleaved thinking for similar functionality “off-the-shelf”.

This will help you probe why agents do or don’t call certain tools and highlight specific areas of improvement in tool descriptions and specs.

As well as top-level accuracy, we recommend collecting other metrics like the total runtime of individual tool calls and tasks, the total number of tool calls, the total token consumption, and tool errors.

Tracking tool calls can help reveal common workflows that agents pursue and offer some opportunities for tools to consolidate.

Held-out test set performance of our internal Asana tools
Analyzing results
Agents are your helpful partners in spotting issues and providing feedback on everything from contradictory tool descriptions to inefficient tool implementations and confusing tool schemas.

However, keep in mind that what agents omit in their feedback and responses can often be more important than what they include.

LLMs don’t always say what they mean.

Observe where your agents get stumped or confused.

Read through your evaluation agents’ reasoning and feedback (or CoT) to identify rough edges.

Review the raw transcripts (including tool calls and tool responses) to catch any behavior not explicitly described in the agent’s CoT.

Read between the lines; remember that your evaluation agents don’t necessarily know the correct answers and strategies.

Analyze your tool calling metrics.