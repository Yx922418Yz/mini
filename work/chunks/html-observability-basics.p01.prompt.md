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

Apr 23rd, 2025
Traces & Spans: Observability Basics You Should Know
Learn how traces and spans help you see inside distributed systems—so you can troubleshoot faster and build more reliable software.

Anjali Udasi
Contents
In modern software architecture, applications aren't just getting bigger—they're getting more distributed.

With microservices, serverless functions, and containers running across multiple environments, understanding what's happening inside your systems can feel like trying to track a single raindrop in a storm.

That's where traces and spans come in.

These observability tools aren't just buzzwords—they're your secret weapon for making sense of complex distributed systems.

Let's break down what traces and spans are, why they matter, and how you can use them to troubleshoot faster and build more reliable systems.

Understanding Traces and Spans: Core Concepts
Traces capture the journey of a request as it moves through your distributed system.

Think of a trace as the complete story of a request from start to finish—from when a user clicks a button until they see the result.

Spans are the building blocks of traces.

Each span represents a unit of work within that journey—like a database query, an API call, or a function execution.

Spans nest within each other to show parent-child relationships between operations.

Here's the relationship in simple terms:
A trace contains multiple spans
Each span represents one operation
Spans have timing data and metadata
Spans can be nested to show how operations relate to each other
Trace
├── Span (API Gateway)
│ ├── Span (Auth Service)
│ └── Span (User Service)
│ └── Span (Database Query)
└── Span (Response Formatting)💡
If you're curious how traces and spans fit alongside metrics, logs, and events, this post breaks down all four.

Benefits of Traces and Spans for DevOps Professionals
You're running a complex system with dozens of microservices.

Suddenly, users report the checkout process is slow.

Without tracing, you'd need to check each service individually, wasting precious time.

With traces and spans, you can:
Find bottlenecks instantly: See exactly which service or function is taking too long
Debug across service boundaries: Follow requests as they jump between services
Understand dependencies: Visualize how your services connect and depend on each other
Improve performance: Identify and fix slow operations with precision
Reduce mean time to recovery (MTTR): Get to the root cause faster when issues arise
Technical Implementation of Traces and Spans
Let's get into the nuts and bolts of how tracing works in distributed systems.

Trace Context and Propagation
For tracing to work across service boundaries, each service needs to know it's handling part of the same request.

This happens through context propagation—passing a trace ID and span ID between services.

When a request first hits your system, it gets assigned a unique trace ID.

As the request moves between services, this ID travels with it (usually as HTTP headers).

Each service then creates its own spans but links them to the same trace.

Span Attributes and Events
Spans aren't just timestamps—they're rich with data:
Name: What operation this span represents
Timing: Start and end times
Status: Success, error, etc.

Attributes: Custom key-value pairs (like user_id or cart_size)
Events: Notable occurrences within the span
Links: Connections to other spans
Sampling Strategies
Tracing everything can create massive amounts of data.

That's why most systems use sampling—collecting only a percentage of traces.

Smart sampling strategies include:
Head-based sampling: Decide whether to sample at the beginning of a request
Tail-based sampling: Decide after the request completes (better for catching errors)
Priority sampling: Always trace important operations, but sample routine ones
💡
If you're looking to understand the differences between observability, telemetry, and monitoring, check out this helpful post: Observability vs Telemetry vs Monitoring.

Tracing Implementation Guide: Tools and Frameworks
Ready to add tracing to your systems?

Here's what you need:
OpenTelemetry: The Industry Standard
OpenTelemetry has become the go-to framework for implementing traces and spans.

It provides:
Libraries for all major programming languages
A vendor-neutral API and SDK
Automatic instrumentation for popular frameworks
A consistent way to collect and export data
The Tracing Toolbox
Several tools can help you collect, store, and visualize your traces:
Tool
Type
Best For
Last9
All-in-one observability
Cost-effective, high-cardinality observability with predictable pricing
Jaeger
Open-source tracing
Self-hosted tracing visualization
Zipkin
Open-source tracing
Simple distributed tracing
Grafana Tempo
Tracing backend
Integration with Grafana dashboards
OpenTelemetry Collector
Data collection pipeline
Processing and routing telemetry data
If you're after an observability solution that fits your budget, Last9 is worth checking out.

With pricing based on ingested events, it keeps things predictable.

Plus, our platform handles high-cardinality data at scale and integrates with OpenTelemetry and Prometheus to bring your metrics, logs, and traces together in one place.

Implementing Tracing in Your Code
Here's a simplified example of how to create spans in a Node.js application using OpenTelemetry:
// Initialize the OpenTelemetry SDK (once in your app)
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');
const { SimpleSpanProcessor } = require('@opentelemetry/sdk-trace-base');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');
const provider = new NodeTracerProvider();
const exporter = new OTLPTraceExporter({
url: 'http://localhost:4318/v1/traces',
});
provider.addSpanProcessor(new SimpleSpanProcessor(exporter));
provider.register();
// Get a tracer
const { trace } = require('@opentelemetry/api');
const tracer = trace.getTracer('my-service');
// Create spans in your code
async function processOrder(orderId) {
const span = tracer.startSpan('process-order');
// Add attributes to the span
span.setAttribute('order.id', orderId);
span.setAttribute('customer.type', 'premium');
try {
// Do work...

// Create a child span
const dbSpan = tracer.startSpan('database-query', {
parent: span,
});
try {
// Run database query...

dbSpan.end();
} catch (error) {
dbSpan.setStatus({ code: SpanStatusCode.ERROR });
dbSpan.recordException(error);
dbSpan.end();
throw error;
}
span.end();
} catch (error) {
span.setStatus({ code: SpanStatusCode.ERROR });
span.recordException(error);
span.end();
throw error;
}
}💡
Wondering how OpenTelemetry stacks up against traditional APM tools?

This post breaks down the key differences: OpenTelemetry vs Traditional APM Tools.

Advanced Tracing Techniques
Once you've got basic tracing in place, these advanced techniques can take your observability to the next level.

Distributed Context Management
In complex systems, you need to manage context beyond just trace IDs.

The W3C Trace Context specification provides standards for:
traceparent: Contains the trace ID and parent span ID
tracestate: Allows vendors to add custom context data
Using these headers ensures your tracing works across different services and vendors.

Correlation Between Traces, Metrics, and Logs
The real power of observability comes from connecting different signals:
Exemplar traces: Link metrics to the traces that generated them
Trace IDs in logs: Add trace IDs to log messages for cross-referencing
Custom attributes: Use consistent attributes across all telemetry types
Error Handling and Exception Tracking
When exceptions occur, spans can provide crucial context:
Mark spans with error status
Record exceptions with stack traces
Add events to spans that show the error's progression
Create baggage items that carry error context across service boundaries
💡
For a deeper look at staying ahead of issues and improving system reliability, check out this post on proactive monitoring: Proactive Monitoring.