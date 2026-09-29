# 站点可靠性工程简介（导读）

> 来源：Benjamin Treynor Sloss（编者：Betsy Beyer，摘自 Google SRE 书籍） · 文章 id：`html-sre-introduction` · 原文约 26.1K 字符

## 核心主张
本文是 Google SRE 书籍的第 1 章「Introduction」，作者 Benjamin Treynor Sloss（编者 Betsy Beyer）系统解释了什么是站点可靠性工程（SRE），以及它为何产生。核心论点是：传统系统管理员（sysadmin）模式会随服务规模线性扩张、人力不堪重负，因此需要用软件工程手段来自动化运维；同时 SRE 通过「错误预算（error budget）」这一机制，化解开发团队想快速上线、运维团队想稳定运行的激励冲突。

## 关键要点（原文引用）
- 开篇立场鲜明：`Hope is not a strategy.`（指望不出事不是策略），点明可靠性必须靠工程与数据而非运气。
- 对比两种模式：传统 sysadmin 方式靠拼装现有软件组件（assembling existing software components）把它们组合起来提供服务；这种 ops 团队会随服务规模线性扩张（scales linearly with service size），最终只能不断加人。
- SRE 主张用具备软件工程能力的工程师来承担运维，用自动化替代人工重复操作。
- 关键约束：SRE 应将不超过 `50%` 的时间用于运维（ops）工作，其余 `50%` 用于开发工作；这一上限防止团队被日常工单淹没。
- 错误预算的量化示例：`99.99%` 的可用性目标意味着 `0.01%` 的不可用时间，这个额度就是 error budget。
- 把可用性目标设为 `100%` 是错误的目标（wrong target）：既不现实，也会扼杀发布与创新。
- 错误预算把「快」与「稳」的冲突变成可度量的共同目标，让团队在同一框架下做取舍。
- 系统出故障是预期之内的（outages are expected），因此重点不是追求零故障，而是缩短恢复时间。
- 监控（monitoring）不能只靠人看仪表盘，应让软件去解释与判断监控输出。
- SRE 的典型输出/工作产物包括 Alerts、Tickets、Logging 三类。
- 应急响应（emergency response）的核心是降低 MTTR（平均恢复时间）。
- playbook（预案手册）可显著改善 MTTR，原文中给出的量级约是 `3x` 的提升。
- 原文中的工程判断：`Hope is not a strategy.` 应被制度化为可度量的目标（如 error budget），而非口号。

## 术语与译法
- `Site Reliability Engineering` → 站点可靠性工程
- `Service Level Agreement` → 服务等级协议
- `On-call` → 值班
- `Incident` → 事故
- `Troubleshooting` → 排障
- `Latency` → 延迟
- `Throughput` → 吞吐量

## 结论
SRE 的本质是用软件工程方法解决运维规模化问题，并用「50% 运维上限」和「错误预算」两个机制，把可靠性与发布速度这对张力转化为可管理的工程目标。
