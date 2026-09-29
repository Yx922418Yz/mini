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

As our simulated attacks demonstrate, a wide variety of prompt payloads can trigger the same weakness, underscoring how flexible and evasive these threats can be.

Securing AI agents requires more than ad hoc fixes.

It demands a defense-in-depth strategy that spans prompt hardening, input validation, secure tool integration and robust runtime monitoring.

General-purpose security mechanisms alone are insufficient.

Organizations must adopt purpose-built solutions — such as Palo Alto Networks Prisma AIRS — to Discover, Assess and Protect threats unique to agentic applications.

Palo Alto Networks customers are better protected from the threats discussed above through the following products:
A Unit 42 AI Security Assessment can help you proactively identify the threats most likely to target your AI environment.

If you think you may have been compromised or have an urgent matter, get in touch with the Unit 42 Incident Response team or call:
North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
UK: +44.20.3743.3660
Europe and Middle East: +31.20.299.3130
Asia: +65.6983.8730
Japan: +81.50.1790.0200
Australia: +61.2.4062.7950
India: 00080005045107
Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members.

CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors.

Learn more about the Cyber Threat Alliance.

Additional Resources
Stock Advisory Assistant – GitHub
CrewAI – CrewAI Documentation
CrewAI – CrewAI GitHub Repository
SerperDevTool – CrewAI GitHub Repository
ScrapeWebsiteTool – CrewAI GitHub Repository
Hierarchical Process – CrewAI Documentation
AutoGen – AutoGen Documentation
AutoGen – AutoGen GitHub Repository
Swarm – AutoGen Documentation
About VM metadata – Google Cloud Documentation
OWASP Top 10 for LLMs – OWASP
OWASP Agentic AI Threats and Mitigation – OWASP
Nasdaq – Nasdaq
Updated May 2, 2025, at 2:20 p.m.

PT to update product language.

Tags
Agentic AI
AI
BOLA
GenAI
Prompt injection
Threat Research Center
Next: Gremlin Stealer: New Stealer on Sale in Underground Forum
Table of Contents
Related Articles
Double Agents: Exposing Security Blind Spots in GCP Vertex AI
Threat Brief: March 2026 Escalation of Cyber Risk Related to Iran (Updated March 26)
Who’s Really Shopping?

Retail Fraud in the Age of Agentic AI
Related Malware Resources
High Profile Threats April 1, 2026
Threat Brief: Widespread Impact of the Axios Supply Chain Attack
API attacks
JavaScript
Supply chain
Read now
High Profile Threats March 31, 2026
Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure
CVE-2025-55182
GitHub
Infostealer
Read now
Threat Research March 31, 2026
Double Agents: Exposing Security Blind Spots in GCP Vertex AI
Agentic AI
Data exfiltration
GCP
Read now
High Profile Threats March 26, 2026
Threat Brief: March 2026 Escalation of Cyber Risk Related to Iran (Updated March 26)
APK
DDoS attacks
GenAI
Read now
Threat Actor Groups March 26, 2026
Converging Interests: Analysis of Threat Clusters Targeting a Southeast Asian Government
CL-STA-1048
CL-STA-1049
Stately Taurus
Read now
Threat Research March 24, 2026
Threat Brief: Recruiting Scheme Impersonating Palo Alto Networks Talent Acquisition Team
Email scam
Lure
Phishing
Read now
Threat Research March 19, 2026
Analyzing the Current State of AI Use in Malware
.NET
ChatGPT
GenAI
Read now
Threat Research March 17, 2026
Open, Closed and Broken: Prompt Fuzzing Finds LLMs Still Fragile Across Open and Closed Models
Evasion
GenAI
LLM
Read now
Threat Research March 12, 2026
Suspected China-Based Espionage Operation Against Military Targets in Southeast Asia
Advanced Persistent Threat
AppleChris
Backdoor
Read now
Threat Research March 10, 2026
Auditing the Gatekeepers: Fuzzing "AI Judges" to Bypass Security Controls
AI
Fuzzing
LLM
Read now