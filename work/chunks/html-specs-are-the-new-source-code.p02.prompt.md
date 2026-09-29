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

Now, it’s important to caveat the above with what’s needed for it to work well:
Being specific: Using vague specs will only result in a messy codebase.

Using Claude to take an initial draft of a ticket, review the codebase, and help make it more specific is an essential part of the process.

In our case, we also have guidelines for writing a good spec.

Being selective: Using the above for simpler tasks is ideal.

The more complex the ticket, the greater the need for someone who knows what they’re doing to get involved (“self-serve” ends up being anything but, in these cases).

Gatekeeping: This approach only works well because there’s an actual engineer who knows what they’re doing, reviewing changes and ensuring the balance between simplicity and functionality is maintained.

But let’s be clear: the rules have changed.

Specs are the source of truth for everyone building the product, including the LLM.

With the proper setup, it is entirely realistic to expect to be contributing to a codebase as a non-technical person.

With enough time and patience, you can start to understand the codebase and implement changes yourself, rather than simply relying on Claude to bail you out every time.

One day, you might even expect an AI agent to ship your ticket whilst you sip your coffee.

If you’re a PM and worried about what AI is going to do to your job, the key is to realize that the job itself is changing.

But that’s also the case for everyone else.

The great thing is that the core skills required for an excellent PM are even more valuable in this new world.

As we predicted in a previous post, the companies that are working in this way will need more, not fewer PMs.

And it turns out that prediction is working out rather well:
Long live the spec!

William Gibson, the science fiction writer who coined the phrase “cyberspace,” once said:
The future is already here—it’s just not very evenly distributed.

I’m reminded of this when I think about what is and is not possible with AI.

Today, AI's gains are profoundly uneven.

Some things—generating code, text, images—have made quantum leaps.

They operate at AI speed.

Other things—talking to customers, discovering their needs, convincing them to buy—still move at human speed.

This uneven distribution is reshaping product teams.

The spotlight is shifting from implementation work to understanding work.

The core skills that have always set apart the best PMs—understanding user needs, defining problems clearly, designing elegant solutions—have become exponentially more valuable.

The best PMs turn those insights into specs—specifications that align teams, guide implementation, and serve as the lasting artifact in an increasingly automated development world.

Thanks for reading Ravi on Product!

Subscribe for free to receive new posts and support my work.

A guest post by
Danny Martinez
✍️ Writing about hiring
Subscribe to Danny