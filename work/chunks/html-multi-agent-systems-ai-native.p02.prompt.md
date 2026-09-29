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

AI architecture without domain knowledge produces output that investigates the wrong things.

The breakthrough happens when you combine both: knowing what database connection pools do under load (domain) with building agents that can coordinate pool health checks with deployment timeline analysis and upstream service validation: all running in parallel without stepping on each other (AI systems).

At Resolve AI, our team includes engineers with over two decades of experience in production systems, founders who co-created OpenTelemetry (one of the most impactful open-source observability projects in the ecosystem) and researchers with deep artificial intelligence expertise who are the minds behind Google DeepResearch and Gemini Agents.

This combination lets us build systems that don't just understand that "payment failures are bad" but know to check connection pool metrics and correlate with upstream service degradation.

All the while managing complex agent orchestration that prevents circular investigations and maintains coherent narrative threads across parallel execution paths.

About Resolve AI
Resolve AI is your always-on AI SRE that helps you resolve incidents and run production.

With Resolve AI customers like Salesforce, Zscaler, and Coinbase have increased engineering velocity and systems reliability by putting machines on-call for humans and letting engineers just code.

Learn more about AI-native engineering workflows at resolve.ai.

AI SRE Buyer's Guide
Learn how to evaluate and adopt AI SRE in production.

Download
Spiros Xanthos
Founder and CEO
Spiros is the Founder and CEO of Resolve AI.

He loves learning from customers and building.

He helped create OpenTelemetry and started Log Insight (acquired by VMware) and Omnition (acquired by Splunk), most recently he was an SVP and the GM of the Observability business at Splunk.

Gabor Angeli
Research Engineer
Gabor Angeli brings extensive AI expertise, most recently at Google DeepMind and Square.

His work on products like Gemini and Square Assistant touches millions of users daily.

He joined Resolve AI to build Agentic AI systems that help engineers understand and navigate production systems.

Bharat Khandelwal
Research Engineer
@ Resolve AI
Bharat is a Research Engineer at Resolve AI, where he builds agentic systems that enable large language models to debug and operate production software infrastructure.

Prior to Resolve, he led machine learning initiatives at WorldQuant, designing transformer-based architectures for macroeconomic forecasting and incorporating LLM-driven sentiment signals from unstructured data.

He has also worked at Moveworks on enterprise NLP systems and at Tower Research Capital, where he developed low-latency ML strategies for high-frequency trading.

Bharat holds an M.S.

in Computer Science from Stanford University, with a specialization in Artificial Intelligence, and a B.Tech.

(Honors) in Computer Science from IIT Bombay.

Content
AI for prod ebook
Learn how top engineering teams use AI to run production.

Download
Spiros Xanthos
Founder and CEO
Spiros is the Founder and CEO of Resolve AI.

He loves learning from customers and building.

He helped create OpenTelemetry and started Log Insight (acquired by VMware) and Omnition (acquired by Splunk), most recently he was an SVP and the GM of the Observability business at Splunk.

Gabor Angeli
Research Engineer
Gabor Angeli brings extensive AI expertise, most recently at Google DeepMind and Square.

His work on products like Gemini and Square Assistant touches millions of users daily.

He joined Resolve AI to build Agentic AI systems that help engineers understand and navigate production systems.

Bharat Khandelwal
Research Engineer
@ Resolve AI
Bharat is a Research Engineer at Resolve AI, where he builds agentic systems that enable large language models to debug and operate production software infrastructure.

Prior to Resolve, he led machine learning initiatives at WorldQuant, designing transformer-based architectures for macroeconomic forecasting and incorporating LLM-driven sentiment signals from unstructured data.

He has also worked at Moveworks on enterprise NLP systems and at Tower Research Capital, where he developed low-latency ML strategies for high-frequency trading.

Bharat holds an M.S.

in Computer Science from Stanford University, with a specialization in Artificial Intelligence, and a B.Tech.

(Honors) in Computer Science from IIT Bombay.

Related Post
Fireside Chat: How FinServ Companies Optimize Cost with AI for Prod
Hear AI strategies and approaches from engineering leaders at FinServ companies including Affirm, MSCI, and SoFi.

Technology
How to Evaluate a Production Ready AI SRE
Learn how to evaluate an AI SRE to ensure they run in your unique production environments.

This guide explains the five agentic pillars, six key evaluation dimensions, and enterprise readiness criteria that separate production-ready AI SRE from experiments.

Beyond the Build: Accelerating Engineering Velocity with Agentic AI
100 Engineering software engineering executives joined Resolve AI and other luminary leaders to discuss the accelerated evolution of agentic AI in software engineering from coding to managing production systems.