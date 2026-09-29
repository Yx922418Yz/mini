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
