# Anthropic 团队如何使用 Claude Code

Anthropic 内部团队正在用 Claude Code 重塑各自的工作流，让开发者与非技术岗位的同事都能承接复杂项目、自动化任务，并弥合此前限制其生产力的技能鸿沟。

通过与自家 Claude Code 重度用户的访谈，我们收集了不同部门如何借助 Claude Code 的洞察、它对工作的影响，以及供其他正在考虑引入该工具的组织参考的建议。

ANTHROP\C

## 目录

| 章节 | 页码 |
| --- | --- |
| Claude Code 用于数据基础设施 | 3 |
| Claude Code 用于产品开发 | 5 |
| Claude Code 用于安全工程 | 7 |
| Claude Code 用于推理（inference） | 9 |
| Claude Code 用于数据科学与可视化 | 11 |
| Claude Code 用于 API | 13 |
| Claude Code 用于增长营销（growth marketing） | 15 |
| Claude Code 用于产品设计（product design） | 17 |
| Claude Code 用于强化学习（RL）工程 | 19 |
| Claude Code 用于法务 | 21 |

## Claude Code 用于数据基础设施

数据基础设施（Data Infrastructure）团队负责为全公司各团队组织所有业务数据。他们用 Claude Code 自动化日常的数据工程任务、排查复杂的基础设施问题，并为技术与非技术团队成员创建有文档记录的工作流，使他们能够独立访问和操作数据。

### Claude Code 主要使用场景

**用截图调试 Kubernetes**

当 Kubernetes 集群宕机、无法调度新的 Pod 时，团队用 Claude Code 来诊断问题。他们把仪表盘（dashboard）截图喂给 Claude Code，后者逐级引导他们浏览 Google Cloud 的 UI 菜单，直到发现一条提示 Pod IP 地址耗尽的告警。随后 Claude Code 给出了创建新 IP 池并将其加入集群的确切命令，从而无需引入网络方向的专家。

**面向财务团队的纯文本工作流**

团队向财务部门的成员演示了如何编写描述其数据工作流的纯文本文件，然后把这些文件加载进 Claude Code 以实现全自动执行。没有编程经验的员工可以描述诸如「查询这个仪表盘、获取信息、运行这些查询、产出 Excel 输出」这样的步骤，Claude Code 便会执行整个工作流，包括主动询问日期等必需输入。

**面向新员工的代码库导航**

当新的数据科学家加入团队时，会被引导使用 Claude Code 来熟悉其庞大的代码库。Claude Code 会阅读他们的 Claude.md 文件（文档），为特定任务定位相关文件，解释数据管道（data pipeline）的依赖关系，并帮助新成员理解哪些上游数据源最终流入仪表盘。这一做法取代了传统的数据目录与可发现性（discoverability）工具。

**会话结束时的文档更新**

团队会在每项任务结束时，让 Claude Code 总结已完成的工作会话并提出改进建议。这就形成了一个持续改进闭环：Claude Code 依据实际使用情况帮助打磨 Claude.md 文档与工作流说明，使后续迭代更有效。

**跨多个实例的并行任务管理**

在处理长时间运行的数据任务时，他们会在不同仓库中为不同项目打开多个 Claude Code 实例。每个实例都保持完整上下文，因此当他们数小时甚至数天后切回来时，Claude Code 仍清楚记得此前在做什么、进行到哪里，从而在不丢失上下文的前提下实现真正的并行工作流管理。
