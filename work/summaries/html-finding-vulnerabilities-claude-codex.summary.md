# 用 Claude Code 与 Codex 寻找漏洞（导读）

> 来源：Semgrep · 文章 id：`html-finding-vulnerabilities-claude-codex` · 原文约 22.8K 字符

## 核心主张
Semgrep 通过实验评估 AI 编码智能体（Coding Agent）在真实代码中寻找漏洞的有效性。结论是：仅用相对简单的安全聚焦提示词（Prompt），AI 编码智能体已能在真实应用中找出真实漏洞，但结果噪声很大（高误报率），且高度不确定（non-deterministic）。因此细致的评估（Evaluation）与基准测试（Benchmark）是判断某方法是否真正有效的关键。这是该系列的第一篇文章。

## 关键要点（原文引用）
- 实验对象：Anthropic 的 Claude Code（v1.0.32, Sonnet 4）与 OpenAI Codex（v0.2.0, o4-mini），任务是在 11 个流行且大型的开源 Python Web 应用中寻找漏洞，共产生 400+ 条安全发现，由安全研究团队人工复核。
- Claude Code 找到 46 个漏洞（14% true positive rate – TPR，86% false positive rate – FPR）；Codex 报告 21 个漏洞（18% TPR，82% FPR）；其中约 20 个为高危漏洞（high severity）。
- Claude Code 最擅长 Insecure Direct Object Reference (IDOR)，达 22% TPR（13/59）；但在跨多个文件与函数做 taint tracking 时很吃力，SQL Injection 仅 5% TPR（2/38），XSS 仅 16% TPR（12/74）。
- Codex 的 IDOR 为 0% TPR（0/5）、SQL Injection 为 0% TPR（0/5）、XSS 为 0% TPR（0/28），却在 Path Traversal 上意外优于 Claude Code，达 47% TPR（8/17）。
- 非确定性是真问题：在同一代码库上运行完全相同的提示词，结果经常差异巨大；在某个应用中，三次完全相同的运行分别产生 3、6、11 个不同的发现。
- 基准测试现实性不足：许多 SAST 基准只用带已知漏洞的开源应用（如 WebGoat、JuiceShop、OWASP Benchmark），而当前 LLM 很可能已「看过」这些仓库代码与公开 write-ups，从而让结果失真。
- 在传统注入类漏洞（SQL injection、XSS、SSRF）上，误报尤其多。
- 针对注入类漏洞，文章关心 LLM 能否追踪从 source（如用户提供的值）到 sink（如消费原始 SQL 的方法）的数据流，能否跨函数与文件追踪，能否理解 sanitization 与第三方开源依赖中的函数。
- 文章讨论了 Anthropic 的 `/security-review` 命令「pretty mid」，并列出一组关于 AI 漏洞挖掘的开放研究问题（误报/漏报率、常见误报原因、是否确定性等）。
- 附有用于调用智能体的简单安全提示词模板，包含 `<SARIF_OUTPUT>...</SARIF_OUTPUT>` 标签与 `{vuln_type}` 占位符。
- 文章最后编辑于 Sept 3, 2025。

## 术语与译法
- `Coding Agent` → 编码智能体
- `Vulnerability` → 漏洞
- `SAST` → 静态应用安全测试（SAST）
- `Injection` → 注入
- `Deterministic` → 确定性的
- `Benchmark` → 基准测试
- `Evaluation` → 评估
- `LLM` → 大语言模型
- `Prompt` → 提示词

## 结论
AI 编码智能体已能发现真实漏洞，但目前误报率高、结果不确定，尤其在需要跨文件追踪数据流的注入类漏洞上表现薄弱；要判断某方案是否有效，必须做细致的评估与基准测试，而非依赖失真的传统 SAST 基准。
