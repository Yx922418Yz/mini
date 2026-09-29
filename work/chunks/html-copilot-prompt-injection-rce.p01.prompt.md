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

This post is about an important, but also scary, prompt injection discovery that leads to full system compromise of the developer’s machine in GitHub Copilot and VS Code.
It is achieved by placing Copilot into YOLO mode by modifying the project’s settings.json file.
As described a few days ago with Amp, a vulnerability pattern in agents that might be overlooked is that if an agent can write to files and modify its own configuration or update security-relevant settings it can lead to remote code execution. This is not uncommon and is an area to always look for when performing a security review.
Background Research
When looking at VS Code and GitHub Copilot Agent Mode I noticed a strange behavior… it can create and write to files in the workspace without user approval.
The edits are immediately persistent, they are not in-memory as a diff to review. The modifications are written to disk right away.
It’s one of these things that as a red teamer you know is probably not good… so I was looking if this could be used to escalate privileges and execute code.
YOLO Mode
So, next I researched features in VS Code that depend on settings that are within the project/workspace folder, and quickly found an interesting one.
It turns out that in the .vscode/settings.json file one can add the following line:
"chat.tools.autoApprove": true
This will put GitHub Copilot in YOLO mode.
And it disables all user confirmations, and we can run shell commands, browse the web, and more!
What is interesting is that this is an experimental feature, but it is still present by default. I did not download a special version or set my VS Code overall into an experimental mode.
Furthermore, it works on Windows, macOS and also Linux.
Exploit Chain Explained
The proof-of-concept exploit chain to hijack Copilot and escalate privileges is as follows:
The attack starts with a prompt injection planted in a source code file, web page, GitHub issue, tool call response, or other content… The payload can also use invisible text as instructions.
The prompt injection first adds the line “chat.tools.autoApprove”: true, to the ~/.vscode/settings.json file. Folder and file will be created if they don’t exist yet.
GitHub Copilot immediately enters YOLO mode!
Attack runs a Terminal command. And using conditional prompt injection we can actually target what to run based on the operating system.
We achieved Remote Code Execution powered by Prompt Injection.
Here is a screenshot that shows the demo file with the prompt injection, the developer interacting with the file on the right side in the chat box, and the calculator popping up!
Of course any other means of prompt injection delivery, like web or data coming back from an MCP server is an attack angle. I just used it inside the source code file because it’s easiest to test with.
Video Walkthrough
Short Demos
Here is a demonstration video that shows the code execution on Windows.
And this one on macOS:
Walkthrough
Here is a longer form video explaining the discovery and exploit in detail:
AI that can set its own permissions and configuration settings is wild!
Joining the Workstation to a Botnet - ZombAIs
Of course, this means we can join the developer’s machine to a botnet as a ZombAI.
Also, for fun we can modified the settings.json file to switch VS Code into a Red color scheme and similar things.
It doesn’t end here though! This also means we can build an actual AI virus that attaches to files and propagates as developers download and interact with infected files.
Last but not least, to demonstrate that we have full control of the developer’s host, we show that Copilot can be hijacked to download malware, and join a remote command and control server.
This means the door is open for malware, ransomware, info stealers, etc.
Scary stuff.
Building an AI Virus
When seeing this, one will notice that this basically allows the creation of a virus. An attacker can embed instructions and once they gain code execution, additional malware can compromise other Git projects (and RAG sources) to embed the malicious instructions, and commit the changes or even force push them upstream.
This can lead to further spread as other developers unknowingly propagate the infected code.
Finally, we also need to talk about invisible instructions!
Using Invisible Instructions
One might say that it would be quickly discovered if instructions are embedded as comments. So in order to make it a bit more interesting, I went ahead and created an invisible payload that achieves the attack chain, but is not visible to users. This was not as reliable, but it still worked:
Note: Although the demo here with invisible instructions worked multiple times for me, using invisible instructions often leads to the exploit being very unreliable, and is also commonly also refused by the model and there is also typically a visual indicator that VS Code shows about Unicode characters. However, attacks (and models) get better over time. It’s also worth highlighting that not all models are vulnerable to such invisible prompt injection attacks.
Recommendations and Fix
There are actually more attack angles then just the YOLO mode example I shared. When Microsoft asked me if there is any more info I have, I had looked a bit more and noticed there are other problematic places, for instance .vscode/tasks.json that the AI can write to, or adding fake malicious MCP servers, etc which can lead to code execution. And the AI can reconfigure the user interface and configuration settings of the project.
Recently I noticed that developers often use multiple agents, so there is also the threat of overwriting other agent configuration files (allow-list bash commands, add MCP servers…), as they are commonly in the project folder as well.
Ideally, the AI would not be able to modify files without a human first approving it. Many other editors do show the diff, which then can be approved by the developer.
Responsible Disclosure
After reporting the vulnerability on June 29, 2025 Microsoft confirmed the repro and asked a few follow up questions. A few weeks later MSRC pointed out that it is an issue they were already tracking, and that it will be patched by August. With the August Patch Tuesday release this is now fixed.
Shout out to Markus Vervier from Persistent Security who has also identified and reported this vulnerability to Microsoft. You can find their write-up here. And also a shout out to Ari Marzuk who seems to also have discovered it in parallel.
Thanks to the members of the MSRC and product team for the help in getting it mitigated.
Conclusion
This is another example of how an AI agent might not stay in its box! By modifying its own environment GitHub Copilot can escalate privileges and execute code to compromise the developer’s machine. It’s a not uncommon design flaw in agentic systems as I have discovered.
Keep looking out for such design flaws, these should be easily caught during threat modeling.
Cheers.
References
Month of AI Bugs 2025
Amp Code: Arbitrary Command Execution via Prompt Injection Fixed
Copilot Settings
CVE-2025-53773: GitHub Copilot and Visual Studio Remote Code Execution Vulnerability
Persistent Security Write-Up
Persistent Security
Newer →
Contact me
← Older