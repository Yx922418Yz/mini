# 上下文腐化：输入词元增长如何影响大语言模型表现（导读）

> 来源：Chroma（作者 Kelly Hong、Anton Troynikov、Jeff Huber，July 2025，技术报告）· 文章 id：`html-context-rot` · 原文约 50.3K 字符

## 核心主张
以 Needle in a Haystack（NIAH）为代表的长上下文基准测试本质是简单的词汇检索任务，模型在其上近乎满分，容易让人误以为长上下文性能是均匀的。本文通过一系列刻意受控、尽量简单的实验证明：即使在最简条件下，随着输入长度增长，模型表现也会下降，且下降方式往往出人意料、并不均匀；真实应用复杂度更高，输入长度的影响在实践中有可能被进一步放大。

## 关键要点（原文引用）
- 动机：最新模型输入上下文已达到数百万 token（Gemini 1.5 Pro 于 2024 年初率先引入 1M 上下文窗口，随后 GPT-4.1 为 1M，Llama 4 达 10M），但 NIAH 只是直接词汇匹配，可能无法代表灵活的语义任务。
- 作者在标准 NIAH 基础上扩展，并加入一个使用 LongMemEval 的对话式问答评估，以及一个让模型复述一串重复词元的合成任务。
- 四组主要实验：Needle-Question Similarity（针与问题的相似度）、Impact of Distractors（干扰项的影响）、Needle-Haystack Similarity（针与草堆的相似度）、Haystack Structure（草堆结构）。
- 贯穿结论：即使在这些最简条件下，模型表现也会随输入长度增加而下降，且呈现令人意外、非均匀的形态。
- 针与问题的相似度越低，随长度增长带来的性能退化越明显。
- 干扰项（distractors）的影响并不均匀，并且会随上下文长度被放大。
- 在所测试模型中，Claude 系列模型的幻觉率最低。
- LongMemEval 实验对比了完整约 113k tokens 与聚焦约 300 tokens 两种设置；从 500 条中过滤后保留 306 条 prompts，使用 LLM judge（GPT-4.1）评分，与人工对齐度超过 99%。
- Repeated Words 合成任务使用了 Claude Sonnet 4、GPT-4.1、Qwen3-32B 与 Gemini 2.5 Flash；输入长度与输出长度成正比。
- 在该任务中，Sonnet 3.5 直到 8192 上表现优于更新的 Claude 模型；Opus 4 的拒答率为 2.89%，GPT-4.1 的拒答率为 2.55%；准确率最高点出现在上下文接近开头处。
- 报告以 @techreport{hong2025context, title={Context Rot: How Increasing Input Tokens Impacts LLM Performance}, author={Hong, Kelly and Troynikov, Anton and Huber, Jeff}, year={2025}, month={July}, institution={Chroma}, url={https://trychroma.com/research/context-rot}} 形式给出引用。

## 术语与译法
- `Context Rot` → 上下文腐化
- `Context Window` → 上下文窗口
- `Long-context` → 长上下文
- `Token` → 词元
- `LLM` → 大语言模型
- `Benchmark` → 基准测试
- `Hallucination` → 幻觉
- `Evaluation` → 评估
- `Context Engineering` → 上下文工程
- `Retrieval-Augmented Generation` → 检索增强生成

## 结论
长上下文能力并非「越长越强」：即便在最精简的受控任务中，输入长度增长也会让大语言模型（LLM）表现以非均匀方式退化。作者据此强调上下文工程（Context Engineering）——真实应用需要比「把一切塞进上下文窗口」更精细的上下文管理。
