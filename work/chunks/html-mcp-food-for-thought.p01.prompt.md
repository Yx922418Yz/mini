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

The Model Context Protocol (MCP) is a pretty big deal these days. It’s become the de facto standard for giving LLMs access to tools that someone else wrote, which, of course, turns them into agents. But writing tools for a new MCP server is hard, and so people often propose auto-converting existing APIs into MCP tools; typically using OpenAPI metadata (1, 2).
In my experience, this can work but it doesn’t work well. Here are a few reasons why:
Agents don’t do well with large numbers of tools
Infamously, VS Code has a hard limit of 128 tools - but many models struggle with accurate tool calling well before that number. Also, each tool and its description takes up valuable context window space.
Most web APIs weren’t designed with these constraints in mind! It’s fine to have umpteen APIs for a single product area when those APIs are called from code, but if each of those APIs is mapped to an MCP tool the results might not be great.
MCP tools designed from the ground up are typically much more flexible than individual web APIs, with each tool being able to do the work of several individual APIs.
APIs can blow through context windows quickly
Imagine an API that returns 100 records at a time, and each record is very wide (say, 50 fields). Sending those results to an agent as-is will use up a lot of tokens; even if a query can be satisfied with only a few fields, every field ends up in the context window.
APIs are typically paginated by the number of records, but records can vary a lot in size. One record might contain a large text field that takes up 100,000 tokens, while another might contain 10. Putting these API results directly into an agent’s context window is a gamble; sometimes it works, sometimes it will blow up.
The format of the data can also be an issue. Most web APIs these days return JSON, but JSON is a very token-inefficient format. Take this:
[
{
"firstName": "Alice",
"lastName": "Johnson",
"age": 28
},
{
"firstName": "Bob",
"lastName": "Smith",
"age": 35
}
]
Compare to the same data in CSV format:
firstName,lastName,age
Alice,Johnson,28
Bob,Smith,35
The CSV data is much more succinct - it uses up half as many tokens per record. Typically CSV, TSV, or YAML (for nested data) are better choices than JSON.
None of these issues are insurmountable. You could imagine automatically adding tool arguments that let agents project fields, automatically truncating or summarizing large results, and automatically converting JSON results to CSV (or YAML for nested data). But most servers I’ve seen do none of those things.
APIs don’t make the most of agents’ unique capabilities
APIs return structured data for programmatic consumption. That’s often what agents want from tool calls… but agents can also handle other, more free-form instructions.
For example an ask_question tool could perform a RAG query over some documentation, then return information in plain text that is used to inform the next tool call - skipping structured data entirely.
Or, a call to a search_cities tool could return a structured list of cities and a suggestion of what to call next:
city_name,population,country,region
Tokyo,37194000,Japan,Asia
Delhi,32941000,India,Asia
Shanghai,28517000,China,Asia
Suggestion: To get more specific information (weather, attractions, demographics), try calling get_city_details with the city_name parameter.
That sort of layering and tool chaining can be very effective in MCP servers, and it’s something you’ll miss out on completely if auto-converting APIs to tools.
If an agent needs to call an API, it could just do that
Agents like Claude Code are remarkably capable of writing+executing code these days, including scripts that call web APIs. Some people take this so far as to argue that MCP isn’t needed at all!
I disagree with that conclusion, but I do think we should skate to where the puck is going. Sandboxing of agents is improving rapidly, and if it’s easy+safe for an agent to call APIs directly then we might as well do that and cut out the middleman.
Conclusion
Agents are fundamentally different from the typical consumers of APIs. It’s possible to automatically create MCP tools from existing APIs, but doing that is unlikely to work well. Agents do best when given tools that are designed for their unique capabilities and limitations.