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

TL;DR: We evaluated how effective AI Coding Agents are at finding vulnerabilities in real code.

How: we tasked Anthropic's Claude Code (v1.0.32, Sonnet 4) and OpenAI Codex (v0.2.0, o4-mini) with finding vulnerabilities in 11 popular and large open-source Python web applications.

Together they produced over 400 security findings our security research team reviewed.

AI Coding Agents Find Real Vulnerabilities: Claude Code found 46 vulnerabilities (14% true positive rate – TPR, 86% false positive rate – FPR) and Codex reported 21 vulnerabilities (18% TPR, 82% FPR).

About 20 of these are high severity vulnerabilities.

AI Grasps Context, Chokes on Flows: Claude Code was best at finding Insecure Direct Object Reference (IDOR) bugs with a 22% (13 correct issues/59 reported) true positive rate (TPR), but struggled at performing taint tracking across multiple files and functions, with a 5% (2/38) TPR for SQL Injection and a 16% (12/74) TPR for XSS.

OpenAI Codex struggled to report any correct IDOR 0% (0/5) TPR, did very poorly at SQL injection 0% (0/5) and XSS 0% (0/28) but surprisingly reported more correct Path Traversal issues than Claude Code 47% (8/17) TPR.

Non-Determinism is a Real Struggle: Running the exact same prompt on the exact same codebase multiple times often yielded vastly different results.

In one application, three identical runs produced 3, 6, and then 11 distinct findings.

Key take-aways:
AI Coding Agents with relatively simple security-focused prompts can already find real vulnerabilities in real applications.

BUT: depending on the vulnerability class, the results may be quite noisy (high false positive rate), especially on traditional injection-style vulnerability classes like SQL injection, XSS, and SSRF.

Detailed evaluations and benchmarking are key for understanding how effective an approach is for finding vulnerabilities (this has always been true, but even more so now with non deterministic tools like LLMs), and to know when your improvements are headed in the right direction.

This is our first post of a series on using and augmenting AI for finding vulnerabilities!

In this post we'll cover:
The problems with usual SAST benchmarks and how it affects AI SAST evaluation
Some open research questions about AI-based vulnerability hunting
Our AI Coding Agents experiment, dataset, and what we learned
How Anthropic's /security-review command is pretty mid
The non-determinism of AI Coding Agents, and why it happens
This post was last edited on Sept 3, 2025, 11:15am UTC
Sept 3, 2025, 11:15am UTC: Added details about models used and commands to call them
Introduction
Here at Semgrep, we live and breathe application security (AppSec).

We've been productionizing AI for a long time in our products (tech behind Assistant, promptfoo for testing our AI workflows, using security researcher triage to evaluate auto triage performance), constantly researching the best combination of traditional, deterministic analysis and the contextual power of modern AI without chasing trends.

This research is part of that ongoing mission.

We're embarking on a deep, public exploration to answer a question that's on everyone's mind: how effective are LLMs really at finding vulnerabilities in source code?

Open Research Questions about AI-based Vulnerability Hunting
To guide our investigation, we broke down the broad question of "Are LLMs good at finding bugs?" into more specific, measurable sub-questions.

What are the false positive and false negative rates for LLM-based vulnerability finding?

Does it vary by programming language, framework, code base size, or vulnerability class?

What are the sensibilities to how code is written?

What are the common reasons for false positives and false negatives?

How deterministic is the analysis?

Do you get the same results every time?

For injection vulnerabilities specifically, we wanted to know:
How effective is the LLM at tracking user input between a source (e.g., a user supplied value) and a sink (e.g., a method that consumes a raw SQL query)?

Can it track data across functions and files?

Can it reason about sanitization functions and other security controls?

Can it reason about functions from third-party open source dependencies?

The Problem with Usual SAST Benchmarks: Lack of Realism
Before diving into our findings, let's talk about how we measure AI performance.

Much of the current research/claims relies on benchmarks that, while valuable, don't fully capture the complexity of real-world code.

Apps with known vulnerabilities: These benchmarks only use open-source applications with known vulnerabilities; many can be found in vulnerable-apps thanks to Kinnaird McQuade.

If you read this blog, you may recognize some of the names WebGoat, JuiceShop, OWASP Benchmark, etc.

But, there's a problem with these, current LLMs have likely ingested the code for these repositories as well as many public write-ups on the Internet, giving them pre-existing knowledge and skewing the results.

Their code is often not realistic with an abundance of comments, annotations, and variable names that hint at or directly describe where the vulnerabilities are in the code or how to exploit them.

Sometimes, tools results are even checked in the repo.

from javaspringvulny's SearchService.java
from juiceshop, the challenge is part of the file name…
XBOW provides benchmarks for auto pentesting tools, but not adapted to static analysis: the code is often too contrived and simplistic and doesn't represent real application.

ZeroPath did a good job when they sanitized them, but only a fraction were sanitized.

Moreover, each of these test cases are tiny applications, designed to stimulate a dedicated attack scenario.

If we focus on Python benchmarks, XBOW has 45 of them; 45 different tiny applications with an average of less than 98 lines of code and 3 Python files.

This is too small to capture the complexity of searching and reasoning across an entire code base or many functions.

CVE Memorization Bias: As LLMs are trained on a massive corpus of public data from the internet, including the very codebases where CVEs were found and fixed.

This creates a fundamental data contamination problem.

The AI may not be detecting a vulnerability through novel analysis but simply recognizing a pattern it memorized during training.

More recently academics have designed benchmarks such as CyberGym, Eyeballvul, or SecVulEval.

These show a great improvement and are closer to real-world examples but they lack the focus on modern web apps or isolate vulnerabilities from the broader application context.

EyeballVul: A more recent benchmark from Timothée Chauvin that extracts real-world, human-vetted vulnerabilities from open-source projects and presents them as minimal, reproducible test cases.

While based on real code, it still isolates the vulnerability from the broader application context, making the search problem easier.

SecVulEval and CyberGym: These suites are designed to evaluate vulnerabilities in C or C++.

While valuable in their domain, their focus on C and C++ means these data are not applicable to the Python/JavaScript and other web-centric languages that dominate modern cloud-native development.

While each of these approaches are useful and should be used at times, they don't necessarily reflect the reality of modern software development.

Real-world applications are not clean, isolated functions.

They are complex webs of dependencies, frameworks, and business logic.

Our approach is different.

We tested on 11 large, Python based, actively maintained open-source projects, written in common web frameworks (Django, Flask, FastAPI).

Our method is complementary to the previous ones, and we believe it's unique in that it a) aims to be representative of AI-driven vulnerability finding in the real world (vs.

small, isolated synthetic examples), b) is not contaminated by model training data, and c) represents the types of applications most developers and companies are actually building – web applications using modern languages and frameworks.

Scope for this Blog Post
To make this tractable, we focused on:
Using 1 run of Anthropic Claude Code (v1.0.32, Sonnet 4) and OpenAI Codex (v0.2.0, o4-mini) out of the box with a simple, scripted prompt [1] reused for the different kinds of vulnerabilities.

We asked them to return SARIF formatted security issues.

Analyzing 11 different large-ish, real-world open source Python projects.

Focusing on common, high-impact vulnerability classes: Auth Bypass, IDOR, Path Traversal, SQL Injection, SSRF, and XSS.

Exploratory results with Anthropic's recent /security-review command
Exploring the (non) determinism on a subset of these apps for IDOR by doing 3 runs on 3 different apps.

To ground our research, we selected popular and actively maintained projects.

Here's a look at the scale of the applications we analyzed.