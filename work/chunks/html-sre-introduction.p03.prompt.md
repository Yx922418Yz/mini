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

As soon as SRE activities are conceptualized in this framework, freeing up the error budget through tactics such as phased rollouts and 1% experiments can optimize for quicker launches.

The use of an error budget resolves the structural conflict of incentives between development and SRE.

SREâs goal is no longer "zero outages"; rather, SREs and product developers aim to spend the error budget getting maximum feature velocity.

This change makes all the difference.

An outage is no longer a "bad" thingâit is an expected part of the process of innovation, and an occurrence that both development and SRE teams manage rather than fear.

Monitoring
Monitoring is one of the primary means by which service owners keep track of a systemâs health and availability.

As such, monitoring strategy should be constructed thoughtfully.

A classic and common approach to monitoring is to watch for a specific value or condition, and then to trigger an email alert when that value is exceeded or that condition occurs.

However, this type of email alerting is not an effective solution: a system that requires a human to read an email and decide whether or not some type of action needs to be taken in response is fundamentally flawed.

Monitoring should never require a human to interpret any part of the alerting domain.

Instead, software should do the interpreting, and humans should be notified only when they need to take action.

There are three kinds of valid monitoring output:
Alerts
Signify that a human needs to take action immediately in response to something that is either happening or about to happen, in order to improve the situation.

Tickets
Signify that a human needs to take action, but not immediately.

The system cannot automatically handle the situation, but if a human takes action in a few days, no damage will result.

Logging
No one needs to look at this information, but it is recorded for diagnostic or forensic purposes.

The expectation is that no one reads logs unless something else prompts them to do so.

Emergency Response
Reliability is a function of mean time to failure (MTTF) and mean time to repair (MTTR) [Sch15].

The most relevant metric in evaluating the effectiveness of emergency response is how quickly the response team can bring the system back to healthâthat is, the MTTR.

Humans add latency.

Even if a given system experiences more actual failures, a system that can avoid emergencies that require human intervention will have higher availability than a system that requires hands-on intervention.

When humans are necessary, we have found that thinking through and recording the best practices ahead of time in a "playbook" produces roughly a 3x improvement in MTTR as compared to the strategy of "winging it." The hero jack-of-all-trades on-call engineer does work, but the practiced on-call engineer armed with a playbook works much better.

While no playbook, no matter how comprehensive it may be, is a substitute for smart engineers able to think on the fly, clear and thorough troubleshooting steps and tips are valuable when responding to a high-stakes or time-sensitive page.

Thus, Google SRE relies on on-call playbooks, in addition to exercises such as the "Wheel of Misfortune,"7 to prepare engineers to react to on-call events.

Change Management
SRE has found that roughly 70% of outages are due to changes in a live system.

Best practices in this domain use automation to accomplish the following:
Implementing progressive rollouts
Quickly and accurately detecting problems
Rolling back changes safely when problems arise
This trio of practices effectively minimizes the aggregate number of users and operations exposed to bad changes.

By removing humans from the loop, these practices avoid the normal problems of fatigue, familiarity/contempt, and inattention to highly repetitive tasks.

As a result, both release velocity and safety increase.

Demand Forecasting and Capacity Planning
Demand forecasting and capacity planning can be viewed as ensuring that there is sufficient capacity and redundancy to serve projected future demand with the required availability.

Thereâs nothing particularly special about these concepts, except that a surprising number of services and teams donât take the steps necessary to ensure that the required capacity is in place by the time it is needed.

Capacity planning should take both organic growth (which stems from natural product adoption and usage by customers) and inorganic growth (which results from events like feature launches, marketing campaigns, or other business-driven changes) into account.

Several steps are mandatory in capacity planning:
An accurate organic demand forecast, which extends beyond the lead time required for acquiring capacity
An accurate incorporation of inorganic demand sources into the demand forecast
Regular load testing of the system to correlate raw capacity(servers, disks, and so on) to service capacity
Because capacity is critical to availability, it naturally follows that the SRE team must be in charge of capacity planning, which means they also must be in charge of provisioning.

Provisioning
Provisioning combines both change management and capacity planning.

In our experience, provisioning must be conducted quickly and only when necessary, as capacity is expensive.

This exercise must also be done correctly or capacity doesnât work when needed.

Adding new capacity often involves spinning up a new instance or location, making significant modification to existing systems (configuration files, load balancers, networking), and validating that the new capacity performs and delivers correct results.

Thus, it is a riskier operation than load shifting, which is often done multiple times per hour, and must be treated with a corresponding degree of extra caution.

Efficiency and Performance
Efficient use of resources is important any time a service cares about money.

Because SRE ultimately controls provisioning, it must also be involved in any work on utilization, as utilization is a function of how a given service works and how it is provisioned.

It follows that paying close attention to the provisioning strategy for a service, and therefore its utilization, provides a very, very big lever on the serviceâs total costs.

Resource use is a function of demand (load), capacity, and software efficiency.

SREs predict demand, provision capacity, and can modify the software.

These three factors are a large part (though not the entirety) of a serviceâs efficiency.

Software systems become slower as load is added to them.

A slowdown in a service equates to a loss of capacity.

At some point, a slowing system stops serving, which corresponds to infinite slowness.

SREs provision to meet a capacity target at a specific response speed, and thus are keenly interested in a serviceâs performance.

SREs and product developers will (and should) monitor and modify a service to improve its performance, thus adding capacity and improving efficiency.8
The End of the Beginning
Site Reliability Engineering represents a significant break from existing industry best practices for managing large, complicated services.

Motivated originally by familiarityâ"as a software engineer, this is how I would want to invest my time to accomplish a set of repetitive tasks"âit has become much more: a set of principles, a set of practices, a set of incentives, and a field of endeavor within the larger software engineering discipline.

The rest of the book explores the SRE Way in detail.

6Vice President, Google Engineering, founder of Google SRE
7See Disaster Role Playing.

8For further discussion of how this collaboration can work in practice, see Communications: Production Meetings.

Previous
Part I - Introduction
Next
Chapter 2 - The Production Environment at Google, from the Viewpoint of an SRE
Copyright Â© 2017 Google, Inc.

Published by O'Reilly Media, Inc.

Licensed under CC BY-NC-ND 4.0