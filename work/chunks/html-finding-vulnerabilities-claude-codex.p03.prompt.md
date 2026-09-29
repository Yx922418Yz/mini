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

Many times, it couldn't find security issues that we were getting when we prompted Claude Code to search for one specific kind of security issue at a time.

We ran this command on PY-APP-003, PY-APP-002, and PY-APP-008, and it only found one XSS across all of them, which is very different from the results we got in the overall experiment.

Answering Our Questions
Let's revisit our initial research questions based on what we've learned.

What are the FP/FN rates?

For raw AI on real-world code, the false positive rate is very high, ranging from at best 53% for Path Traversal for Codex or 78% for IDOR for Claude Code to at worst 95% with SQL injection for Claude Code and 100% for SQL injection or IDOR for Codex.

The performance varies dramatically by application too, from 100% (10/10) real IDOR in PY-APP-002 (Claude Code) to 0% (0/7) for PY-APP-007.

Across all apps and all reported issues, Claude Code found 46 vulnerabilities (14% TPR, 86% FPR) and Codex reported 21 vulnerabilities (18% TPR, 82% FPR).

Since we've been using real applications, we can't accurately measure false negatives in this experiment.

We'll cover techniques for measuring false negative rates in an upcoming blog post!

Why does it fail?

The primary weakness we observed is a lack of deep, semantic understanding of code execution for injection issues.

Models struggle with inter-procedural taint flow and implicit flows, the things traditional SAST engines are usually built for.

Some of the limitations are also coming from context compaction and context rot.

We will continue to explore these limitations in more detail and explore solutions to mitigate them.

How important are scaffolding and agentic workflows?

They are not just important; they are becoming essential.

The future of AI in security review is not a single, monolithic model but a system of AI agents (including coding agents like in our cases) that can use tools, reason about evidence, and collaborate to find and validate vulnerabilities.

While we don't (yet) have data here on the difference between using an agent with access to Claude Code versus more typical context engineering (that is, building the scaffolding to provide all of the relevant code) with reasoning model, we observed a huge difference in the system's ability to work through a complex process and make educated decisions on the way to reporting security issues.

That being said, a counterexample of this is how Sean Heelan was able to do enough context engineering to get a reasoning model to report a vulnerability (8% of the time).

We really suggest you read his blog post.

How about the cost in all of this?

Unfortunately, we haven't been able to track uniformly the cost between Claude Code and Codex.

The overall cost of Claude Code was $114, for all these vulnerabilities and all these apps (except running for non-determinism and for /security-review command).

Dataset: Future Release
We are not releasing a dataset today nor the names of the open source applications analyzed because we're in the process of responsible disclosure, reaching out to the application developers to get all the security issues fixed and validated.

Once that's done, we'll be comfortable releasing the data.

Conclusion
LLMs are not a silver bullet that will replace human security engineers tomorrow, in fact they are pretty weak on finding high-severity injection-style vulnerabilities end to end.

However, they are an incredibly powerful tool.

Our research indicates that by understanding their strengths (contextual reasoning) and weaknesses (deep semantics of the code), and by building sophisticated agentic systems around them using advanced static analysis engines, we can create a new generation of security tooling that is far more powerful than anything that has come before.

[1] Scripted simple prompt for Claude Code and Codex
BATCH_PROMPT_TEMPLATE = """
I am a core developer of this app.

It's been reported to me that
there are several {vuln_type} vulnerabilities in the code base.

I need
your expertise to find all of them!

# Instructions
- Find all {vuln_type} vulnerabilities in my code, don't worry about
third-party code.

- Explain why they are real security vulnerabilities I should care about; give
code snippets from the code to support your analysis (trace from entry points);
maybe some clue on how to trigger the issue for testing.

- Report all {vuln_type} vulnerabilities using the SARIF JSON format that you will
write within the <SARIF_OUTPUT>...</SARIF_OUTPUT> tag; make sure it's valid JSON.

- Fix these security issues in the code.

Don't ask for confirmation, just do it.

"""