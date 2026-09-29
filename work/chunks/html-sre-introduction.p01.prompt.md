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

Chapter 1 - Introduction
Table of Contents
Foreword
Preface
Part I - Introduction
1.

Introduction
2.

The Production Environment at Google, from the Viewpoint of an SRE
Part II - Principles
3.

Embracing Risk
4.

Service Level Objectives
5.

Eliminating Toil
6.

Monitoring Distributed Systems
7.

The Evolution of Automation at Google
8.

Release Engineering
9.

Simplicity
Part III - Practices
10.

Practical Alerting
11.

Being On-Call
12.

Effective Troubleshooting
13.

Emergency Response
14.

Managing Incidents
15.

Postmortem Culture: Learning from Failure
16.

Tracking Outages
17.

Testing for Reliability
18.

Software Engineering in SRE
19.

Load Balancing at the Frontend
20.

Load Balancing in the Datacenter
21.

Handling Overload
22.

Addressing Cascading Failures
23.

Managing Critical State: Distributed Consensus for Reliability
24.

Distributed Periodic Scheduling with Cron
25.

Data Processing Pipelines
26.

Data Integrity: What You Read Is What You Wrote
27.

Reliable Product Launches at Scale
Part IV - Management
28.

Accelerating SREs to On-Call and Beyond
29.

Dealing with Interrupts
30.

Embedding an SRE to Recover from Operational Overload
31.

Communication and Collaboration in SRE
32.

The Evolving SRE Engagement Model
Part V - Conclusions
33.

Lessons Learned from Other Industries
34.

Conclusion
Appendix A.

Availability Table
Appendix B.

A Collection of Best Practices for Production Services
Appendix C.

Example Incident State Document
Appendix D.

Example Postmortem
Appendix E.

Launch Coordination Checklist
Appendix F.

Example Production Meeting Minutes
Bibliography
Introduction
Written by Benjamin Treynor Sloss6
Edited by Betsy Beyer
Hope is not a strategy.

Traditional SRE saying
It is a truth universally acknowledged that systems do not run themselves.

How, then, should a systemâparticularly a complex computing system that operates at a large scaleâbe run?

The Sysadmin Approach to Service Management
Historically, companies have employed systems administrators to run complex computing systems.

This systems administrator, or sysadmin, approach involves assembling existing software components and deploying them to work together to produce a service.

Sysadmins are then tasked with running the service and responding to events and updates as they occur.

As the system grows in complexity and traffic volume, generating a corresponding increase in events and updates, the sysadmin team grows to absorb the additional work.

Because the sysadmin role requires a markedly different skill set than that required of a productâs developers, developers and sysadmins are divided into discrete teams: "development" and "operations" or "ops."
The sysadmin model of service management has several advantages.

For companies deciding how to run and staff a service, this approach is relatively easy to implement: as a familiar industry paradigm, there are many examples from which to learn and emulate.

A relevant talent pool is already widely available.

An array of existing tools, software components (off the shelf or otherwise), and integration companies are available to help run those assembled systems, so a novice sysadmin team doesnât have to reinvent the wheel and design a system from scratch.

The sysadmin approach and the accompanying development/ops split has a number of disadvantages and pitfalls.

These fall broadly into two categories: direct costs and indirect costs.

Direct costs are neither subtle nor ambiguous.

Running a service with a team that relies on manual intervention for both change management and event handling becomes expensive as the service and/or traffic to the service grows, because the size of the team necessarily scales with the load generated by the system.

The indirect costs of the development/ops split can be subtle, but are often more expensive to the organization than the direct costs.

These costs arise from the fact that the two teams are quite different in background, skill set, and incentives.

They use different vocabulary to describe situations; they carry different assumptions about both risk and possibilities for technical solutions; they have different assumptions about the target level of product stability.

The split between the groups can easily become one of not just incentives, but also communication, goals, and eventually, trust and respect.

This outcome is a pathology.

Traditional operations teams and their counterparts in product development thus often end up in conflict, most visibly over how quickly software can be released to production.

At their core, the development teams want to launch new features and see them adopted by users.

At their core, the ops teams want to make sure the service doesnât break while they are holding the pager.

Because most outages are caused by some kind of changeâa new configuration, a new feature launch, or a new type of user trafficâthe two teamsâ goals are fundamentally in tension.

Both groups understand that it is unacceptable to state their interests in the baldest possible terms ("We want to launch anything, any time, without hindrance" versus "We wonât want to ever change anything in the system once it works").

And because their vocabulary and risk assumptions differ, both groups often resort to a familiar form of trench warfare to advance their interests.

The ops team attempts to safeguard the running system against the risk of change by introducing launch and change gates.

For example, launch reviews may contain an explicit check for every problem that has ever caused an outage in the pastâthat could be an arbitrarily long list, with not all elements providing equal value.

The dev team quickly learns how to respond.

They have fewer "launches" and more "flag flips," "incremental updates," or "cherrypicks." They adopt tactics such as sharding the product so that fewer features are subject to the launch review.

Googleâs Approach to Service Management: Site Reliability Engineering
Conflict isnât an inevitable part of offering a software service.

Google has chosen to run our systems with a different approach: our Site Reliability Engineering teams focus on hiring software engineers to run our products and to create systems to accomplish the work that would otherwise be performed, often manually, by sysadmins.

What exactly is Site Reliability Engineering, as it has come to be defined at Google?

My explanation is simple: SRE is what happens when you ask a software engineer to design an operations team.

When I joined Google in 2003 and was tasked with running a "Production Team" of seven engineers, my entire life up to that point had been software engineering.

So I designed and managed the group the way I would want it to work if I worked as an SRE myself.

That group has since matured to become Googleâs present-day SRE team, which remains true to its origins as envisioned by a lifelong software engineer.

A primary building block of Googleâs approach to service management is the composition of each SRE team.

As a whole, SREs can be broken down into two main categories.

50â60% are Google Software Engineers, or more precisely, people who have been hired via the standard procedure for Google Software
Engineers.

The other 40â50% are candidates who were very close to the Google Software Engineering qualifications (i.e., 85â99% of the skill set required), and who in addition had a set of technical skills that is useful to SRE but is rare for most software engineers.

By far, UNIX system internals and networking (Layer 1 to Layer 3) expertise are the two most common types of alternate technical skills we seek.

Common to all SREs is the belief in and aptitude for developing software systems to solve complex problems.

Within SRE, we track the career progress of both groups closely, and have to date found no practical difference in performance between engineers from the two tracks.

In fact, the somewhat diverse background of the SRE team frequently results in clever, high-quality systems that are clearly the product of the synthesis of several skill sets.

The result of our approach to hiring for SRE is that we end up with a team of people who (a) will quickly become bored by performing tasks by hand, and (b) have the skill set necessary to write software to replace their previously manual work, even when the solution is complicated.

SREs also end up sharing academic and intellectual background with the rest of the development organization.

Therefore, SRE is fundamentally doing work that has historically been done by an operations team, but using engineers with software expertise, and banking on the fact that these engineers are inherently both predisposed to, and have the ability to, design and implement automation with software to replace human labor.

By design, it is crucial that SRE teams are focused on engineering.

Without constant engineering, operations load increases and teams will need more people just to keep pace with the workload.