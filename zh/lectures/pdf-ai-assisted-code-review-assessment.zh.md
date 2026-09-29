# pdf-ai-assisted-code-review-assessment（中文译稿）

> 原文：`ai-assisted-code-review-assessment.pdf` ｜ 段数：9 ｜ 原文字符：53103

---

# 现代代码评审中 AI 辅助的编码实践评估

**Manushree Vijayvergiya**（manushree@google.com，Google，瑞士苏黎世）
**Małgorzata Salawa**（magorzata@google.com，Google，瑞士苏黎世）
**Ivan Budiselić**（ibudiselic@google.com，Google，瑞士苏黎世）
**Dan Zheng**（danielzheng@google.com，Google，美国山景城）
**Pascal Lamblin**（lamblinp@google.com，Google，加拿大蒙特利尔）
**Marko Ivanković**（markoi@google.com，Google，瑞士苏黎世）
**Juanjo Carin**（juanjocarin@google.com，Google，美国森尼韦尔）
**Mateusz Lewko**（mlewko@google.com，Google，瑞士苏黎世）
**Jovan Andonov**（jandonov@google.com，Google，瑞士苏黎世）
**Goran Petrović**（goranpetrovic@google.com，Google，瑞士苏黎世）
**Daniel Tarlow**（dtarlow@google.com，Google，加拿大蒙特利尔）
**Petros Maniatis**（maniatis@google.com，Google，美国山景城）
**René Just**（rjust@cs.washington.edu，华盛顿大学，美国西雅图）

## 摘要

现代代码评审（modern code review）是一种流程：代码作者提交的增量式代码贡献，在被提交到版本控制系统之前，会由一名或多名同行进行评审。现代代码评审的一个重要环节，是核实代码贡献是否遵循最佳实践（best practices）。其中一些最佳实践可以自动校验，但另一些通常只能交由人工评审者来判断。本文报告了 AutoCommenter 的开发、部署与评估情况。AutoCommenter 是一个由大语言模型（large language model, LLM）支撑的系统，能够自动学习并强制执行编码最佳实践。我们为四种编程语言（C++、Java、Python 和 Go）实现了 AutoCommenter，并在大规模工业环境中评估了它的性能与采纳情况。我们的评估表明，一个端到端地学习并强制执行编码最佳实践的系统是可行的，并且对开发者工作流有积极影响。此外，本文还报告了将这样一个系统部署给数万名开发者所面临的挑战，以及相应的经验教训。

## CCS 概念

- **软件及其工程** → 软件验证与确认。

† 本工作完成于 Google 期间。

个人使用或课堂教学目的下，允许免费制作本作品全部或部分的数字或纸质副本，前提是这些副本不用于营利或商业利益，且副本上须保留本声明与首页的完整引用。第三方组件的版权须予以尊重。其他用途请联系所有者/作者。

AIware '24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas
© 2024 版权归所有者/作者所有。
ACM ISBN 979-8-4007-0685-1/24/07
https://doi.org/10.1145/3664646.3665664

## 关键词

人工智能、代码评审、编码最佳实践

## ACM 引用格式

Manushree Vijayvergiya, Małgorzata Salawa, Ivan Budiselić, Dan Zheng, Pascal Lamblin, Marko Ivanković, Juanjo Carin, Mateusz Lewko, Jovan Andonov, Goran Petrović, Daniel Tarlow, Petros Maniatis, and René Just. 2024. AI-Assisted Assessment of Coding Practices in Modern Code Review. In *Proceedings of the 1st ACM International Conference on AI-Powered Software (AIware '24)*, July 15–16, 2024, Porto de Galinhas, Brazil. ACM, New York, NY, USA, 9 pages. https://doi.org/10.1145/3664646.3665664

## 1 引言

与整体式代码评审（holistic code review）相比，现代代码评审 [21, 23] 多年来在开源与工业环境中逐步发展成型。一套常见的同行评审标准已经形成 [5, 20, 21]，其中就包含编码最佳实践。许多公司、项目乃至编程语言，都以“样式指南”（style guides）[1–4] 的形式对它们作出正式定义，通常涵盖以下几个方面：

- **格式（Formatting）**：行长度限制、空白与缩进的使用、圆括号与方括号的位置等；
- **命名（Naming）**：大小写、简洁性、描述性等；
- **文档（Documentation）**：文件级、函数级及其他注释应放置的位置与应有的内容；
- **语言特性（Language features）**：在不同（代码）上下文中使用特定语言特性的方式；
- **代码惯用法（Code idioms）**：运用代码惯用法来提升代码的清晰度、模块化程度与可维护性。

开发者普遍对现代代码评审流程表示高度满意 [23, 28]。其中一个主要收益，是让不熟悉该代码库、特定语言特性或常见代码惯用法的代码作者获得学习体验。在评审过程中，资深开发者会向代码作者讲解最佳实践，同时评审（并了解）代码贡献及其影响。

（原文页码：1）

---

# 现代代码评审中 AI 辅助的编码实践评估（续）

AIware '24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas
Manushree Vijayvergiya 等

除了评审（并了解）代码贡献及其影响之外，这也是一个学习过程。

诸如 linters 之类的静态分析工具 [15] 可以自动校验代码是否遵循某些最佳实践（例如格式规则），有些工具甚至能自动修复违规。然而，那些细微的准则、或者带有例外情形的准则，很难被完整地自动校验（例如命名约定，以及遗留代码中经过合理说明的偏离）；还有一些准则根本无法用精确规则来刻画（例如代码注释的清晰度与具体程度），它们依赖人工判断与开发者的集体知识。因此，人们普遍期望由人工评审者来检查代码变更是否存在违反最佳实践之处。

代码评审流程中最大的一项成本是时间，尤其是资深开发者投入的时间。即使已有大量自动化，且流程尽可能保持轻量，一名开发者每天也很容易为这项任务投入数小时 [23]。

机器学习的最新进展，尤其是大语言模型（LLM）所展现的能力，表明 LLM 适合用于代码评审自动化（例如 [11, 16, 17, 24–26]）。然而，围绕在规模化场景下部署端到端系统所面临的软件工程挑战仍未被充分探索。同样，对此类系统在整体效能与用户接受度方面的外部评估也仍然缺失。

本文研究的问题是：能否将代码评审流程、特别是最佳实践违规的检测，部分地自动化，从而为代码作者提供及时的反馈，并让评审者能够专注于整体功能。具体而言，本文报告了我们在工业环境中（Google）开发、部署并评估 AutoCommenter——一个自动化代码评审助手——的经验；目前，Google 每天有数万名开发者在使用它。

总结而言，本文的贡献是：

- 一个基于 LLM 的代码评审助手系统的通用架构（第 3 节）。
- 工具校准与向数万名开发者部署的描述（第 4 节）。
- 对该系统的评估（第 5 节）。
- 经验教训的总结与讨论（第 6 节）。

## 2 背景

AutoCommenter 是在 Google 的大规模工业环境中开发的。Google 的现代代码评审实践与其他工业项目及开源项目相似 [23]。

### 2.1 代码评审流程

Google 的代码评审流程成熟完备，以变更（change）为单位，并有工具辅助。Ivanković 等人 [12] 与 Petrović 等人 [18] 对该流程作了详细总结。对代码库的每一次变更，都必须至少由另一名开发者评审。每天，代码库有数万次变更走完评审流程，数万名开发者以代码作者和评审者的双重身份参与其中。

作者与评审者通过代码评审系统交换评论，评审则沿着受该变更影响的文件的各个快照（snapshot）推进。每条评审者评论都附着在某个特定文件快照中的特定行列区间上。为处理（resolve）一条评论，作者通常会在自己的本地副本中修改文件，并导出一个新的快照，进入下一轮代码评审。当作者与所有评审者都满意，且没有任何自动化分析阻塞合并时，代码就会被合并进代码库。

代码评审流程中最昂贵的部分，是代码作者与评审者“陪跑”（shepherding）一次变更所花的时间——从最初的编码，到处理评审者评论、确保所有自动化分析通过，直到最终把变更合并进代码库。尽管该流程已通过自动化系统在评审前分析代码而得到优化（尤其是无需人工介入的自动代码格式化），代码评审每年仍要耗费数千开发者年（developer-years）。因此，即便只节省个位数的百分比，也会带来显著的业务影响。

### 2.2 最佳实践

最佳实践（best practice）指被认为更优的某种具体编程语言用法；最佳实践文档则描述它应当如何应用、能带来什么好处。**最佳实践 URL** 指某份最佳实践文档或其中的具体章节；**最佳实践违规**（best practice violation）指某段未遵循某项最佳实践、但可以通过修改予以遵循的代码。若从上下文可明确判断，我们就用 URL 和 violation 分别指代最佳实践 URL 与最佳实践违规。

Google 的中央代码仓库包含多种语言的代码，其中 C++、Java、Python 和 Go 各自都超过 1 亿行 [19]。共有 15 种语言为全体开发者提供了现成的正式样式指南。其中许多语言还有额外的语言入门资料、核心库文档，以及“每周小贴士”式的简讯。这些材料虽不像样式指南那样被严格强制执行，但在代码评审中常被引用。有些语言的此类文档多达数百页。代码作者与评审者都被期望核实代码是否遵循了全部最佳实践。

十多年前引入的一项名为“readability”的正式机制，用于确保最佳实践被一致地遵循。某种语言中专职的样式专家被称为“readability 导师”（readability mentor），他们引导经验不足的开发者逐步精通该语言 [23]。readability 导师通常会用几句话概括一项最佳实践，并在评论末尾附上一个 URL 供变更作者参考。图 1 给出了一条由 readability 导师发布的评论示例。

**图 1：人工评审者发布的评论示例。**

（原文页码：2–3）

---

# 现代代码评审中 AI 辅助的编码实践评估（续）

AIware '24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas

**图 2（架构图）标注：**

- 训练与微调（按需）
- Worker / Workers
- 源仓库（Source repository）
- 评论存储（Comment storage）
- 调度器（Scheduler）
- 相关的代码评论（Relevant code comments）
- 示例（按时间切分，temporal splits）
- TPU pods
- Tensorboard
- 模型检查点（Model checkpoints）
- 输入/目标格式（Input/target format）
- 大规模预处理（周期性）
- 数据集整理（按需）

**图 2：模型训练流水线的架构。**

readability 流程存在一些缺点。对作者而言，它因额外的评审轮次而延长了开发时间。对 readability 导师而言，它可能变成一项单调且耗时的工作。它要求掌握数百条不断演变的最佳实践，包括识别并废弃过时的规则，并将它们（连同相关链接）记录在代码评审系统中。此外，它还需要持续跟踪，有时要经过多轮迭代，以确保所有违规都已得到整改。

## 3 方法

针对 2.1 节与 2.2 节所述的挑战，我们开发了 AutoCommenter——一个能自动检测最佳实践违规的代码分析工具。它旨在为代码作者提供及时的反馈，并减少对人工最佳实践评审的依赖，从而让评审者能够专注于代码功能。

### 3.1 模型与任务定义

要实现最佳实践分析的自动化，需要一个能够表示源代码、定位违规位置并识别所违反的最佳实践的模型。我们采用基于 T5 的传统 transformer 方法、使用 T5X [22]，目标是完成一种文本到文本（text-to-text）的转换。

最佳实践分析是某个多任务大序列模型（multi-task large sequence model）中的一项任务。除了 T5 标准的预训练任务——span 去噪（span denoising，即预测被遮蔽的 token）——之外，用于训练该模型的其他任务还包括：代码评审评论的处理（comment resolution）、下一次编辑预测（next edit prediction）、变量重命名，以及构建错误修复（build-error repair）[9]。训练语料包含超过 30 亿个示例，其中最佳实践分析数据集贡献约 80 万个示例。模型使用此类模型常用的标准交叉熵损失（cross-entropy loss）进行训练，并以最大化序列准确率（sequence accuracy）指标为目标进行调优，即对每个示例预测出完全正确的目标文本。

对于最佳实践分析，模型的输入是一段任务提示（task prompt）加源代码，目标是某个源代码位置以及一个指向所违反最佳实践的 URL。任务提示被格式化为一段固定文本的代码注释，使用该编程语言相应的注释风格。它以自然语言描述任务，并置于源代码之前；源代码是某个文件的直接文本表示。若输入超出模型的上下文窗口，则会被截断。位置是源代码中的一个字节偏移量（byte offset），URL 则指向被违反的最佳实践。一种领域特定语言（domain specific language）定义了目标的格式；一个特殊情况是当不存在任何违规时，目标为“空”。除目标之外，模型还会输出一个 0 到 1 之间的置信度分数（confidence score）。

请看下面这个 Go 语言的输入/目标示例：

```go
//
[†]
Task: Check language best practices.
//
// Package addition provides Add
package addition

// Return a sum
func Add(value1, value2 int) int {
    return value1 + value2
}
```

```
INSERT 153 COMMENT https://go.dev/doc/comment#func
```

输入的第一行是固定文本的任务提示，其余部分为源代码。目标给出了位置（字节偏移量 153 对应 Add 函数的起始处）以及一个 go.dev 的 URL，指向 Go 语言样式指南中该函数注释所违反的确切部分（在本例中，即注释通常应以函数名开头的惯例）。请注意，目标可能包含零个、一个或多个（并接的）位置–URL 对，具体取决于源代码中违规的数量。

### 3.2 模型训练

图 2 展示了模型训练流水线的架构，它由三部分组成。我们把数据集创建拆分为两步（预处理与整理），因为第一步要在数据量大得多的情况下运行，成本显著更高。预处理步骤的产出与模型的输入/目标表示无关。这种拆分提升了特性迭代速度（feature velocity），因为可以快速迭代示例表示及其他示例层面的调整。预处理步骤使用一个容错的调度系统，并周期性地抽取相关的代码评论，以确保新数据随时可用。

#### 3.2.1 大规模预处理

训练示例来自真实的代码评审数据，但并非所有代码评论都适合用于模型训练。因此，预处理步骤会识别**相关代码评论**（relevant code comments）——即由人撰写、且包含指向某份最佳实践文档的 URL 的评论。对每条评论，预处理步骤随后收集相应的源代码与相关元数据，包括该评论在源代码中的位置及其创建时间。该步骤的产出是一组相关代码评论，每条都带有为模型训练整理示例所需的一切数据。

（原文页码：3–4）

---

# 现代代码评审中 AI 辅助的编码实践评估（续）

AIware '24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas
Manushree Vijayvergiya 等

#### 3.2.2 数据集整理

数据集整理（dataset curation）是一个单一的、按需触发的处理步骤，以 Beam¹ 流水线实现。它依据 3.1 节所述的输入/目标格式，把每条相关代码评论转换为标准的 TensorFlow Example 数据结构。

#### 3.2.3 训练与微调

整理后的示例被直接用于模型训练与评估。我们在一个 TPU 集群上使用 T5X 框架 [22]，每 1000 步保存一次模型检查点，并使用 Tensorboard 监控训练过程。

### 3.3 模型选择

在历史数据上进行的两项内在评估（intrinsic evaluation），指导了我们选择模型检查点、置信度阈值以及解码策略。第一项是在验证集与测试集上做评估，给出按文件（per-file）统计的精确率（precision）与召回率（recall）估计。第二项是在完整的历史代码评审上做评估，给出每次代码评审中评论总数的估计，从而表明开发者与 AutoCommenter 交互的频繁程度。

#### 3.3.1 在验证集与测试集上的评估

我们按时间切分数据集，以确保模型没有在验证集与测试集中代码评论的未来代码评审快照上接受过训练。在我们的数据集中，85% 的文件恰好有一条相关代码评论，11% 有两条，4% 有三条或更多。只要预测出的代码位置与 URL 与期望值匹配（不论顺序），我们就认为该预测是正确的。

回顾一下，模型会为每个预测给出一个置信度分数，这引入了另一个参数：当某个预测的置信度分数低于某个阈值 *t* 时，该预测可被抑制。我们把 precision_t 定义为置信度分数大于 *t* 的正确预测数量，除以置信度分数大于 *t* 的全部预测数量；recall_t 的定义与之类似。这些定义使我们能够估计：作为 *t* 的函数，会有多少（不）正确的结果被展示给用户。precision_t 与 recall_t 用于训练期间比较不同的模型检查点。

尽管这种评估避免了数据泄漏，也让我们能够自动评估模型性能，但它有一个局限：虽然可以合理假定给定代码评审快照上的人工评论是正确的，但这些评论并不完备。换言之，某个代码评审快照中的代码可能依据多项最佳实践都有改进空间，而人工评审者并未对每一项都留下（带 URL 的）评论。这可能有几种原因：

- **缺少引用**：评审者可能就某个问题发表了评论，却没有附上 URL 作为参考。
- **选择性评论**：评审者可能只就某个问题评论一次，期望作者在全文范围内统一修复。
- **专长或关注点不同**：评审者可能并不熟悉所有最佳实践，或者只是在某次特定代码评审的语境下选择不对某个问题发表评论（例如只关注被改动的代码）。

尽管我们数据集中大多数文件只有一条相关评论，但基于人工检视“不正确”预测所获得的轶事性证据表明，由于上述原因，通常可能存在多条最佳实践评论。考虑到我们的基准真值（ground-truth）数据并不完备，我们所测得的精确率与召回率是含噪的。

¹ https://beam.apache.org/

因此，我们采用下一节所描述的一项补充评估，以增强对模型整体性能的信心。

#### 3.3.2 在完整历史代码评审上的评估

为了准确估计真实环境（live setting）下可能产生的评论量，我们在一个历史代码评审集合上、使用特定的模型检查点与阈值来评估 AutoCommenter。预测出的评论不会追溯性地发布到代码评审系统中，而是记录到数据库里以供分析。这使我们能够估计预期的发布频率——既可按文件粒度，也可按单次代码评审粒度。

由于开发者是对整个受代码评审约束的代码变更集合与 AutoCommenter 交互，因此在生产部署（production deployment）之前，这项评估是重要的一步。额外的好处是，这一步还允许我们做进一步优化，并评估针对不同用户群体、编程语言等的发布频率。

### 3.4 推理基础设施

AutoCommenter 的核心是一个中心化的最佳实践分析服务。该服务接收一个或多个待分析的源文件作为输入。对每个文件，它构造模型输入（3.1 节），将其编码为标准的 TensorFlow Example 数据结构，并向模型发起查询。模型本身由一个模型服务（model service）提供，该服务使用 TensorFlow 的 Example 数据结构作为与领域无关的输入输出格式。最后，最佳实践分析服务会执行一系列过滤步骤（第 4 节），抑制低质量的预测，并返回其余的预测结果。

### 3.5 IDE 与代码评审集成

开发者通过两种方式与 AutoCommenter 的分析服务交互——直接通过 IDE 插件，或间接通过代码评审系统。Google 的全体开发者都使用代码评审系统，几乎所有人都使用该 IDE。

AutoCommenter 的评论在 IDE 中显示为诊断信息（diagnostics），以蓝色波浪下划线标出相关代码片段。将鼠标悬停在下划线代码上，会显示完整评论，其中包含该最佳实践的简明摘要，以及一个指向相关最佳实践文档的可点击链接。这种嵌入式信息省去了开发者为了解不熟悉的最佳实践而在 IDE 与网页浏览器之间来回切换的需要，从而简化了工作流。由于 IDE 中的评论需要实时生成，我们力求以亚秒级（sub-second）延迟生成评论。

在代码评审系统中，AutoCommenter 会在每次更新后（即在每个新的代码评审快照上）运行，一旦检测到违规就自动发布评论。自动化工具产生的评论在外观上与人工评论相似，但背景颜色不同。

图 3 展示了 AutoCommenter 在代码评审系统中生成并发布的一条评论示例。请注意（右侧的）点赞与点踩按钮，作者与评审者若认为某条评论特别有用或特别没用，可以点击它们。另请注意（左侧的）“Please fix”按钮，它对评审者可见。一旦点击，就会生成一条新评论，表明该评审者认为这条评论很重要、必须在代码合并进代码库之前予以处理。这些反馈按钮是代码评审系统中的标准功能，出现在所有由自动化工具（例如 [7, 13]）生成的评论上，并为工具的用户接受度提供信号。IDE 也提供了类似的反馈机制。

**图 3：AutoCommenter 在代码评审系统中发布的一条评论示例。**

（原文页码：4–5）

---

# 现代代码评审中 AI 辅助的编码实践评估（续）

AIware '24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas

**图 3：AutoCommenter 发布的一条评论示例。**

## 4 部署

我们在 2022 年 7 月至 2023 年 10 月期间，分阶段把 AutoCommenter 部署给了 Google 的全体开发者：

- 直到 2022 年 7 月——吃狗粮（teamfooding）：即本文的作者们。
- 2022 年 7 月——早期采用者：约 3 千名志愿者。
- 2023 年 7 月——A/B 实验：约一半的开发者。
- 2023 年 10 月起——全面可用：全体开发者。

请注意，出于商业保密原因，我们无法披露代码评审、开发者、文件、评论的绝对数量，也无法披露代码评审时长的分布。在适当的情况下，我们报告相对指标与相关趋势。

我们持续评估并改进 AutoCommenter 的性能，采用迭代式优化的方法：

- 在历史数据上评估（3.3 节），以从方向上了解模型在该任务上的表现，并据此确定阈值、选择解码策略。
- 监控与分析用户交互，以及通过反馈按钮和问题报告提交的直接反馈。
- 基于其他评估步骤中观察到的模式，开展有针对性的**人工评估**。

图 4 展示了随时间变化的、已发布代码评审评论与 IDE 诊断信息上开发者反馈的正负比例。虚线表示开发者每月提供的反馈点击总数。如预期的那样，该数值在早期采用者阶段要低得多。此外，该阶段的波动性更高，因为我们在此期间积极优化 AutoCommenter。

回忆一下代码评审系统中的三个反馈按钮（图 3），它们让开发者可以对已发布的评论表达正面或负面情绪。我们把获得点赞或“Please fix”的评论视为正面，把获得点踩的评论视为负面；我们把**有用率**（useful ratio）定义为正面评论数占所有有反馈评论数的比例。

本节其余部分描述部署期间我们做出的具体观察及相应的优化。

**图 4：整个部署期间的开发者反馈。**

### 4.1 选择阈值与解码策略

#### 4.1.1 阈值

在初始部署阶段，我们希望谨慎管理开发者对 AutoCommenter 的信任，因此从较高的置信度阈值 *t* = 0.98 开始。我们人工抽样了数百条结果，观察到阈值以下的预测中约 80% 仍然是正确的——也就是说，在 *t* = 0.98 时假阴性率非常高。此外，我们观察到 Python 的预测呈现出显著不同的置信度分数分布，受阈值处理的影响不成比例。我们推测，训练数据集的构成（不同 URL 的数量及 URL 出现频率）以及最佳实践文档的颗粒度是原因所在，但把更深入的调查留待未来工作。尝试按语言设置阈值被证明无效：因为每种语言仅用一个阈值，仍无法充分刻画模型正确预测数百条多样化最佳实践的能力。这导致所预测 URL 的多样性不足，因为无论正确与否，模型倾向于对某些 URL 给出比另一些更高的分数。这些观察促成了对 AutoCommenter 的第一次重大改动：基于验证数据集上的内在评估，计算**按 URL 区分的阈值**（per-URL thresholds）。

#### 4.1.2 解码

在完整的历史代码评审上，使用按 URL 区分的阈值与贪婪解码（greedy decoding）进行评估，结果显示 AutoCommenter 能在 6% 的已变更文件中检测出违规。然而，其中 80% 的评论会发布在作者并未修改的代码行上。开发者通常不会对未改动的代码采取行动。因此，AutoCommenter 会过滤掉生成于未变更代码行上的评论，把已变更文件中的评论比例降至 1.3%。为了提高这一比例，我们尝试了不同的解码策略：贪婪（默认）、束搜索（beam search）、top-k 采样与 top-p 采样。我们最终选择束搜索（生成 *k* = 4 个候选回答），它把发布频率提高到三倍，达到 3.9%。它还带来了高得多的 URL 多样性：发布最频繁的 10 个 URL 占全部评论的 41%，而贪婪搜索下这一比例为 80%。

在为部署选择解码策略时，延迟是另一个重要方面。虽然束搜索提高了发布频率与多样性，但推理变得明显更慢（中位延迟 2 秒）。鉴于该延迟对于 IDE 中的交互式使用而言过高，我们最终决定：在代码评审系统中使用束搜索，在 IDE 中使用贪婪搜索。

（原文页码：5–6）

---

# 现代代码评审中 AI 辅助的编码实践评估（续）

AIware '24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas
Manushree Vijayvergiya 等

### 4.2 抑制过时的最佳实践

在把 AutoCommenter 发布给约 3 千名自愿的早期采用者之后，我们注意到用户们在几天内提交了大量问题。其中许多都对应同一个 URL²，该 URL 描述的是与 Python import 相关的最佳实践。然而，在 Python 3.9 中某些类型名称的规范来源已经改变，该最佳实践也在 2022 年初发生了变化。由于我们的训练数据延伸至 2022 年之前，其中包含了一批已不再适用的最佳实践评论。我们意识到这是一个反复出现的模式：随着语言的演进，或新库的引入，最佳实践也会随之演进。缓解该问题的一种方式是在规则发生变化时，把这类数据过滤掉，并重新训练模型。但这既耗时间又耗资源：它需要完整的数据重新生成、模型训练、评估与上线。与此同时，那个“过时”的模型要么必须被关掉（导致系统停机），要么受影响的预测必须被抑制。否则，系统可能会很快失去开发者的信任。我们选择使用条件过滤（对源代码匹配正则表达式）来抑制特定最佳实践的预测，原因有两点。第一，它可以被动态部署并立即生效。第二，它允许对预测做细粒度的过滤。

² https://github.com/google/styleguide/blob/gh-pages/pyguide.md#22-imports

### 4.3 对选定评论的独立评分

在早期使用几个月后，我们观察到有用率停滞在约 54%。为了理解其中原因、找出改进空间并为更大范围的部署做准备，我们在 2023 年 4 月开展了一项独立的人工评分研究，分析了约 370 条在“早期采用者”部署阶段获得了开发者反馈的已发布评论样本。

为了获得关于评论有用性的多元视角，我们招募了 15 名评分者——来自合作团队的开发者。我们请他们对获得明确用户反馈的 AutoCommenter 评论进行评分。我们没有向评分者展示原始的用户反馈，以避免使其评估产生偏差。评分者依据所链接的最佳实践及周边代码，评估每条评论的有用性。我们要求他们重点关注评论的正确性，但也关注该评论作为作者对他们而言是否可操作（例如，一条技术上正确、但在具体场景下似乎不值得处理的评论，他们是否会去处理）。我们鼓励他们对每条评论提供自由形式的反馈。

评分者评估得到的有用率为 60%，略高于同一批评论上开发者反馈的 54%，但远低于我们为更大范围部署设定的 80% 目标。这项研究最有趣的发现是：无用评论存在清晰的模式。以下是一些例子：

- **主题过多或主题复杂**：例如，某个 URL 指向一节内容，其中描述了与 Python linter 交互的多条准则，包括它经常触发的场景以及抑制它的方法。作者可能难以理解所发布的评论究竟指向哪条具体准则，以及如何解决。类似地，关于在 C++ 中编写优秀函数文档的指导是一整页密集的文字。评分者经常指出，最佳实践（以及 AutoCommenter 的简短摘要）与实际代码之间存在脱节，即使代码中确实包含相关违规。
- **高质量摘要的重要性**：评分者常常发现，AutoCommenter 的摘要（通过抓取文档源生成，有时会缺失）未能充分说明所引用准则与该评论/代码之间的关联。
- **主观且可能存在争议的主题**：一个例子是避免在库代码中使用 flag。flag 用在库中可能引发问题，但有些库正是被设计为通过 flag 配置大量特性的。此外，遗留代码可能并不遵循这条准则，评审者也不会强制执行它。模型没有学到这些细微差别，有时会在作者为既有库新增一个 flag 时预测出违规。
- **某些准则上的系统性模型错误**：一个有趣的例子是某条准则提倡：对 C++ vector，当 `push_back` 与 `emplace_back` 两者可用相同实参达到相同效果时，优先使用成员函数 `push_back`。模型学会了预测这一条，但它也会在本应使用 `emplace_back` 的场景下预测它，甚至当某个不相关的类型有一个名为 `push_back` 的成员函数时也会预测。
- **正确但价值低的评论**：代码注释中句子末尾缺少句点，通常会被人工评审者放过。虽然技术上正确，但要求作者回到 IDE 去修复该问题，可能带来净负面价值。

评分者研究的洞见促成了对 AutoCommenter 的两项改动。第一，该研究识别出 17 个不可操作的 URL，抑制它们后，历史有用率在开发者反馈上从 54% 提升到 66%，在评分者反馈上从 60% 提升到 74%。我们进一步分析了与相似的、未被评分的 URL 相关联的评论，又抑制了额外的 5 个。第二，我们审查并人工更新了所有高频发布 URL 的摘要。这些改动合在一起，足以达到我们为下一阶段部署设定的 80% 目标有用率。

### 4.4 A/B 实验

2023 年 7 月，我们在一次 A/B 实验中把 AutoCommenter 部署给了约一半的开发者。我们把开发者随机分配到实验组（启用 AutoCommenter）与对照组（禁用 AutoCommenter）。我们依据开发者邮箱地址 SHA256 哈希值的最后几位进行随机化，并核实两组在规模与构成上没有差异，包括任职时长、资历、编程语言与业务单元的分布。我们还确认，在实验开始之前，实验中测量的各项变量在对照组与实验组之间均无差异。实验期间的评论发布频率符合预期（4.1 节）。

在以下任何一项上，我们都没有检测到统计上显著的变化：代码评审的总时长、开发者主动花费在代码评审上的时间、作者与评审者之间的评论–回应迭代次数。不过，我们确实检测到编码速度有轻微提升。我们推测，跳转到文档的上下文切换减少带来了这一正向效果。更深入的调查留待未来工作。基于这些结果，我们得出结论：不存在不利影响，并于 2023 年 10 月把 AutoCommenter 部署给了全体开发者。

（原文页码：6–7）

---

# 现代代码评审中 AI 辅助的编码实践评估（续）

AIware '24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas

**图 5：AutoCommenter 在生产环境中生成的自动评论与训练数据中人工评论的「每个 URL 的评论数」累积分布对比。**

## 5 评估

基于自 2023 年 3 月以来收集的有用率与用户反馈，我们得出结论：开发者总体上对 AutoCommenter 产出的评论是满意的。我们通过分析用户反馈，持续改进数据集整理、阈值、URL 抑制与摘要生成，以确保 AutoCommenter 对开发者工作流产生高度的正向影响。

除了开发者满意度之外，在全量发布给整个 Google 数月之后，我们还评估了 AutoCommenter 表现的另外三个方面：

1. **评论被解决情况**：开发者有多频繁地修改代码来解决 AutoCommenter 发布的评论？
2. **AutoCommenter 与人工评论的对比**：AutoCommenter 的评论在多大程度上覆盖了人工评审者在其评论中引用的最佳实践文档？
3. **AutoCommenter 与 linter 的对比**：AutoCommenter 的产出在多大程度上超越了传统静态分析工具的能力？

### 5.1 评论被解决情况

开发者很少通过点击代码评审系统和 IDE 中的「赞／踩」按钮、以及代码评审系统中的「Please fix」按钮来对 AutoCommenter 的评论给出显式反馈（图 3）：代码评审系统中约 10% 的自动评论、IDE 中约 2% 的诊断收到了显式反馈，这一比例与 Google 其他自动化分析相当。与此同时，开发者对 AutoCommenter 约 50% 的 IDE 诊断会悬停查看，而既有研究表明，开发者经常在未给出显式反馈的情况下就解决了自动评论 [18]。为了评估开发者实际解决 AutoCommenter 评论的频率，我们开展了一项离线分析，估算评论被后续代码变更解决的比例。

为分析评论被解决情况，我们提取了包含 AutoCommenter 自动评论的文件上的历史变更。对每个变更，我们提取评论发布时的初始快照，以及开发者最终合并进代码库的快照。每条评论覆盖特定的行范围。我们在两个快照之间使用一种基于 AST 的自动化行映射方法 [18]，以识别那些模型最初在第一个快照上预测出、但在合并后的快照上不再预测的评论。这样的快照对表明该评论可能已被解决，但也存在另一种可能：不相关的代码变更导致模型不再预测出某条特定评论。

对 6000 对快照的自动化分析显示，在 50% 的情况下，该评论在其最初发布的那些行上已从提交的快照中消失。我们又人工抽查了其中 40 对随机样本，发现在 80% 的情况下，作者所做的某处变更直接解决了该评论所描述的问题。因此，我们估算评论被解决率约为 40%，显著高于「获得显式正面反馈的评论占全部评论的比例」。

**图 6：出现频率最高的 top-50 URL 按类型分类。Linter 一列表示是否存在（或能否容易地构建出）能检测相应违规的 linter。**

### 5.2 AutoCommenter 与人工评论的对比

图 5 比较了 AutoCommenter 在生产环境中生成的自动评论与训练数据中人工评论的「每个最佳实践文档 URL 对应评论数」累积分布。横轴是把所有在自动评论中出现过的 URL 按频率排序后的排名。例如，使用最频繁的 URL 排名第 1，它占全部自动评论的 9.9%；而同一个 URL 在训练数据的人工评论中仅占 4.3%。AutoCommenter 总共为 330 个不同 URL 生成过评论。AutoCommenter 使用的 URL 集合覆盖了 68% 带有最佳实践 URL 的历史人工评论。这是一个不错的结果：它表明 AutoCommenter 并没有把注意力放在评审者极少引用的冷门最佳实践上。

另一方面，尽管使用了 beam search，URL 多样性仍然相对偏低：top-85 个 URL 构成了 AutoCommenter 所生成评论的 90%，而同样这组 URL 只覆盖了带最佳实践 URL 的人工评论的 35%。在保持准确率与低延迟的同时，提升自动评论中 URL 的多样性与对最佳实践的覆盖率，是我们的首要任务之一。

### 5.3 AutoCommenter 与 linter 的对比

为理解 AutoCommenter 在那些能被 linter 高效且精确检查的最佳实践之外还能带来多大价值，我们抽样了出现频率最高的 top-50 违规——即图 5 中排名最前的 50 个 URL。对每个抽样 URL，我们查阅其最佳实践文档，并判定：(1) 该最佳实践的**类型**（第 1 节）；(2) 是否存在（或能否容易地构建出）能检测相应违规的 linter。

（原文页码：7–8）

---

# 现代代码评审中 AI 辅助的编码实践评估（续）

AIware '24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas
Manushree Vijayvergiya 等

（接 5.3 节）具体而言，三位作者——每人都有超过 10 年构建静态分析工具的经验——分别阅读文档并独立地对这些 URL 进行分类。在最佳实践**类型**上没有任何分歧，但对于约 15% 的 URL，在「能否容易地为其构建 linter」这一点上存在分歧。三位作者通过多数投票与讨论解决了这些分歧。分歧源自最佳实践本身含义模糊，以及某些最佳实践包含多条准则。例如，检查代码中是否存在文档相对直接，但要判断例外情形是否正当、内容是否清晰，可能就不那么简单了。

图 6 展示了这 50 个抽样 URL 的分布，按类型以及「违规是否能被 linter 检测」拆分。对这些最佳实践中的 33/50（66%）而言，违规检测已超出传统静态分析的能力范围。

## 6 经验教训

基于我们开发和部署 AutoCommenter 的经验，我们总结出若干关键经验教训：

- **对传统分析的补充**：AutoCommenter 基于 LLM 的方法能够为人工评审者频繁引用的 68% 的最佳实践生成评论，其中许多都超出了传统静态分析的能力范围。
- **内在评估与现实世界表现**：内在评估与现实世界表现可能差异巨大。我们的内在评估使用真实人工评论构成的数据集，配合当时最先进的模型架构与训练流程，指向了一个前景良好的模型；但事实证明，外在实际评估与系统改进对成功上线至关重要。
- **监控用户接受度至关重要**：哪怕只有少数负面用户体验，也会侵蚀用户对自动化系统的信任。持续监控并分析真实世界反馈，对于发现这类情况并找到补救办法至关重要。就 AutoCommenter 而言，一个简单的抑制机制就足以把用户接受度大幅提升至 80% 以上，而无需在效果上做出重大牺牲。

## 7 相关工作

Johnson [15] 在近 50 年前的 1977 年提出了 C linter。在这 50 年间，围绕自动化静态分析产生了大量研究：Heckman 与 Williams [10] 近期的一篇文献综述识别出 17,571 篇论文。许多研究探讨开发者如何与静态分析交互。Johnson 等人 [14] 探讨了开发者在尝试使用静态分析时面临的挑战，其结果凸显了与既有开发者工作流良好集成的重要性，以及建立并维护对工具之信任的重要性。Vassallo 等人 [27] 探讨了开发者在不同情境（包括编码与代码评审）下如何与静态分析交互，他们同样发现，融入既有工作流对开发者使用这些工具的意愿影响重大，且结果的高质量极为重要。Beller 等人 [6] 研究了大量开源项目中静态代码分析的使用情况，在诸多发现中他们强调：自动化分析实际如何被使用、以及应当如何使用，会因编程语言而异。

相比之下，使用机器学习进行代码分析是一个相对较新、理解尚不充分的领域。近期若干公开文献（例如 Hong 等人 [11]、Li 等人 [16]、Li 等人 [17]、Thongtanunam 等人 [24]、Tufano 等人 [25]，以及 Tufano 等人 [26]）报告了模型评估并提出面向自动化代码评审的工具。尽管这些模型与评审评论生成任务同本文提出的模型非常相似，但其评估大多聚焦于历史数据集。如 3.3.1 节所讨论，仅基于历史评论的内在评估有一定局限，有时无法预测真实世界的表现。Frömmgen 等人 [9] 近期的另一篇文献给出了对在线系统的评估，但针对的是相反的任务：从评论生成代码，而非从代码生成评论。

## 8 结论

验证代码是否遵循最佳实践，是现代代码评审流程中的常见任务。有些最佳实践可以用 linter 等传统工具自动校验，但许多最佳实践需要经验丰富的开发者运用知识与判断力，这需要投入时间与精力。

本文报告了我们开发、部署并评估 AutoCommenter 这一基于 LLM 的代码评审助手系统的经验。具体而言，它完整呈现了从任务与模型设计，到内在评估与系统校准，再到分阶段上线与最终用户评估的全过程。

评估结果表明，构建一个能力远超传统工具的端到端系统、同时获得高度的最终用户接受度，是可行的。这些结果是为部署更复杂的代码评审助手与自动化代码评审迈出的、前景良好的第一步。

我们的首要目标是确保良好的开发者体验，因此把 AutoCommenter 设计为具有极高的精确率。虽然召回率并非主要关注点，但我们认识到它的重要性，并计划探索模型与系统架构上的哪些改动可以提升召回率。例如，我们在 2022 年使用的模型在当时是最先进的，但它的上下文窗口只有 2048 个 token，仅足以容纳约 200 行代码。当前最先进的模型在训练时上下文窗口达数万 token，推理时超过一百万 token。这一跃升为新增功能以及现有功能的显著改进打开了空间。

## 9 致谢

本工作是 Google Core Systems 与 Google DeepMind 各团队多年协作的成果。我们感谢所有团队成员与领导层的支持与建议，包括 Alberto Elizondo、Alexander Frömmgen、Ballie Sandhu、Chandu Thekkath、Chris Gorgolewski、David Tattersall、Ilya Cherny、Jacob Austin、Katja Grünwedel、Kristóf Molnár、Lera Kharatyan、Luka Rimanić、Madhura Dudhgaonkar、Marc Brockschmidt、Marcus Revaj、Maxim Tabachnyk、Nina Chen、Niranjan Tulpule、Nitya Ramani、Paige Bailey、Pavel Sychev、Pierre-Antoine Manzagol、Quinn Madison、Roger Fleig、Satish Chandra、Savinee Dancs、Stoyan Nikolov、Subhodeep Moitra 以及 Vaibhav Tulsyan。

（原文页码：8–9）

---

# 现代代码评审中 AI 辅助的编码实践评估（续）

AIware '24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas

## 参考文献

[1] 2024. Google Style Guides. https://google.github.io/styleguide/. 访问日期：2024-03-15.
[2] 2024. Linux kernel coding style. https://www.kernel.org/doc/html/v4.10/process/coding-style.html. 访问日期：2024-03-15.
[3] 2024. PEP 8 — Style Guide for Python Code. https://peps.python.org/pep-0008/. 访问日期：2024-03-15.
[4] 2024. Rust Style Guide. https://doc.rust-lang.org/nightly/style-guide/. 访问日期：2024-03-15.
[5] Alberto Bacchelli and Christian Bird. 2013. Expectations, outcomes, and challenges of modern code review. In 2013 35th International Conference on Software Engineering (ICSE). 712–721. https://doi.org/10.1109/ICSE.2013.6606617
[6] Moritz Beller, Radjino Bholanath, Shane McIntosh, and Andy Zaidman. 2016. Analyzing the state of static analysis: A large-scale evaluation in open source software. In 2016 IEEE 23rd International Conference on Software Analysis, Evolution, and Reengineering (SANER), Vol. 1. IEEE, 470–481.
[7] Zimin Chen, Małgorzata Salawa, Manushree Vijayvergiya, Goran Petrović, Marko Ivanković, and René Just. 2023. MuRS: Mutant Ranking and Suppression using Identifier Templates. In Proceedings of the Symposium on the Foundations of Software Engineering (FSE). 1798–1808.
[8] M. E. Fagan. 1976. Design and code inspections to reduce errors in program development. IBM Systems Journal 15, 3 (1976), 182–211. https://doi.org/10.1147/sj.153.0182
[9] Alexander Frömmgen, Jacob Austin, Peter Choy, Nimesh Ghelani, Lera Kharatyan, Gabriela Surita, Elena Khrapko, Pascal Lamblin, Pierre-Antoine Manzagol, Marcus Revaj, Maxim Tabachnyk, Daniel Tarlow, Kevin Villela, Daniel Zheng, Satish Chandra, and Petros Maniatis. 2024. Resolving Code Review Comments with Machine Learning. In International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP).
[10] Sarah Heckman and Laurie Williams. 2011. A systematic literature review of actionable alert identification techniques for automated static code analysis. Information and Software Technology 53, 4 (2011), 363–387. https://doi.org/10.1016/j.infsof.2010.12.007 Special section: Software Engineering track of the 24th Annual Symposium on Applied Computing.
[11] Yang Hong, Chakkrit Tantithamthavorn, Patanamon Thongtanunam, and Aldeida Aleti. 2022. Commentfinder: a simpler, faster, more accurate code review comments recommendation. In Proceedings of the Joint Meeting of the European Software Engineering Conference and the Symposium on the Foundations of Software Engineering (ESEC/FSE). 507–519.
[12] Marko Ivanković, Goran Petrović, René Just, and Gordon Fraser. 2019. Code Coverage at Google. In Proceedings of the Joint Meeting of the European Software Engineering Conference and the Symposium on the Foundations of Software Engineering (ESEC/FSE). 955–963.
[13] Marko Ivanković, Goran Petrović, Yana Kulizhskaya, Mateusz Lewko, Luka Kalinovčić, René Just, and Gordon Fraser. 2024. Productive Coverage: Improving the Actionability of Code Coverage. In International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP).
[14] Brittany Johnson, Yoonki Song, Emerson Murphy-Hill, and Robert Bowdidge. 2013. Why don't software developers use static analysis tools to find bugs?. In 2013 35th International Conference on Software Engineering (ICSE). IEEE, 672–681.
[15] Stephen C Johnson. 1977. Lint, a C program checker. Bell Telephone Laboratories Murray Hill.
[16] Lingwei Li, Li Yang, Huaxi Jiang, Jun Yan, Tiejian Luo, Zihan Hua, Geng Liang, and Chun Zuo. 2022. Auger: Automatically generating review comments with pre-training models. In Proceedings of the Joint Meeting of the European Software Engineering Conference and the Symposium on the Foundations of Software Engineering (ESEC/FSE). 1009–1021.
[17] Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green, Alexey Svyatkovskiy, Shengyu Fu, and Neel Sundaresan. 2022. Automating code review activities by large-scale pre-training. In Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE 2022). Association for Computing Machinery, New York, NY, USA, 1035–1047. https://doi.org/10.1145/3540250.3549081
[18] Goran Petrović, Marko Ivanković, Gordon Fraser, and René Just. 2023. Please fix this mutant: How do developers resolve mutants surfaced during code review?. In International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP). 150–161.
[19] Rachel Potvin and Josh Levenberg. 2016. Why Google Stores Billions of Lines of Code in a Single Repository. Communications of the ACM (CACM) 59 (2016), 78–87. http://dl.acm.org/citation.cfm?id=2854146
[20] Peter Rigby, Brendan Cleary, Frederic Painchaud, Margaret-Anne Storey, and Daniel German. 2012. Contemporary Peer Review in Action: Lessons from Open Source Development. IEEE Software 29, 6 (2012), 56–61. https://doi.org/10.1109/MS.2012.24
[21] Peter C. Rigby and Christian Bird. 2013. Convergent contemporary software peer review practices. In Proceedings of the 2013 9th Joint Meeting on Foundations of Software Engineering (ESEC/FSE 2013). Association for Computing Machinery, New York, NY, USA, 202–212. https://doi.org/10.1145/2491411.2491444
[22] Adam Roberts, Hyung Won Chung, Gaurav Mishra, Anselm Levskaya, James Bradbury, Daniel Andor, Sharan Narang, Brian Lester, Colin Gaffney, Afroz Mohiuddin, et al. 2023. Scaling up models and data with t5x and seqio. Journal of Machine Learning Research 24, 377 (2023), 1–7.
[23] Caitlin Sadowski, Emma Söderberg, Luke Church, Michal Sipko, and Alberto Bacchelli. 2018. Modern Code Review: A Case Study at Google. In International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP). 181–190.
[24] Patanamon Thongtanunam, Chanathip Pornprasit, and Chakkrit Tantithamthavorn. 2022. Autotransform: Automated code transformation to support modern code review process. In Proceedings of the International Conference on Software Engineering (ICSE). 237–248.
[25] Rosalia Tufano, Ozren Dabić, Antonio Mastropaolo, Matteo Ciniselli, and Gabriele Bavota. 2024. Code Review Automation: Strengths and Weaknesses of the State of the Art. IEEE Transactions on Software Engineering (TSE) (2024).
[26] Rosalia Tufano, Simone Masiero, Antonio Mastropaolo, Luca Pascarella, Denys Poshyvanyk, and Gabriele Bavota. 2022. Using pre-trained models to boost code review automation. In Proceedings of the International Conference on Software Engineering (ICSE). 2291–2302.
[27] Carmine Vassallo, Sebastiano Panichella, Fabio Palomba, Sebastian Proksch, Harald C Gall, and Andy Zaidman. 2020. How developers engage with static analysis tools in different contexts. Empirical Software Engineering 25 (2020), 1419–1457.
[28] T. Winters, T. Manshreck, and H. Wright. 2020. Software Engineering at Google: Lessons Learned from Programming Over Time. O'Reilly Media. https://books.google.ch/books?id=TyIrywEACAAJ

收稿日期 2024-04-05；录用日期 2024-05-04

（原文页码：9）
