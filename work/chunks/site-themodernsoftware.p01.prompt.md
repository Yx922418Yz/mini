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

Offline Cache — This is a locally saved version of themodernsoftware.dev captured on April 2, 2026.
Article pages are saved in the pages/ folder. PDF documents are in the pdfs/ folder.
Video links (YouTube) and Google Slides remain as external links.
Course Description
In the last few years, large language models have introduced a revolutionary new paradigm in software development. The traditional software development lifecycle is being transformed by AI automation at every stage, raising the question: how should the next generation of software engineers leverage these advances to 10x their productivity and prepare for their careers?
This course demonstrates that modern AI tooling will not only enhance developer productivity but also democratize software engineering for a broader audience. We'll show that software development has evolved from 0-1 code creation to an iterative workflow of plan, generate with AI, modify, and repeat. Students will master both the theory behind traditional software engineering challenges and the cutting-edge AI-powered tools solving them today.
Through hands-on engineering tasks and talks from industry pioneers building these revolutionary tools, you'll gain practical experience with AI-assisted development, automated testing, intelligent documentation, and security vulnerability detection. By the end of this course, you'll have a crisp understanding of how to integrate state-of-the-art LLM models into complex development workflows and avoid common pitfalls.
Units
3 units
Prerequisites
CS111 equivalent programming experience. CS221/229 recommended.
Format
Weekly lectures, hands-on coding sessions, and guest speakers from industry. Final project showcasing modern development practices.
Goals
Master modern development tools, understand AI-assisted coding, learn automated testing and deployment, explore emerging software trends.
Classroom
420-041
Office Hours
Mihail Eric: Friday 12:00–12:30 PM
Febie Lin: Wednesday 9:00–11:00 AM (Huang Basement)
Assignment Deadlines
Calendar (Google Sheets)
Team
Mihail Eric
Instructor
Febie Lin
TA
Brent Ju
TA
Course Schedule
Week 1: Introduction to Coding LLMs and AI Development
Topics
Course logistics
What is an LLM actually
How to prompt effectively
Reading
Deep Dive into LLMs
Prompt Engineering Overview
Prompt Engineering Guide
AI Prompt Engineering: A Deep Dive
How OpenAI Uses Codex
Assignment
LLM Prompting Playground
Lectures
Mon 9/22: Introduction and how an LLM is made — Slides
Fri 9/26: Power prompting for LLMs — Slides
Week 2: The Anatomy of Coding Agents
Topics
Tool use and function calling
MCP (Model Context Protocol)
Reading
MCP Introduction
Sample MCP Server Implementations
MCP Server Authentication
MCP Server SDK
MCP Registry
MCP Food-for-Thought
Assignment
First Steps in the AI IDE
Lectures
Mon 9/29: Building a coding agent from scratch — Slides, Completed Exercise
Fri 10/3: Building a custom MCP server — Slides, Completed Exercise
Week 3: The AI IDE
Topics
Context management and code understanding
PRDs for agents
IDE integrations and extensions
Reading
Specs Are the New Source Code
How Long Contexts Fail
Devin: Coding Agents 101
Getting AI to Work In Complex Codebases
How FAANG Vibe Codes
Writing Effective Tools for Agents
Assignment
Build a Custom MCP Server
Lectures
Mon 10/6: The AI IDE deep dive — Slides
Fri 10/10: Guest: Silas Alberti (Cognition) — Slides
Resources: Design Doc Template
Week 4: Claude Code and Agentic Coding
Topics
Claude Code architecture and internals
Agentic coding workflows
Context engineering for agents
Reading
How Anthropic Uses Claude Code
Claude Best Practices
Awesome Claude Agents
Super Claude
Good Context Good Code
Peeking Under the Hood of Claude Code
Assignment
Coding with Claude Code
Lectures
Mon 10/13: Claude Code deep dive — Slides
Fri 10/17: Guest: Boris Cherney (Claude Code) — Slides
Week 5: Warp and the AI Terminal
Topics
AI-native terminal development
Agentic development workflows
Reading
Warp vs Claude Code
How Warp Uses Warp to Build Warp
Warp University
Assignment
Agentic Development with Warp
Lectures
Mon 10/20: Warp and the AI terminal — Slides
Fri 10/24: Guest: Zach Lloyd (Warp) — Slides (Figma)
Week 6: AI Security and Vulnerability Detection
Topics
Security testing (SAST vs DAST)
Prompt injection attacks
AI-assisted vulnerability detection
OWASP Top 10
Reading
SAST vs DAST
Copilot Remote Code Execution via Prompt Injection
Finding Vulnerabilities in Modern Web Apps Using Claude Code and OpenAI Codex
Agentic AI Threats: Identity Spoofing and Impersonation Risks
OWASP Top Ten: The Leading Web Application Security Risks
Context Rot: Understanding Degradation in AI Context Windows
Vulnerability Prompt Analysis with O3
Assignment
Writing Secure AI Code
Lectures
Mon 10/27: AI security deep dive — Slides
Fri 10/31: Guest: Isaac Evans (Semgrep)
Week 7: AI-Powered Code Review
Topics
Code review best practices
AI-assisted code review
Automated review tooling
Reading
Code Reviews: Just Do It
How to Review Code Effectively
AI-Assisted Assessment of Coding Practices in Modern Code Review
AI Code Review Implementation Best Practices
Code Review Essentials for Software Teams
Lessons from Millions of AI Code Reviews
Assignment
Code Review Reps
Lectures
Mon 11/3: AI code review deep dive — Slides
Fri 11/7: Guest: Tomas Reimers (Graphite) — Slides
Week 8: Full-Stack AI Development and Deployment
Topics
Multi-stack web application development
AI-assisted deployment pipelines
Assignment
Multi-stack Web App Builds
Lectures
Mon 11/10: Full-stack AI development — Slides
Fri 11/14: Guest: Gaspar Garcia (Vercel) — Slides
Week 9: SRE, Observability, and Agentic On-Call
Topics
Site Reliability Engineering fundamentals
Observability and monitoring
AI agents in on-call engineering
Multi-agent systems
Reading
Introduction to Site Reliability Engineering
Observability Basics You Should Know
Kubernetes Troubleshooting with AI
Your New Autonomous Teammate / Benefits of Agentic AI in On-call Engineering
Role of Multi Agent Systems in Making Software Engineers AI-native
Lectures
Mon 11/17: SRE and AI observability — Slides
Fri 11/21: Guests: Mayank Agarwal & Milind Ganjoo (Resolve) — Slides
Week 10: The Future of AI in Software Engineering
Topics
Future trends in AI-assisted development
Industry perspectives and career implications
Final project presentations
Lectures
Mon 12/1: Guest: Martin Casado (a16z)
Fri 12/5: Final project presentations
Frequently Asked Questions
Who is this course for?
This course is designed for students with programming experience (CS111 equivalent) who want to learn how to leverage modern AI tools to dramatically improve their software development productivity. CS221/229 is recommended but not required.
What will I build in this course?
Students will complete weekly hands-on assignments covering LLM prompting, MCP server development, AI IDE usage, Claude Code workflows, security analysis, code review automation, and full-stack web applications. The course culminates in a final project showcasing modern development practices.
What tools will we use?
The course covers a range of AI development tools including Claude Code, Warp terminal, Cursor/Windsurf IDEs, Semgrep, Graphite, and Vercel. We'll also work with the Model Context Protocol (MCP) and various LLM APIs.
How are grades determined?
Grades are based on weekly assignments, participation in class discussions, and the final project. See the assignment calendar for specific deadlines.
Are lectures recorded?
Please check with the course staff for recording availability. Slides for each lecture are linked in the syllabus above.
How do I contact the teaching team?
Mihail Eric: Office hours Friday 12:00–12:30 PM
Febie Lin: Office hours Wednesday 9:00–11:00 AM (Huang Basement)
Brent Ju: See course Slack/Ed for contact info.