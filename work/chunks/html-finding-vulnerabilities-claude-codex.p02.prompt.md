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

Note that we are not releasing the names of these popular open-source web apps today, since we are still in the process of responsible disclosure, we will release the dataset once the process has concluded.

App ID
Commits
as of Aug, 2025
Github Stars
Python files
Python lines of code
No blank.

No comment.

PY-APP-001
>25k
5k
>500
85k
PY-APP-002
>5k
6k
>500
60k
PY-APP-003
>15k
10k
>200
45k
PY-APP-004
>5k
>100
>500
95k
PY-APP-005
>15k
1k
>500
100k
PY-APP-006
>25k
2k
>1000
110k
PY-APP-007
>5k
20k
>1000
250k
PY-APP-008
>1k
>100
>200
40k
PY-APP-009
1k
3k
>50
2k
PY-APP-010
15k
5k
>200
45k
PY-APP-011
>5k
>25k
>200
30k
7k files
>800kLOC
Application names will be released when all vulnerabilities are disclosed and handled.

The Experiment: AI vs.

Real-World Apps Code
We ran our analysis across the 11 applications and then triaged every one of the 445 findings manually, validating most of them (especially IDOR or Auth bypass) dynamically.

Anthropic Claude Code (v1.0.32, Sonnet 4)
Vulnerability Class
True Positives
False Positives
True Positive Rate
Auth bypass
6
52
10% (6/58)
IDOR
13
46
22% (13/59)
Path traversal
5
31
13% (5/36)
SQL Injection
2
36
5% (2/38)
SSRF
8
57
12% (8/65)
XSS
12
62
16% (12/74)
Using the following command:
claude --verbose
--print
--output-format json
--dangerously-skip-permissions
<PROMPT>OpenAI Codex (v0.2.0, o4-mini/high reasoning)
Vulnerability Class
True Positives
False Positives
True Positive Rate
Auth bypass
5
32
13% (5/37)
IDOR
0
5
0% (0/5)
Path traversal
8
9
47% (8/17)
SQL Injection
0
5
0% (0/5)
SSRF
8
15
34% (8/23)
XSS
0
28
0% (0/28)
Using the following command:
codex --config disable_response_storage=true
--config model_reasoning_effort=high
--config model_reasoning_summary=detailed
exec
--model o4-mini
--full-auto
--skip-git-repo-check
<PROMPT>What we Found
Both Claude Code and Codex are useful today: they find real security vulnerabilities, but they're very noisy.

The overall noise is still very high, but they found real security vulnerabilities in these popular open source Python web applications.

Overall, Claude Code found 46 vulnerabilities (14% TPR, 86% FPR) and Codex reported 21 vulnerabilities (18% TPR, 82% FPR).

Many IDOR bugs looked correct at first and Claude Code suggested credible fixes: The LLM could not only find these bugs but also suggest credible fixes, like injecting new permission checks based on existing patterns in the code.

IDOR issues can be hard to triage and we had to test most of them to be certain, which brought the true positive rate much lower.

Claude Code as a good secure guardrails tool?

Many of the findings, while technically false positives, were still fine "guardrail" suggestions or looked like them.

For instance, the model would often suggest parameterizing a SQL query that was already safe.

While not a vulnerability, this strengthens the code.

We still considered these to be false positives, though not as severe as others.

However, these code hardening recommendations can't always be trusted.

We found several instances, especially in client-side JavaScript code, where the AI tries to fix what it perceives as an issue around DOM manipulation, but in fact, it breaks the code (double escaping the HTML in the cases we observed), despite there being no security issue there in the first place.

XSS and SQL Injection – hard to piece components together: The model struggles to trace data from a server-side framework to a client-side component (a common pattern for XSS) or through complex application layers.

It often got confused by statically defined data or failed to recognize server-side sanitization.

Repeating the prompt helped with getting more results: The probabilistic nature of LLMs means that asking the same question in a slightly different way can yield new findings, highlighting the inconsistency of the analysis.

Repeating the same prompt multiple times on the same code base gave us different answers, but it eventually circled back to the same findings.

OpenAI Codex sometimes failed to report valid SARIF.

9 reports over the 66 we expected were not valid SARIF.

We considered all findings reported in those files, but they weren't valid SARIF or JSON.

Claude Code didn't have this problem in any of the cases we tried.

Same Code, Same AI, Different Bugs Every Time: AI Coding Agents' Non-Determinism Problem
To explore how non-determinism manifested in practice, we selected three of these applications and ran the same prompt multiple times with the same prompt, targeting the same security issue: IDOR.

A pattern emerged: the AI's findings were different every single time we ran the test.

In the context of vulnerability detection this is a major issue.

First, as a security engineer, ideally we want stronger guarantees that our code was scanned for important vulnerability classes than "I hope the model searched thoroughly this time."
Second, intermittently detecting vulnerabilities can cause inconsistencies and noise in your security tools or vulnerability management systems.

For example, if you're using a SAST platform, ASPM, or something you've built internally, oftentimes those systems assume that when a previously detected vulnerability is no longer present, then it has been fixed.

But that may not be the case with LLM-driven detection, as a single scan might miss it, and thus a "new" finding will be created when a subsequent scan re-finds the same issue, leading to duplicate JIRA tickets and developer frustration.

Here are some specific examples we observed:
PY-APP-007: In the first run, the AI identified a "missing search authorization" vulnerability that was absent from the other two runs.

The second run flagged issues that were unique to that run.

The third run, in turn, found its own distinct set of vulnerabilities.

PY-APP-006: Similar story: the first run unearthed a vulnerability in the user API, while the subsequent runs focused on different parts of the codebase, such as the event abstracts and notes modules.

PY-APP-002: The variability here was perhaps the most pronounced.

The number of identified vulnerabilities jumped from 3 in the first run to 6 in the second, and then 11.

Each run presented different findings that only partially overlapped.

So, what's behind this?

We believe the key factors are what's known as context rot and compaction.

When an AI agent is tasked with analyzing an entire codebase, it's dealing with a massive amount of information: context rot leads to the inability to retrieve accurately from its own context.

To manage this, LLMs use a form of lossy compression (sometimes called compaction), which means that some of the finer reasoning details like function names, paths, etc.

can get lost in the summarization process.

Think of it like trying to summarize a long, complex novel.

You'll capture the main plot points, but you're bound to miss some of the subtleties and nuances.

In the same way, the AI might lose track of a specific architectural pattern or a subtle data flow, leading it to miss a vulnerability in one run that it might catch in another.

We saw a clear example of this in PY-APP-006, where one of the AI's proposed fixes was incomplete because it failed to reuse an existing base class for user authorization — a crucial piece of context that was seemingly lost in that particular run.

This non-determinism has significant implications for how we approach AI native SAST.

On one hand, the ability of the AI to "think" differently each time means it can explore a wider range of potential attack vectors, much like a team of human penetration testers with diverse perspectives.

On the other hand, it introduces a level of uncertainty that can lead to confusion or mis-behaviors.

Incomplete Coverage: A single run might provide a false sense of security, as it could miss critical vulnerabilities that might be caught in a subsequent run.

Lack of Repeatability: The inability to reproduce results makes it difficult to verify the AI's findings and to trust its output in a consistent, repeatable manner.

Increased Cost and Time: The need to run multiple audits to get a more complete picture can significantly increase the time and computational resources required.

Note: with traditional software, once you've written it, you can run it again basically "for free" (excluding hardware costs, electricity, etc.) This is not the case for LLM-heavy tooling, where in this case reading in a code base and reasoning about it could result in tens to hundreds of dollars in token costs per scan.

This cost may decrease over time for today's models, but newer models may be more expensive.

How Effective is Claude Code's New /security-review Command?

Anthropic released a new command for Claude Code, called /security-review.

It's designed to be run on a pull request to examine the changed files and ask questions to identify specific security issues.

You can find the prompt here.

When running this command on the entire codebase, we found that the security issues identified were fairly limited.