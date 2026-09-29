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

The spec is dead, long live the spec!

Prototypes are the new specs and specs are the new....

source code?

Ravi Mehta and Danny Martinez
Jul 31, 2025
Over my career, specs have gotten shorter and shorter.

When I started at Microsoft, the worth of a PM was measured in the weight of their specs.

Years later, at Tripadvisor, we mythologized the PM who brought a spec—scribbled on a napkin—to Product Review.

Product teams often treat specifications like paperwork—a necessary evil before the "real work" of shipping.

Engineers get celebrated for elegant code, designers for beautiful UX.

PMs get kudos for delivering impact.

But specs?

They’re typically rushed through, tossed aside, forgotten.

Thanks for reading Ravi on Product!

Subscribe for free to receive new posts and support my work.

This was always a mistake.

In my Product Competency Toolkit, Feature Specification sits at the top—first among twelve competencies—for a reason.

It underpins Product Execution, along with Product Delivery and Product Quality.

Flawless execution is the foundation of good product management, and a great spec is the starting line.

Today, the way we build is shifting.

Engineers are getting faster—much faster.

AI can turn rough ideas into working code in minutes.

The bottleneck is no longer building.

It's knowing what to build, and aligning the team around those requirements.

Suddenly, the humble specification isn't ephemeral paperwork.

It’s the foundation of product management—it's becoming the source code itself.

Why PMs are suddenly the bottleneck
In his recent talk Building Faster with AI, Andrew Ng noted an unprecedented trend:
"For the first time in my life that I saw managers proposed to me having twice as many PMs as engineers.

I still don't know if this proposal is a good idea, but I think it's a sign of where the world is going." —Andrew Ng
This validates what we predicted in our previous post: as engineers deliver many times faster with AI, companies need more PMs to support those productive engineers, not fewer.

As product delivery accelerates, that puts intense pressure on every other aspect of product management—understanding customer needs, crafting the right features, validating impact.

And all of that pressure gets focused into one artifact—the spec.

Specs—the new source code
In traditional software development, programmers write human readable “source code” which gets compiled into highly optimized, machine readable “object code”.

The “object code” (also known as a binary) is a byproduct that can be recreated with the source code.

The source code is literally the source of truth.

Sean Grove, from OpenAI, has a provocative thesis.

In his recent talk, The New Code, he argues that a well-written prompt (i.e., the spec) is the new source code.

Seen in that light, we’re doing AI development backwards.

We craft careful prompts to communicate our intentions to models.

The AI generates code.

Then we keep the code and throw away the prompt.

"This feels like you shred the source and then you very carefully version control the binary," Grove observes.

Think about that.

In traditional programming, source code is sacred.

The source contains comments, structure, and documentation—everything needed to understand and modify the system.

The binary is just a downstream artifact.

But with AI, we've flipped this relationship.

We treat the generated code as the artifact worth keeping and the specification—the prompt—as disposable.

Grove argues this gets it exactly backwards.

Code, even elegant code, is what he calls a "lossy projection" from the specification.

Just like decompiling a binary won't give you the original comments and variable names, reading code won't tell you the full intent behind it.

The specification, however, contains everything.

A sufficiently robust spec can generate "good TypeScript, good Rust, servers, clients, documentation, tutorials, blog posts, and even podcasts."
“A sufficiently robust spec can generate good TypeScript, good Rust, servers, clients, documentation, tutorials, blog posts, and even podcasts.” —Sean Grove, OpenAI
More importantly, specifications do something code cannot: they align both humans and machines on shared goals.

Grove puts it simply: "A written specification effectively aligns humans and is the artifact that you use to communicate and discuss and debate and refer to and synchronize on."
He predicts: "In the near future, the person who communicates most effectively is the most valuable programmer.

And literally, if you can communicate effectively, you can program."
The new scarce skill isn't coding.

It's writing specifications that fully capture intent and values.

For product managers, this should sound familiar.

It's what we've always done—just now the machines are listening too.

Wait, didn’t prototypes kill the spec?

Until recently, the product lifecycle had to start with the spec (or PRD or concept doc or napkin) that gets the initial wireframing, designing, prototyping, and MVP development under way.

The traditional approach felt like a necessary evil.

Engineers built basic MVPs to get something—anything—into customers' hands.

"If you're not embarrassed by the first version of your product, you've launched too late" became gospel.

Our entire approach to building products has recently undergone a significant shift, and in this new world, the spec is often the output, not the input.

Today, you don't need to ship a single line of code to get a prototype into customer hands.

Tools like v0, Lovable, and Replit let you build functioning prototypes in hours, not weeks.

No engineering required.

This isn't just faster—it's fundamentally different.

Armed with a "vibe coded" prototype, you can gather real customer feedback before writing a single line of your feature spec.

You can test assumptions, iterate on flows, refine interactions.

The old workflow looked like this: vague idea → wireframes → designs → engineer-built MVP → customer feedback → painful spec revision → wireframes → designs → rebuild → pray.

The new workflow: vague idea → rapid prototype → customer feedback → crystal-clear spec → AI-assisted implementation.

Prototypes haven't killed the spec.

They're making specs better.

Spec-driven development in action
Let's look at a hands-on example of how this all plays out.

Danny Martinez is the founder of decimals, a platform (in stealth) that enables experts in the creator economy to place talent from their network into jobs.

Are you an AI-first PM looking for a new opportunity?

Drop in your details and we’ll let you know when we come across interesting opportunities.

Are you a company looking to hire an AI-first PM?

Apply to our talent network and we’ll share a curated shortlist of candidates.

Danny is going to walk us through their spec-driven development process—a process that has had two impacts:
massively improved communication with engineering for the bigger features, and
enabled Danny, despite having no prior coding experience, to go all the way from detailed spec to live feature for the smaller stuff.

Over to Danny…
Here’s a recent example I worked on.

For context, we’re building a product that enables expert influencers to place candidates from their networks into jobs.

After shipping a new landing page, we needed to give our experts a quick way of accessing the link to their own page.

We need a button in the header that directs to the company-apply page.

I'm focused on the emails at the moment.

This is vibe code-able if you can pick it up please.

This was from my co-founder, referring to a simple button that needed to be shipped.

Easy enough, and precisely the kind of thing that a non technical person can now ship themselves.

Here’s the setup and steps for how this got shipped within a couple of minutes:
Project management tool: Linear
IDE: VS Code
Extension: GitHub Copilot Pro
Model: Claude Sonnet 4
MCP Server: Linear MCP server to allow Linear tickets to be accessed via Copilot
Let’s take a look at the steps in the process (follow along in the Loom video above):
Generate a Linear ticket out of the Slack message from my co-founder (00:14)
Clarify what I want the new copy to be in the ticket above (00:25)
Open up Copilot and prompt Claude to open up the Linear ticket (01:18)
Prompt Claude to review the ticket and analyse it relative to the codebase (01:52)
Prompt Claude to create a branch and implement these changes (02:30)
Test the changes to ensure they’re working as expected.

(02:52)
Open a pull request (PR) on GitHub to ship these changes into the codebase (03:55)
Wait for an engineer to review/approve the PR
Zooming out, the true power of this setup comes into focus.

Yes, this is a trivial example, but the point remains: a non-technical person can now go between Linear tickets, a codebase, and an engineer, all with a couple of prompts to Claude via GitHub Copilot.

And again, the critical part of all of this isn’t the code itself: it’s the spec.