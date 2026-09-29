# 提示工程总览与指南（导读）

> 来源：Google Cloud · 文章 id：`html-prompt-engineering-overview` · 原文约 23.6K 字符

## 核心主张
本文由 Google Cloud 出品（页面标注 Last Updated: 01/14/2026），系统介绍围绕大语言模型（LLM）的新兴技能「提示工程（Prompt Engineering）」，回答两个问题：什么是提示工程、如何为 AI 写出好提示词（Prompt）。核心论点是：要让模型准确理解意图、遵循指令并产出期望结果，关键在于精心设计提示词的格式、上下文与示例；提示词相当于交给 AI 的一张 roadmap，把它导向你心中的具体输出。因此提示工程成为保证人机交互准确、相关且安全的关键能力。

## 关键要点（原文引用）
- 定义：提示工程是 "the art and science of designing and optimizing prompts to guide AI models, particularly LLMs, towards generating the desired responses"；它通过提供 context、instructions 与 examples 让模型理解你的 intent。
- 有效提示的四大要素：Prompt format、Context and examples、Fine-tuning and adapting、Multi-turn conversations。
- 提示词类型：Direct prompts (Zero-shot)、One-, few- and multi-shot prompts、Chain of Thought Prompts，以及把二者结合的 Zero-shot CoT Prompts。
- 用例覆盖四大类：Language and Text Generation（Creative Writing / Summarization / Translation / Dialogue）、Question Answering（Open-Ended / Specific / Multiple Choice / Hypothetical / Opinion-Based）、Code Generation（Code Completion / Code Translation / Code Optimization / Code Debugging）、Image Generation（Photorealistic / Artistic / Abstract / Image Editing）。
- 写出更好提示词的 6 条策略：1）Set Clear Goals and Objectives；2）Provide Context and Background Information；3）Use Few-Shot Prompting；4）Be Specific；5）Iterate and Experiment；6）Leverage Chain of Thought Prompting。
- 具体化与量化示例：把 "Write something about climate change" 改成 "Write a persuasive essay arguing for the implementation of stricter carbon emission regulations"；把 "Write a long poem" 改成 "Write a sonnet with 14 lines that explores themes of love and loss"；把 "Create a marketing plan" 拆成 "1. Identify the target audience. 2. Develop key marketing messages. 3. Choose appropriate marketing channels."。
- Few-shot 示例格式：Input: "Cat" Output: "A small furry mammal with whiskers." Input: "Dog" Output: "A domesticated canine known for its loyalty." Prompt: "Elephant"。
- 思维链示例："Solve this problem step-by-step: John has 5 apples, he eats 2. How many apples does he have left?"，引导模型逐步推理并解释其 reasoning process。
- 代码相关示例："Write a Python function to calculate the factorial of a given number."、"Optimize the following Python code to reduce its execution time."、"Debug the following Java code and explain why it is throwing a NullPointerException."。
- 提示工程的收益：Improved model performance、Reduced bias and harmful responses、Increased control and predictability、Enhanced user experience。
- 相关 Google Cloud 产品：Vertex AI Platform、Generative AI on Vertex AI、AI APIs、Model Garden on Vertex AI；新客户可获 $300 免费额度。

## 术语与译法
- `Prompt Engineering` → 提示工程
- `Prompt` → 提示词
- `LLM` → 大语言模型

## 结论
提示工程是驾驭 LLM 的核心技能，本质是用清晰的格式、充分的上下文与恰当示例把意图传达给模型；掌握提示词类型、6 条写作策略与迭代实验习惯，即可显著提升输出的准确性与可控性。
