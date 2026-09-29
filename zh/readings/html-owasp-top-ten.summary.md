# OWASP 十大 Web 应用安全风险（导读）

> 来源：OWASP Foundation · 文章 id：`html-owasp-top-ten` · 原文约 16.4K 字符

## 核心主张
本文是 OWASP（Open Web Application Security Project）维护的「OWASP Top Ten」官方说明页，面向开发者与安全从业者，回答「当前最严重的 Web 应用安全风险是什么、应优先修哪些」。它强调这份榜单不是厂商营销，而是由全球社区基于真实数据与共识（consensus）评选出的十大关键风险，是开始编写安全代码（secure coding）的第一步。页面同时说明了 2025 版本的数据分析方法与全球翻译协作机制。

## 关键要点（原文引用）
- 当前已发布的最新版本为 `OWASP Top Ten 2025`，历史版本可在 `OWASP Top Ten 2021` 与 `OWASP Top Ten 2017` 查阅。
- 该文档定位为「awareness document」（意识/认知文档），列出的是共识认定的十大最关键 Web 应用安全风险，而非穷尽式清单。
- 数据来源涵盖多种渠道：security vendors、consultancies、bug bounties，以及公司/组织的贡献（company/organizational contributions），并会做归一化处理后进行等级排序。
- 数据入口与原始数据仓库：`https://bit.ly/OWASPTop10Data` 与 `https://github.com/OWASP/Top10/tree/master/2025/Data`。
- 贡献数据的截止时间为 `July 31, 2025`，覆盖 `2021` 至 `2024` 期间的数据。
- 提交数据所需的最小字段包括：统计周期（period）、被测应用总数（total apps tested）、CWE 列表与每个 CWE 的计数。
- 一个关键统计口径：incidence（出现率）定义为「包含某 CWE 的应用数 / 被测应用总数」，而非该缺陷在代码中出现的频率。
- 2021 版本已完成多语言翻译，包括 `ar`、`es`、`fr`、`id`、`it`、`ja`、`pt_BR`、`zh_CN`、`zh_TW`；2025 版本页面标注 `Top10:2025 Completed Translations:` 与 `Translations in progress - check back soon!`。
- 项目由多位负责人协作维护，页面列出的 leaders 包含 `Andrew van der Stock`、`Brian Glas`、`Neil Smithline`、`Tanya Janca`、`Torsten Gigler`。
- 历史版本赞助方变更：2021 为 `Secure Code Warrior`，2017 为 `Autodesk`（OWASP NoVA Chapter），2003–2013 为 `Aspect Security`。
- 数据提交需提供元数据与 CWE 映射（metadata/CWE schema），并可区分已验证场景与伪匿名（pseudo-anonymous）贡献。
- 针对入选的前 20–30 个 CWE，会使用 CWSS base scores 进行评分。

## 术语与译法
- `OWASP Top Ten` → OWASP 十大安全风险
- `Vulnerability` → 漏洞
- `Injection` → 注入
- `Static Analysis` → 静态分析
- `SAST` → 静态应用安全测试（SAST）
- `DAST` → 动态应用安全测试（DAST）
- `Supply Chain Attack` → 供应链攻击

## 结论
OWASP Top Ten 是一份社区共识驱动、以真实数据为支撑的 Web 安全风险清单；2025 版本延续了数据征集、归一化排序与全球多语言协作的模式，适合作为安全编码与风险优先级的起点。
