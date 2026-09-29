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

Sarah Vessels·@cheshire137
July 23, 2024
|
16 minutes
Share:
As a staff engineer at GitHub, code review is one of my main focus areas in my day to day work.

Over the past eight years, I’ve reviewed more than 7,000 pull requests.

Why so many?

Because code review is crucial to building good software and another set of eyes can often spot issues you would have otherwise missed.

I see code review as one of the most important aspects of my job.

In fact, whenever I see that a teammate has a pull request ready for code review, I prefer to drop whatever branch I’m working on to review their proposed changes instead.

After all, their pull request has already passed the continuous integration (CI) gauntlet and met the bar for their own judgment of “done,” so it’s probably closer to being shippable than my own in-progress work.

I’d rather get their code over the finish line than churn an unknown amount of time more to finish my code.

The sooner I provide feedback — “This can be nil and cause an error,” “This looks like an n+1 query,” “It would be great to have a method signature on this” — the faster that feedback can be addressed and the bug squashed or feature shipped.

I’d like to share how I approach code review in hopes that we can all ship better code.

What is code review?

Strictly speaking, code reviews—via pull request reviews on GitHub—allow collaborators to comment on the changes proposed in pull requests, indicate their approval of the changes, or request further changes before the pull request is merged.

I see a pull request as the beginning of conversation.

I read it as the author saying “I think this improves on what we have today.” Code review is a great opportunity to shape the product’s implementation.

As a code reviewer, my job is to go back and forth in discussion with the author to improve their code by asking questions, questioning assumptions, and generally serving as a second set of eyes.

Fine-tune your code review process
How to find pull requests for review
I live in my GitHub notifications inbox.

It’s one of just a few tabs I pin in my browser, so it’s always available.

Any time I’m waiting on CI, I’m in between tasks, starting my day, or generally have a spare moment, I like to check my inbox.

I find most of the pull requests I review there.

Teams at GitHub tend to have a particular Slack channel they treat as home base, and that’s a good place to share ready-for-review pull requests—it’s one of the other main ways I discover pull requests.

I also have good luck using the GitHub Slack integration to subscribe a Slack channel to new pull requests relevant to my team.

To filter which pull requests show up in Slack, I use a label specific to the team, then a ‘subscribe’ command in Slack like /github subscribe your/repo pulls +label:"your-team-label".

I like to search for outstanding pull requests that may need review with queries like is:open archived:false is:pr org:github -is:draft team-review-requested:github/relevant-codeowner-team.

With that query, I find open, unarchived pull requests within the GitHub organization that are not drafts and have relevant codeowner teams as a requested reviewer.

I usually will omit the review:required search qualifier because I’m interested in reviewing a pull request even if a teammate has already reviewed it.

After all, reviewing code not only helps the author, it helps me stay up to date with changes affecting code I’m responsible for.

Use reviewer teams to manage notifications
You don’t want code changes to ping such a large team that everyone on the team assumes reviewing the change isn’t their responsibility.

That can result in pull requests that either languish unreviewed or get merged before they should, because key reviewers missed them in a deluge of notifications.

Both of these scenarios affect the quality of the product.

I recommend honing the number of code owner teams you’re on, if you’re able, to keep your notifications manageable.

That way, pull requests that land in your inbox aren’t just noise, they’re actually something you feel you should review.

While big, catch-all code owner teams can be okay as a fallback option, they aren’t great as a first-line default for automatic review requests.

Keep your repository’s CODEOWNERS file well organized, with well-defined code boundaries to go along with it, to limit notifications and help reviewers avoid notification fatigue.

Another way of limiting team-based notifications is to create a first responders team and then use automation to add and remove team members based on a schedule.

This can let your team focus on their day-to-day code base, while scheduled first responders get notified of pull requests in your team’s service areas.

Using the PagerDuty API, for example, you can determine who is a first responder on a given day.

You can then use the Octokit library to add and remove team members.

Standardize code reviews across teams with automation
Repository-level configuration and automation, such as using a CODEOWNERS file and branch protection rules, can be helpful to enforce review process standards across teams.

Other standards, such as what’s worth commenting on in a pull request, have to be maintained by us humans.

Document how code reviews work within your team to make sure anyone providing a code review or submitting a pull request knows how to get their pull requests reviewed, the expected turnaround time for review, and what automation is in use to facilitate review.

Some teams use a project board to keep track of which pull requests come in for review; I’ve seen this work well for a team that manages a shared API, an area often modified by those outside the team.

Other teams depend on GitHub notifications alone, which I’ve seen work well when code ownership is tightly scoped and the team is disciplined about reviewing pull requests as they come in.

If you follow a process unique to your specific team, automation can help communicate expectations with those outside your team.

For example, if many other teams depend on your team’s reviews, you can use a bot to automatically leave a comment on any pull request where your team’s review is requested, to tell the author when they can expect to hear from you.

What makes a code review good or bad?

Good code reviews add clarity and push code toward a better state than where it started.

As a reviewer, clarity in communication is key.

You’ll want to make clear which of your comments are personal preference and which are blockers for approval.

Provide an example of the approach you’re suggesting to elevate your code review and make your meaning even clearer.

If you can provide an example from the same repository as the pull request, even better—that further supports your suggestion by encouraging consistent implementations.

By contrast, poor code reviews lack clarity.

For example, a blanket approval or rejection without any comments can leave the pull request author wondering if the review was thorough.

Even just reiterating your understanding of the pull request author’s intention with your approval can surface whether you and the author have the same understanding.

A code review that is unclear about when its suggestions should be implemented can also be a poor experience for the author.

It’s fine to note that existing, unchanged code should be refactored, or an additional case should be handled, but it’s important to specify whether those are precursors to approval.

If the pull request is okay to land without your suggestions, make sure to say so.

It may be safer to keep a small diff and ship those changes separately, as separate pull requests.

Here’s a code review comment that displays specificity and clearly communicates suggested implementations:
“I see your new method matches the existing style in this file, taking [X] parameters.

Having that many parameters hurts readability and implies the function is doing too much.

What do you think about refactoring this method and the existing ones in a later pull request to reduce how many parameters they take?”
What this comment does well:
Provides specific details.

References specific code or issues.

Suggests a resolution to the problem.

Cites evidence or provides an explanation
On the other end of the spectrum, here are some examples of review comments that could be better:
“I don’t like this.” – What doesn’t the reviewer like?

Do they have an alternative in mind that they could explicitly state?

Possible improvements:
“This line is doing a lot, could we simplify it to improve readability?”
“I think this will have performance problems because of an n+1 query.”
“Could we use the [preferred framework]’s solution for this instead of writing a custom implementation?”
“This won’t work.” – Why won’t the changes work?