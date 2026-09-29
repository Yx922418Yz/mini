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

Otherwise, most agents will assume the old patterns from these libraries due to knowledge cutoffs in the pretrained base models.

A good agent can overcome this if you point it to docs, but you must be mindful of this (remember, the agent doesn't even know that there are new versions of these libraries).

Practical Considerations
Managing Time and Minimizing Losses
Not all times you use an agent will result in success.

In 2025, there is some real variance in the outcomes of these agents.

Part of the job involves learning how to use agents in such a way to maximize the chance of running into successful outcomes while minimizing wasted time and tokens.

Be willing to cut your losses earlier
A common mistake for people who are new to using agents is that they commit to making an interaction successful, even when an agent's work is veering off track.

If you ever find yourself thinking "it's ignoring my instructions" or "this thing is going in circles", you should be ok discontinuing that conversation or manually taking over.

Sending more messages is more likely a sign of the inherent complexity of your task being higher than the agent's capabilities rather than some simple mistake that can be corrected.

Diversifying your experiments
If you're new to working with agents, we recommend diversifying your bets at the start.

Try a range of different prompts and ideas.

Double down on the types of tasks you see the agents naturally performing well on - and cut your losses on the ones they don't.

Don't feel a need to force your agents to find success every time.

Start fresh when you aren't making progress
Starting over is the right answer a lot more often with agents than with humans.

If you've given an agent a task and it is struggling to address feedback or correct course, starting fresh with a new agent and all of the instructions up front can often get to success much faster.

The ability of an agent to correct a messed-up environment is much worse than its ability to spit out fresh code from scratch.

Practical Considerations
Security and Permissioning
Create accounts for your agent
A throwaway email is helpful for safe testing of sites.

Create custom IAM roles for your agent if it needs to access cloud resources.

Give it a development / staging environment
Ideally the agent uses the same testing setup as the engineers on your team.

We suggest avoiding giving access to production services entirely.

When using remote agents, you can run fully isolated test environments on the agent's remote machine.

Readonly API keys
Where possible, give it readonly access.

We find it is still helpful for humans to manually run any script that interacts with outside services.

Practical Considerations
Big Changes Ahead
We firmly believe that software engineers aren't going anywhere.

Even as coding agents become smarter and more capable, deep technical expertise and intimate knowledge of your codebase remain invaluable.

True ownership of your projects, your systems, and your code is more critical now than ever.

On our team today, engineers are expected to oversee multiple systems while still maintaining deep understanding and thoughtful judgment.

As automation amplifies your impact, the ability to juggle parallel tasks won't just become possible; It'll become essential.

We're excited to share the insights we've gathered while preparing our own organization for this shift, so you and your team can also thrive in the evolving world of software development.