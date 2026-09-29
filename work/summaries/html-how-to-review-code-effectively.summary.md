# 如何有效地做代码评审（导读）

> 来源：Sarah Vessels（@cheshire137），staff engineer at GitHub · 文章 id：`html-how-to-review-code-effectively` · 原文约 19.8K 字符

## 核心主张
GitHub 的 staff engineer Sarah Vessels 在八年里审阅了 7,000 多个 pull request，她认为代码评审（Code Review）是构建好软件最关键的一环，并把每个 PR 视为一次对话的开端。文章给出如何发现待审 PR、如何为团队定制评审流程、如何写出清晰有效的评审意见，以及如何从代码评审中获得最大收益的实用方法。

## 关键要点（原文引用）
- 作者经验：staff engineer at GitHub，过去八年 review 了超过 7,000 个 pull request；认为「另一双眼睛」常能发现你本会遗漏的问题。
- 核心理念："I see a pull request as the beginning of conversation." ——通过提问、质疑假设与作者来回讨论，共同改进代码。
- 尽早给出反馈，例如 "This can be nil and cause an error"、"This looks like an n+1 query"、"It would be great to have a method signature on this"。
- 发现待审 PR 的方式：常驻 GitHub notifications inbox；用 GitHub Slack integration 订阅频道，例如 `/github subscribe your/repo pulls +label:"your-team-label"`。
- 搜索待审 PR 的查询：`is:open archived:false is:pr org:github -is:draft team-review-requested:github/relevant-codeowner-team`；通常省略 `review:required`，因为即使别人审过也值得再读一遍。
- 管理通知：精挑自己加入的 code owner teams，维护好 CODEOWNERS 文件与清晰的代码边界；可用 PagerDuty API 加 Octokit library 做轮值 first responders 的自动增删。
- 好评审的标准：清晰沟通，明确哪些是个人偏好、哪些是 approval 的 blocker；尽量给出所建议实现的示例，最好取自同一仓库。
- 反例：单说 "I don't like this." 或 "This won't work." 毫无信息量；应补充原因与链接，如 "This won't work because [X], see this relevant issue: [issue link]."、"This was tried before in [pull request link] and it didn't work because of [X]."。
- 提问（Ask questions）：把作者当作最了解改动的人，就数据形状、资源消耗、性能等发问；最喜欢的回答是自动化测试（automated test），其次是经验数据（如 data warehouse query 或 Datadog graph）。
- 给予肯定（Offer affirmations）：如 "Thanks for adding a test for this!"、"This is much more readable than before."，这类不索取任何东西的评论能提升作者的体验。
- 警惕偏见：不要因对方资历高或熟悉某块代码就默认其不犯错；推崇写测试以去除偏见，并鼓励 junior developer 提问。
- 是否批准：把评审视为可能阻挡他人改进产品的 gate，很少使用 "Request changes"；只有认为存在即时安全问题（immediate security issue）且担心作者没看到时才会用。
- 提升收益的实践：先 review 自己的 PR（GitHub Senior Software Engineer Paul Smith 的建议）；用 `lerebear/sizeup-action` 给 PR 自动打上规模/复杂度标签；善用 draft pull request 表达是否准备好被审；用 👍 或 ❤ 表达同意与感谢。
- 接受 merge 后的评审：即使 PR 已合并也欢迎事后评论，为未来读者留下 breadcrumb trail；据此可回复解释、再开后续 PR，或新建 issue 跟踪。

## 术语与译法
- `Pull Request` → 拉取请求
- `Code Review` → 代码评审
- `Repository` → 仓库
- `Commit` → 提交
- `Continuous Integration` → 持续集成
- `Unit Test` → 单元测试
- `Refactor` → 重构

## 结论
代码评审是一项需要刻意练习的沟通技能：把 PR 当作对话、用具体且可执行的反馈替代主观评价、按重要性克制地 withhold approval，并通过自审、定标准、善用工具把它变成提升整个团队交付质量的杠杆。
