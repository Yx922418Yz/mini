# 链路追踪与跨度（Trace 与 Span）：不可或缺的可观测性基础（导读）

> 来源：Last9（作者 Anjali Udasi，2025-04-23） · 文章 id：`html-observability-basics` · 原文约 12.4K 字符

## 核心主张
文章要解决「请求跨越多个服务后，出错时难以定位瓶颈」的问题，主张用 trace 与 span 记录请求在分布式系统中的完整旅程，从而更快排障、理解服务依赖并提升可靠性。作者强调：没有 trace，开发者只能在日志与指标之间做推测；有了 trace，一次请求的每个操作及其耗时、上下文都能被精确重建。

## 关键要点（原文引用）
- `A trace contains multiple spans`——一次 trace 代表一个请求穿越整个系统的完整旅程。
- `Each span represents one operation`——每个 span 是过程中一个有名称、有时长的步骤（如一次 API 调用或数据库查询）。
- `Spans have timing data and metadata`（start time、duration、status、attributes/tags）——这些字段用于量化每个操作消耗的时间与结果。
- `Spans can be nested to show how operations relate to each other`——父/子 span 构成树状结构，直观呈现调用层级与依赖关系。
- trace 树示例：用户请求 → API Gateway → Auth Service / Order Service（→ Database、Payment Service → 第三方支付 API / Inventory Service → Cache 与 Database），每一层即一个 span。
- 排障价值：快速定位慢服务（如"Order Service 耗时 3.2s，其中 Database 查询占 2.8s"）、区分本服务问题还是下游依赖、看清因果链、缩短 MTTR。
- 关系定位：trace 与 metrics、logs 互补而非替代——trace 提供请求级上下文，metrics 做聚合趋势，logs 记录离散事件；三者结合才能完整观测系统。
- 实现与标准：OpenTelemetry（OTel）是跨厂商的采集/SDK 标准；上下文通过 W3C Trace Context 的 `traceparent` / `tracestate` 头在服务间传播，保证跨服务 span 归属同一 trace。
- 采样策略：head sampling（在 trace 起点决定，简单但可能丢关键慢请求）、tail sampling（先收集再决定，能保留错误/慢请求但成本更高）、priority sampling、adaptive sampling。
- 成本与开销：文章 FAQ 称合理实施下 tracing 的典型开销常低于 3%，数据量视系统规模从 GB 到 TB/天不等。
- 后端与工具：OpenTelemetry Collector 负责接收/处理/导出，常见后端包括 Jaeger、Zipkin、Grafana Tempo 与商业厂商（Last9、Datadog、New Relic 等）。

## 术语与译法
- `Observability` → 可观测性
- `Telemetry` → 遥测
- `Distributed Tracing` → 分布式链路追踪
- `Troubleshooting` → 排障
- `Latency` → 延迟

## 结论
trace 与 span 把「请求在分布式系统里的旅程」变成可量化、可下钻的数据，是定位延迟与故障根因的关键手段。落地时应以 OpenTelemetry 为统一标准、用 `traceparent` 做跨服务上下文传播，并配合 metrics/logs 形成完整的可观测性体系。
