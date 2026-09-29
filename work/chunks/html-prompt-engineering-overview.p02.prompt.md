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

"What would happen if humans could travel at the speed of light?"
Opinion-Based Questions
Design prompts that elicit the AI's perspective or opinion on a specific topic, encouraging it to provide reasoning and justification for its stance.

"Do you believe that artificial intelligence will eventually surpass human intelligence?

Why or why not?"
Code Generation
Scenario
Instructions
Example Prompt
Code Completion
Provide the AI with a partial code snippet and prompt it to suggest or complete the remaining code based on the context and programming language.

"Write a Python function to calculate the factorial of a given number."
Code Translation
Specify the source and target programming languages to enable the AI to translate code while preserving functionality and syntax.

"Translate the following Python code to JavaScript: def greet(name): print('Hello,', name)"
Code Optimization
Prompt the AI to analyze existing code and suggest improvements for efficiency, readability, or performance.

"Optimize the following Python code to reduce its execution time."
Code Debugging
Provide the AI with code containing errors and prompt it to identify and suggest potential solutions for the identified issues.

"Debug the following Java code and explain why it is throwing a NullPointerException."
Scenario
Instructions
Example Prompt
Code Completion
Provide the AI with a partial code snippet and prompt it to suggest or complete the remaining code based on the context and programming language.

"Write a Python function to calculate the factorial of a given number."
Code Translation
Specify the source and target programming languages to enable the AI to translate code while preserving functionality and syntax.

"Translate the following Python code to JavaScript: def greet(name): print('Hello,', name)"
Code Optimization
Prompt the AI to analyze existing code and suggest improvements for efficiency, readability, or performance.

"Optimize the following Python code to reduce its execution time."
Code Debugging
Provide the AI with code containing errors and prompt it to identify and suggest potential solutions for the identified issues.

"Debug the following Java code and explain why it is throwing a NullPointerException."
Image Generation
Scenario
Instructions
Example Prompt
Photorealistic Images
Craft prompts that describe the desired image in detail, including objects, scenery, lighting, and style, to generate realistic and high-quality images.

"A photorealistic image of a sunset over the ocean with palm trees silhouetted against the sky."
Artistic Images
Design prompts that specify art styles, techniques, and subject matter to guide the AI in creating images that mimic specific artistic movements or evoke certain emotions.

"An impressionist painting of a bustling city street with people walking under umbrellas in the rain."
Abstract Images
Formulate prompts that encourage the AI to generate images that are open to interpretation, utilizing shapes, colors, and textures to evoke feelings or concepts.

"An abstract image representing the concept of hope, using bright colors and flowing shapes."
Image Editing
Provide the AI with an existing image and specify desired modifications, enabling it to edit and enhance the image according to the given instructions.

"Change the background of this photo to a starry night sky and add a full moon." or "Remove the person from this image and replace them with a cat."
Scenario
Instructions
Example Prompt
Photorealistic Images
Craft prompts that describe the desired image in detail, including objects, scenery, lighting, and style, to generate realistic and high-quality images.

"A photorealistic image of a sunset over the ocean with palm trees silhouetted against the sky."
Artistic Images
Design prompts that specify art styles, techniques, and subject matter to guide the AI in creating images that mimic specific artistic movements or evoke certain emotions.

"An impressionist painting of a bustling city street with people walking under umbrellas in the rain."
Abstract Images
Formulate prompts that encourage the AI to generate images that are open to interpretation, utilizing shapes, colors, and textures to evoke feelings or concepts.

"An abstract image representing the concept of hope, using bright colors and flowing shapes."
Image Editing
Provide the AI with an existing image and specify desired modifications, enabling it to edit and enhance the image according to the given instructions.

"Change the background of this photo to a starry night sky and add a full moon." or "Remove the person from this image and replace them with a cat."
Strategies for writing better prompts
Developing effective prompts requires a strategic approach.

Consider these strategies to enhance your prompt engineering skills:
1.

Set Clear Goals and Objectives:
Tactic
Prompt Example
Use action verbs to specify the desired action
"Write a bulleted list that summarizes the key findings of the attached research paper"
Define the desired length and format of the output
"Compose a 500-word essay discussing the impact of climate change on coastal communities."
Specify the target audience
"Write a product description for a new line of organic skincare products, targeting young adults concerned with sustainability."
Tactic
Prompt Example
Use action verbs to specify the desired action
"Write a bulleted list that summarizes the key findings of the attached research paper"
Define the desired length and format of the output
"Compose a 500-word essay discussing the impact of climate change on coastal communities."
Specify the target audience
"Write a product description for a new line of organic skincare products, targeting young adults concerned with sustainability."
2.

Provide Context and Background Information:
Tactic
Prompt Example
Include relevant facts and data
"Given that global temperatures have risen by 1 degree Celsius since the pre-industrial era, discuss the potential consequences for sea level rise."
Reference specific sources or documents
"Based on the attached financial report, analyze the company's profitability over the past five years."
Define key terms and concepts
"Explain the concept of quantum computing in simple terms, suitable for a non-technical audience."
Tactic
Prompt Example
Include relevant facts and data
"Given that global temperatures have risen by 1 degree Celsius since the pre-industrial era, discuss the potential consequences for sea level rise."
Reference specific sources or documents
"Based on the attached financial report, analyze the company's profitability over the past five years."
Define key terms and concepts
"Explain the concept of quantum computing in simple terms, suitable for a non-technical audience."
3.

Use Few-Shot Prompting:
Tactic
Prompt Example
Provide a few examples of desired input-output pairs
Input: "Cat" Output: "A small furry mammal with whiskers." Input: "Dog" Output: "A domesticated canine known for its loyalty." Prompt: "Elephant"
Demonstrate the desired style or tone
Example 1 (humorous): "The politician's speech was so dull, it could cure insomnia." Example 2 (formal): "The dignitary delivered an address that was both informative and engaging." Prompt: "Write a sentence describing the comedian's stand-up routine."
Show the desired level of detail
Example 1 (brief): "The movie was about a young boy who befriends an alien." Example 2 (detailed): "The science fiction film follows the story of Elliot, a lonely boy who discovers and forms a unique bond with an extraterrestrial stranded on Earth." Prompt: "Summarize the plot of the novel you just finished reading."
Tactic
Prompt Example
Provide a few examples of desired input-output pairs
Input: "Cat" Output: "A small furry mammal with whiskers." Input: "Dog" Output: "A domesticated canine known for its loyalty." Prompt: "Elephant"
Demonstrate the desired style or tone
Example 1 (humorous): "The politician's speech was so dull, it could cure insomnia." Example 2 (formal): "The dignitary delivered an address that was both informative and engaging." Prompt: "Write a sentence describing the comedian's stand-up routine."
Show the desired level of detail
Example 1 (brief): "The movie was about a young boy who befriends an alien." Example 2 (detailed): "The science fiction film follows the story of Elliot, a lonely boy who discovers and forms a unique bond with an extraterrestrial stranded on Earth." Prompt: "Summarize the plot of the novel you just finished reading."
4.

Be Specific:
Tactic
Prompt Example
Use precise language and avoid ambiguity
Instead of: "Write something about climate change," use: "Write a persuasive essay arguing for the implementation of stricter carbon emission regulations."
Quantify your requests whenever possible
Instead of: "Write a long poem," use: "Write a sonnet with 14 lines that explores themes of love and loss."
Break down complex tasks into smaller steps
Instead of: "Create a marketing plan," use: "1.

Identify the target audience.

2.