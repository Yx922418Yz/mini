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

Prompt Engineering for AI Guide | Google Cloud
Prompt engineering: overview and guide
Last Updated: 01/14/2026
The rise of large language models (LLMs) has brought forth exciting possibilities for human-computer interaction.

However, harnessing the full potential of these powerful AI models requires a crucial skill: prompt engineering.

This burgeoning field focuses on crafting effective prompts that unlock the capabilities of LLMs, enabling them to understand intent, follow instructions, and generate desired outputs.

As we increasingly interact with AI in various applications, prompt engineering plays a vital role in ensuring accurate, relevant, and safe interactions.

Get started for free
Try chat prompts
1:53
Tips to becoming a world-class Prompt Engineer
What is prompt engineering?

Prompt engineering is the art and science of designing and optimizing prompts to guide AI models, particularly LLMs, towards generating the desired responses.

By carefully crafting prompts, you provide the model with context, instructions, and examples that help it understand your intent and respond in a meaningful way.

Think of it as providing a roadmap for the AI, steering it towards the specific output you have in mind.

To dive deeper into the world of prompt design and explore its applications, check out the Introduction to Prompt Design on Google Cloud.

Ready to experiment with LLMs and prompt engineering firsthand?

Try the Vertex AI free trial and experience the power of this technology.

What is a prompt for AI?

In the context of AI, a prompt is the input you provide to the model to elicit a specific response.

This can take various forms, ranging from simple questions or keywords to complex instructions, code snippets, or even creative writing samples.

The effectiveness of your prompt directly influences the quality and relevance of the AI's output.

What do you need for prompt engineering?

Several key elements contribute to effective prompt engineering.

Mastering these allows you to communicate effectively with AI models and unlock their full potential.

Prompt format
The structure and style of your prompt play a significant role in guiding the AI's response.

Different models may respond better to specific formats, such as:
The format of your prompt plays a significant role in how the AI interprets your request.

Different models may respond better to specific formats, such as natural language questions, direct commands, or structured inputs with specific fields.

Understanding the model's capabilities and preferred format is essential for crafting effective prompts.

Context and examples
Providing context and relevant examples within your prompt helps the AI understand the desired task and generate more accurate and relevant outputs.

For instance, if you're looking for a creative story, including a few sentences describing the desired tone or theme can significantly improve the results.

Fine-tuning and adapting
Fine-tuning the AI model on specific tasks or domains using tailored prompts can enhance its performance.

Additionally, adapting prompts based on user feedback or model outputs can further improve the model's responses over time.

Multi-turn conversations
Designing prompts for multi-turn conversations allows users to engage in continuous and context-aware interactions with the AI model, enhancing the overall user experience.

Types of prompts
There are various types of prompts used in AI, each serving a specific purpose:
Direct prompts (Zero-shot)
Zero-shot prompting involves providing the model with a direct instruction or question without any additional context or examples.

An example of this is idea generation, where the model is prompted to generate creative ideas or brainstorming solutions.

Another example is summarization, or translation, where the model is asked to summarize or translate some piece of content.

One-, few- and multi-shot prompts
This method involves providing the model with one or more examples of the desired input-output pairs before presenting the actual prompt.

This can help the model better understand the task and generate more accurate responses.

Chain of Thought Prompts
CoT prompting encourages the model to break down complex reasoning into a series of intermediate steps, leading to a more comprehensive and well-structured final output.

Zero-shot CoT Prompts
Combines chain of thought prompting with zero-shot prompting by asking the model to perform reasoning steps, which may often produce better output.

Use cases and examples of prompt engineering
Here are some specific examples and use cases showing how prompt engineering helps produce customized and relevant output.

Language and Text Generation
Scenario
Instructions
Example Prompt
Creative Writing
Craft prompts that specify genre, tone, style, and plot points to guide the AI in generating engaging narratives.

"Write a short story about a young woman who discovers a magical portal in her attic."
Summarization
Provide the AI with text and instruct it to generate concise summaries that capture key information.

“Summarize the main points of the following news article on climate change."
Translation
Specify the source and target languages to enable the AI to accurately translate text while preserving meaning and context.

"Translate the following text from English to Spanish: 'The quick brown fox jumps over the lazy dog.'"
Dialogue
Design prompts that simulate conversations, allowing the AI to generate responses that mimic human interaction and maintain context.

"You are a friendly chatbot helping users troubleshoot their computer problems.

Respond to the user's query: 'My computer won't turn on.'"
Scenario
Instructions
Example Prompt
Creative Writing
Craft prompts that specify genre, tone, style, and plot points to guide the AI in generating engaging narratives.

"Write a short story about a young woman who discovers a magical portal in her attic."
Summarization
Provide the AI with text and instruct it to generate concise summaries that capture key information.

“Summarize the main points of the following news article on climate change."
Translation
Specify the source and target languages to enable the AI to accurately translate text while preserving meaning and context.

"Translate the following text from English to Spanish: 'The quick brown fox jumps over the lazy dog.'"
Dialogue
Design prompts that simulate conversations, allowing the AI to generate responses that mimic human interaction and maintain context.

"You are a friendly chatbot helping users troubleshoot their computer problems.

Respond to the user's query: 'My computer won't turn on.'"
Question Answering
Scenario
Instructions
Example Prompt
Open-Ended Questions
Formulate prompts that encourage the AI to provide comprehensive and informative answers based on its knowledge base.

"Explain the concept of quantum computing and its potential impact on the future of technology."
Specific Questions
Design prompts that target specific information, enabling the AI to retrieve precise answers from the provided context or its internal knowledge base.

"What is the capital of France?" or "According to the provided text, what are the main causes of deforestation?"
Multiple Choice Questions
Present prompts with options, prompting the AI to analyze and select the most appropriate answer based on its understanding of the context.

"Who wrote the Harry Potter series?

A) J.R.R.

Tolkien, B) J.K.

Rowling, C) Stephen King"
Hypothetical Questions
Craft prompts that explore hypothetical situations, allowing the AI to reason, speculate, and provide potential outcomes or solutions.

"What would happen if humans could travel at the speed of light?"
Opinion-Based Questions
Design prompts that elicit the AI's perspective or opinion on a specific topic, encouraging it to provide reasoning and justification for its stance.

"Do you believe that artificial intelligence will eventually surpass human intelligence?

Why or why not?"
Scenario
Instructions
Example Prompt
Open-Ended Questions
Formulate prompts that encourage the AI to provide comprehensive and informative answers based on its knowledge base.

"Explain the concept of quantum computing and its potential impact on the future of technology."
Specific Questions
Design prompts that target specific information, enabling the AI to retrieve precise answers from the provided context or its internal knowledge base.

"What is the capital of France?" or "According to the provided text, what are the main causes of deforestation?"
Multiple Choice Questions
Present prompts with options, prompting the AI to analyze and select the most appropriate answer based on its understanding of the context.

"Who wrote the Harry Potter series?

A) J.R.R.

Tolkien, B) J.K.

Rowling, C) Stephen King"
Hypothetical Questions
Craft prompts that explore hypothetical situations, allowing the AI to reason, speculate, and provide potential outcomes or solutions.