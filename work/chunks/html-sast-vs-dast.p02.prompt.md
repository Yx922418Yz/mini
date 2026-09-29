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

Software types supported
Supports various types of software, including web applications, web services, and thick clients.

Supports web applications and web services but does not typically support other software types.

Stage in SDLC
Performed early in the software development life cycle.

Conducted later in the SDLC, often during or after deployment.

Vulnerabilities detected
Identifies coding flaws, such as: SQL injection, cross-site scripting (XSS), buffer overflows, etc.

Detects runtime issues, such as server configuration errors, denial-of-service vulnerabilities, and application-level flaws.

Cost of fixing vulnerabilities
Less expensive since issues are identified early in the SDLC.

More expensive as vulnerabilities are found later, often requiring emergency fixes in order to deploy on time.

Runtime and environment issues
Cannot detect runtime-specific or environment-related vulnerabilities.

Can identify vulnerabilities that appear only during runtime or due to environmental factors.

Depth vs.

breadth
Provides deep insights into code-level vulnerabilities.

Offers a broad view of the application's external security risks.

Integration with tools
Integrates with IDEs and CI/CD pipelines for automated static analysis.

Integrates with CI/CD pipelines for continuous runtime testing.

False positives and negatives
Higher chance of false positives due to in-depth code analysis.

Lower false positives but higher risk of false negatives due to limited internal visibility.

Technology dependency
Relies on programming languages and frameworks; requires compatibility with the tool.

Independent of application frameworks as they interact with the application externally.

Pros and cons of SAST and DAST
Pros of SAST
Identifies security vulnerabilities early in the software development life cycle.

Analyzes the codebase, including basic functions and complex branches.

Operates directly on the source code without requiring the application to run.

Provides real-time feedback with comprehensive insights, such as the exact location of vulnerabilities.

Generates exportable reports that can be tracked using dashboards.

Supports automation so that it is faster and more efficient than manual code reviews.

Cons of SAST
Often generates a large number of false positives.

Therefore, it may require manual reviews.

Cannot identify runtime or environment-specific vulnerabilities, such as configuration errors.

Requires tools specific to each programming language so that maintenance is complex.

Struggles with understanding external libraries, APIs, and REST endpoints.

Pros of DAST
Identifies vulnerabilities that only appear during application execution.

Operates externally and no access to source code is required.

This is effective for testing third-party applications or compiled code.

Simulates actual attack scenarios and identifies risks missed by SAST.

Works independently of the application's programming language.

Evaluates the entire application and system.

This includes memory consumption, resource usage, and third-party interfaces.

Cons of DAST
Focus only on the outer layers of the application, which may miss vulnerabilities in deeper layers.

Applied later in the SDLC so that fixes are more expensive and time-consuming.

Miss certain vulnerabilities that SAST tools can identify through source code analysis.

As an example, consider a web application that uses an insecure random number generator (e.g., Math.random() in JavaScript) to create session tokens.

DAST may miss this flaw because it only tests runtime behavior.

(But SAST can detect it.)
Require custom infrastructure for large projects and multiple instances of the application to run in parallel and therefore resource intensive.

When should I use SAST vs.

DAST?

SAST and DAST play complementary roles in securing SDLC.

Understanding when to use each helps to have comprehensive security coverage.

When to use SAST
During early development phases.

Developers use SAST to identify vulnerabilities like SQL injection and hardcoded credentials early in the SDLC.

By catching these issues before deployment, they reduce the cost and complexity of fixing them.

Eg:- A SAST tool scans Python code and flags a vulnerability where hardcoded API keys are embedded in the source code.

Developers refactor the code to use environment variables to securely store and retrieve the keys.

For code reviews.

SAST integrates into version control systems.

Allows developers to scan their code before committing it.

This makes sure that only secure code enters the repository.

Example: A SAST tool can detect a vulnerability where a file path is constructed directly from user input without validation, exposing the application to path traversal attacks.

Developers fix the issue by sanitizing the input and using secure library functions to handle file paths.

In continuous integration/continuous deployment pipelines.

SAST runs automated scans during the CI/CD process.

It offers real-time feedback to developers.

When to use DAST
Pre-production testing.

Developers use DAST to identify runtime vulnerabilities (eg:- insecure configurations, authentication flaws, insufficient access controls) in a staging or QA environment.

Example: A DAST tool can detect a database misconfiguration that exposes sensitive data.

Then developers can secure the configuration before deployment.

In post-deployment monitoring.

DAST tools continue to scan deployed applications for vulnerabilities caused by changes in the environment or emerging threats.

This guarantees that the application remains secure over time.

Testing third-party integrations.

DAST can mimic an external attacker's perspective to identify vulnerabilities in third-party APIs or interconnected systems.

For example: A DAST tool tests a web application and discovers a vulnerability in a third-party payment API where credit card details are being transmitted over an unencrypted HTTP connection.

Developers resolve the issue by enforcing HTTPS for all API communications.

Which is more effective: SAST or DAST?

The effectiveness of SAST or DAST depends on:
The SDLC stage
The type of vulnerabilities being addressed
SAST works best in early development, primarily to identify vulnerabilities in the source code, reduce costs, and promote secure coding practices.

In contrast, DAST focuses on runtime vulnerabilities in pre-production or deployed applications.

It offers insights into issues like misconfigurations and insecure integrations.

Take a hybrid approach
Instead of choosing one over the other, combining SAST and DAST creates a multi-layered security strategy that addresses vulnerabilities in both static code and runtime environments.

SAST can be integrated into early development stages to detect and fix code-level issues before the application is compiled.

Once the application is running in a test environment, DAST can identify runtime vulnerabilities and evaluate the application’s behavior under attack conditions.

Automating both SAST and DAST scans within a CI/CD pipeline provides continuous feedback and accelerates the development process without compromising security.

For agile or DevOps environments, adding tools like IAST or RASP can further enhance security.

By correlating results from both SAST and DAST, organizations can achieve more comprehensive and effective vulnerability management.

Use RASP as an alternative to SAST and DAST
Runtime Application Self-Protection (RASP) is an advanced security solution installed directly on the server where the application runs.

RASP embeds itself into the application's runtime environment.

This integration allows RASP to analyze the app's logic and data.

While analyzing, it can:
Detect abnormal behaviors as they happen.

Block malicious activities instantly.

A key difference is that RASP doesn't just alert on potential issues — it actively prevents attacks by isolating and resolving threats without relying on external tools.

RASP offers a dynamic alternative to SAST and DAST.

Unlike SAST, which analyzes static code, and DAST, which simulates external attacks, RASP operates in real time.

It monitors the application’s behavior during execution and responds to live threats by terminating sessions or alerting defenders.

RASP is particularly effective in protecting applications against vulnerabilities that bypass network defenses or are missed during development.

However, overconfidence in RASP can lead organizations to neglect secure coding practices.

Also, RASP may impact application performance because it operates directly within the application's runtime environment.

RASP cannot replace the need to fix underlying flaws, but it provides continuous protection while remediation is underway.

As one RASP user comments:
“The decision to use a RASP tool should be based on a thorough assessment of the application's specific requirements and risk profile.”
The future is AppSec testing with SAST, DAST, and RASP
The future of application testing lies in combining SAST, DAST, and RASP to create a comprehensive security strategy.