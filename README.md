# C1 课程资料获取与翻译 · 交付说明

把 CS146S（斯坦福《AI 辅助软件工程》课程）离线资料包中的英文讲义与阅读页，翻译/导读为中文，并给出一条**可复跑**的翻译流水线。

> 挑战：`C1 课程资料获取与翻译` ｜ 难度：入门 ｜ 截止：2026-12-31 23:59

## 1. 交付物清单

| 文件 | 作用 |
|---|---|
| `README.md` | 本文件：结构、复跑方法、覆盖率、已知缺口 |
| `AI日志.md` | 与 AI 协作的完整过程日志（阶段、提示词、产出、踩坑） |
| `AAR.md` | 七维课后复盘（学到什么 / 流程 / 协作 / 完成 / 卡点 / 改进 / ΔR） |
| `拿来说明.md` | ≥3 组「原文 → 提示词 → AI 产出 → 人工修正」对照证据 |

## 2. 目录结构

```
C1_课程翻译/
├─ README.md  AI日志.md  AAR.md  拿来说明.md   ← 交付物
├─ source/CS146S_offline/                 ← 原始资料（只读输入）
│   ├─ pdfs/        3 份英文讲义 PDF（ai-assisted-code-review-assessment / how-anthropic-uses-claude-code / how-openai-uses-codex）
│   ├─ pages/       HTML 阅读页（约 30 篇）
│   ├─ site/        课程主站快照 index.html
│   ├─ assets/  slides_info/
│   ├─ all_urls.txt（105 行）  page_map.json（29 条）
├─ pipeline/                              ← 可复跑流水线（见 §4）
├─ work/                                  ← 中间产物（extracted / chunks / out / summaries / coverage_report.json）
└─ zh/                                    ← 中文成果
    ├─ index.md                          总目录
    ├─ lectures/   3 份讲义全文中译
    ├─ readings/   30 篇阅读页中文导读
    └─ site/       主站部分译稿
```

## 3. 成果概览

- **讲义全文中译 3 / 3，覆盖率 100%**（约 13.9 万原文字符 → 22 个翻译分块）
- **阅读页中文导读 30 篇**（HTML 页以「逐段导读」形式交付，非全文硬译）
- **主站译稿 1 篇（部分）**
- **术语表 70 条**，译文中命中 62 条（要求 ≥50 条）
- 全部成果汇总于 `zh/index.md`，覆盖率明细见 `work/coverage_report.json`

```text
来源统计：full=3（讲义全文） summary=30（导读） partial=1（主站）
lectures_coverage = 1.0003   overall_coverage = 0.2382
glossary_terms = 67（报告口径） / 70（术语表条目）
```

## 4. 翻译流水线（复跑方法）

在 `C1_课程翻译/` 目录下：

```powershell
python pipeline\extract.py     # ① 抽取：PDF/HTML → work\extracted\*.json + *.txt（含 HTML 清洗）
python pipeline\chunk.py       # ② 分块：上限 9000 字 → work\chunks\<id>.src.txt / .prompt.md / _chunks.json
python pipeline\translate.py   # ③ 翻译：逐块产出中文 → work\out\
python pipeline\assemble.py    # ④ 装配：合并译文 / 生成导读，写 zh\ 与 work\coverage_report.json
python pipeline\verify.py      # ⑤ 校验：覆盖率与术语命中 → work\coverage_report.json
python pipeline\status.py      # ⑥ 进度：按来源统计完成情况
# 或一键：
powershell -File pipeline\run_all.ps1
```

| 脚本 | 职责 |
|---|---|
| `extract.py` | 抽取 PDF/HTML 正文；`strip_html()` 清洗导航/脚本噪音 |
| `chunk.py` | 按 `max-chars=9000` 分块，生成翻译提示词骨架 |
| `translate.py` | 逐块翻译驱动（本机 CLI 不可用时，译文由指挥官逐块直写并回填） |
| `assemble.py` | 合并为全文；未全译来源自动生成导读；输出 `zh/index.md` |
| `verify.py` | 计算讲义/整体覆盖率、术语命中数 |
| `glossary.json` | 术语表（v1，CS146S Stanford Fall 2025，70 条） |
| `run_all.ps1` | 顺序执行以上全部 |

**翻译规范（写入提示词）**：① 忠实、通顺、术语一致，保留 Markdown 结构；② 代码 / 命令行 / 文件名 / API / 产品名 / URL 保留原文；③ 严格遵循术语表，未收录专业词首次出现写「中文（English）」；④ 只输出译文。

## 5. 已知缺口与处理方式（透明声明）

| 来源 | 情况 | 处理 |
|---|---|---|
| `lessons-from-ai-code-reviews.html` | 原页抓取为 0 字节，离线无法取正文 | 记录为缺口，未编造内容 |
| how-warp-uses-warp / good-context-good-code / peeking-under-the-hood-of-claude-code | 目标站点（Notion / Ghost / Medium）设访问门，离线仅存占位 | 产出「访问受限」说明式导读 |
| `zh/site/` 主站 | 仅部分段落完成译稿（partial=1） | 已在 `index.md` 标注 |

以上缺口均属**来源侧不可获取**，非流水线失败；已在成果中如实标注，未用推测内容填充。

## 6. 术语表摘要

`pipeline/glossary.json` 收录 70 条核心术语，覆盖代码评审、LLM、Agent、可观测性、安全等主题，例如：现代代码评审（modern code review）、大语言模型（large language model, LLM）、最佳实践（best practices）、提示注入（prompt injection）、可观测性（observability）等。

---
*本交付物由「人 + AI」协作完成，过程留痕见 `AI日志.md` 与 `拿来说明.md`。*
