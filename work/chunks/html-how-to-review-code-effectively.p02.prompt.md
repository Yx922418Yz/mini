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

Possible improvements:
“This won’t work because [X], see this relevant issue: [issue link].”
“This was tried before in [pull request link] and it didn’t work because of [X].”
“If you run into problems with [X], you could try [alternative approach] instead.”
“I think this fixes a bug.” – I love the callout, but is there any additional context, such as an issue link, that could make this more clear?

Possible improvements:
“I think this fixes [issue link].”
“Is this fixing the bug from [issue link]?”
“This looks like the bug we ran into with [link to failing build].

Thanks for the fix!”
How to give a good code review
Ask questions
I think of the pull request author as the person with the most context on the changes their pull request is making.

I can point out problems I see based on my history—my experience working in a Ruby on Rails monolith, in TypeScript, or with a database that gets a lot of traffic—but I trust the author’s answers to my questions.

I treat their understanding of the particulars as better than mine.

I also love to ask questions that involve the assumptions made in the code.

What is the shape of the data they’re working with?

Does data exist that doesn’t match that shape?

Does the code respond to that well?

Is the code resource intensive?

Will it perform well?

As a reviewer, my favorite response is for the author to provide an automated test that verifies the behavior in those scenarios.

My second favorite response is empirical data, such as a query from our data warehouse or a Datadog graph that shows why those scenarios aren’t a problem.

As a pull request author, I appreciate receiving questions.

When someone asks a question, it makes space for me to explain why I’m confident about my change, citing issues, queries, or graphs as necessary.

It also lets me share my knowledge and experience with others.

The author not only sees my responses, but also other reviewers and future readers who may be tracking down context on a past decision.

Offer affirmations
Beyond asking questions, it’s good practice to comment on the parts of the pull request that you agree with.

These comments can highlight that you read and understood what was being changed, or that you verified some assumption in the code.

Here are a few examples:
“Looks like this matches the pattern used in other classes in this module.”
“Thanks for adding a test for this!”
“This is much more readable than before.”
It’s also just nice being on the receiving end of such comments, in my experience.

Receiving a code review can sometimes feel draining.

When I’m fielding questions and suggestions from several parties, it can be a good boost to get a few comments that don’t ask anything of me and instead support and acknowledge the work I’ve already put in.

Be aware of biases and assumptions
It’s easy to let your biases about the reviewer, or the area of code they’re changing, affect your review.

You get used to someone working in an area or having some level of seniority and assume they know what they’re doing—but everyone makes mistakes.

Your eyes on their changes, your questions checking their assumptions or validating your own, can catch a problem before it’s deployed.

I’m big on writing tests because they take some of the bias out.

When you write a test to check that code works properly, you don’t have to take the author’s word for it, you just look at whether the test passed—provided you get the test right, of course.

😅
I’m also big on junior developers asking senior developers questions in code review, even if they think their question is silly or has an obvious answer.

If it’s not obvious to you, that’s valid.

It won’t be obvious to someone else either!

Ask the question, make the space for the author to write down their answer, and preserve that bit of education for those who come later.

To approve or not
I see my review as a blocking gate that can stop another person from improving our product, so I withhold approval conscientiously.

I will often have personal preferences and suggest optional changes I’d like to see the author make, but I won’t withhold an approval based on those alone.

If I have suggestions for someone’s pull request, but their pull request as it is won’t break production, negatively impact users, or otherwise cause problems, I will approve with those comments.

The author can choose to address my feedback before they merge their pull request, or they can follow up in another branch.

Keep in mind the importance of your suggestion when you’re reviewing code.

Is it worth delaying the ship to get your suggestion addressed?

Is it worth the whole cycle of the author seeing your feedback, making the suggested changes, waiting for CI, a re-review, deployment and finally merging?

If a suggestion’s absence isn’t going to make someone’s day worse, let the author decide if or when to make the suggested change.

The ‘Request changes’ option stops a pull request from being merged until the reviewer comes back and approves it.

I very rarely use it, as it usually feels too heavy-handed.

I trust my team to know when to approve a pull request, so a teammate’s approval is fine in place of mine.

Likewise, I trust the pull request author to respect my feedback and consider it, not just blindly merging because someone else approved but I didn’t.

About the only time I’ll choose the ‘Request changes’ option is when I think there is an immediate security issue and I’m worried they won’t see my concern before merging.

How to get the most out of code reviews
Review your own code
GitHub Senior Software Engineer Paul Smith taught me to review my own pull request before asking others to do so, and I would advise you to do the same.

Take a first pass and leave comments inline on non-obvious changes or ones you would ask about if you saw them in someone else’s pull request.

A self-review can also help determine if a pull request is too big and would benefit from being split up.

Shout-out: if you care about keeping your pull requests small, you can make use of lerebear/sizeup-action to automatically apply a label to pull requests indicating their complexity and size.

Be welcoming of post-merge reviews
If I happen to merge a pull request before someone gets a chance to review it, I still welcome their review.

If my pull request broke something or had unintended consequences, commenting as much on the pull request leaves that breadcrumb trail to help future readers track down what happened!

If I receive a review on a merged pull request, I’ll address the feedback like I would have before the pull request landed.

Maybe that’ll be a comment to explain my perspective, maybe it’ll be additional pull requests to iterate on the code I originally shipped.

Maybe it’ll be opening new issues to capture additional work to be done.

Use draft pull requests
When you create a new pull request, you have the option to set the pull request as a draft.

I lean heavily on the draft stage to indicate whether or not I want reviews.

For example, if a required CI build is failing or I’m just not finished yet, I’ll keep it as a draft.

I tend to expect the same from others’ pull requests: if it’s a draft, I assume the author isn’t ready for reviews.

If it’s marked as ready for review, I assume that getting enough approvals is all that’s preventing them from deploying the pull request.

The draft status implies that a pull request is not finished, so I move pull requests back to draft when resolving merge conflicts or addressing reviewer feedback.

If I have to modify the code, I’ll mark my pull request as a draft first so as not to overwhelm people who have already reviewed it.

When I move it back to ‘ready’, it sends a GitHub notification to those reviewers so they can look at it again.

Be gracious
The expression, “You can catch more flies with honey than vinegar,” comes to mind.

I want reviews on my pull requests, so I like to reply to comments on my pull requests—especially if I disagree with the reviewer.

Even if I don’t write a reply to a review comment, I’ll often react with a 👍 to indicate I agree or a ❤ to say thank you.

I want reviewers to trust that their suggestions won’t be forgotten, so I keep them in the loop via comments.

If I agree with their suggestion—to go further refactoring existing code, for example—I may say as much while also pushing back about making that change in the current pull request.

When I address their feedback in a later pull request, I come back to provide a link and let the reviewer know their feedback didn’t go unheard.

I’ll also tag them in later pull requests where I implement the suggested changes and include a note saying “This addresses @so-and-so’s feedback from <previous pull request URL>.” This both provides context for other readers and acts as a shout-out to the original reviewer, giving them credit for the idea.