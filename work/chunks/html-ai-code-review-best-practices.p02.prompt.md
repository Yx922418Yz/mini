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

By implementing the best practices outlined in this guide and approaching AI code review as a complement to human expertise rather than a replacement, teams can significantly improve code quality, security, and developer productivity.

Remember that AI code review is most effective when it's part of a comprehensive quality strategy that includes testing, documentation, and thoughtful human oversight.

The goal is not to eliminate human judgment but to enhance it by automating routine checks and providing valuable insights.

Frequently asked questions
How accurate are AI code review tools?

AI code review tools typically achieve 70-90% accuracy for common issues like syntax errors, style violations, and basic security vulnerabilities.

However, accuracy varies significantly based on the complexity of the issue and the specific tool.

For architectural decisions and complex business logic, human review remains essential.

Can AI code review replace human reviewers entirely?

No, AI code review should complement rather than replace human reviewers.

While AI excels at catching routine issues and maintaining consistency, human reviewers are still needed for architectural decisions, business logic validation, and complex problem-solving.

The most effective approach combines AI automation with human expertise.

How do I convince my team to adopt AI code review?

Start with a pilot program involving enthusiastic team members.

Demonstrate clear value by showing time savings, improved code quality metrics, and reduced bug rates.

Address concerns about job security by positioning AI as a productivity tool that allows developers to focus on higher-value work.

How do I handle false positives from AI code review?

Implement a feedback loop where developers can mark suggestions as false positives.

Most tools allow you to tune sensitivity settings and create ignore patterns for specific code patterns.

Regular review of false positives helps improve the system's accuracy over time.

Is my code secure when using AI code review tools?

Security depends on the tool and deployment model.

Cloud-based tools may process your code on external servers, while on-premises solutions keep code within your infrastructure.

Review each tool's data handling policies and consider your organization's security requirements when choosing a solution.

Will AI code review slow down my development process?

Initially, there may be a slight learning curve, but most teams see net time savings within 2-4 weeks.

AI catches issues early, reducing debugging time and review cycles.

The key is proper configuration to focus on high-impact issues rather than overwhelming developers with minor suggestions.

How do I integrate AI code review with my existing CI/CD pipeline?

Most AI code review tools offer API integrations and webhook support.

You can typically integrate them as a step in your CI pipeline or as automated checks on pull requests.

Start with basic integration and gradually add more sophisticated workflows as your team becomes comfortable.

How do I balance AI suggestions with team coding standards?

Configure the AI tool to align with your existing coding standards and style guides.

Most tools allow customization of rules and can learn from your codebase patterns.

Regularly review and adjust configurations based on team feedback and evolving standards.

How do I measure the success of my AI code review implementation?

Track metrics like reduction in production bugs, time saved in code reviews, developer satisfaction scores, and code quality improvements.

Set baseline measurements before implementation and compare results after 3-6 months of usage.

The AI is missing important issues that human reviewers catch.

How can I improve this?

This is common and expected.

AI tools excel at pattern recognition but may miss context-specific issues.

Supplement AI review with human oversight, especially for complex logic and architectural decisions.

Use AI feedback to improve the tool's configuration and consider custom rules for domain-specific patterns.

Related guides
Balancing code quality and delivery speed in software teams
This guide explores current and timeless best practices to optimize code standards and team producti...

Best practices for pair programming with AI assistants
This guide explores essential best practices for pair programming with AI assistants, including code...

Existing code review tools for TypeScript
This guide explores the best code review tools for TypeScript, focusing on enforcing best practices ...

Last modified 11 months ago
0 min read
On this page
Understanding AI code review
Benefits of AI code review
Implementing AI Code Review
Best practices for AI code review
6.

Performance optimization
Popular AI code review tools
Other notable tools
Measuring success
Common challenges and solutions
Conclusion
Frequently asked questions
Share
Git inspired
Graphite's CLI and VS Code extension make working with Git effortless.

Learn more
Built for the world’s fastest engineering teams, now available for everyone.

Request a demo
Start free trial