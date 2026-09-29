# C1 课程材料翻译流水线（可复跑）

把「备课/取料 → 翻译 → 术语统一 → 装配 → 校验」全过程脚本化，换个课程目录即可重跑。

## 一键复跑

```powershell
# 只抽取+分块+列出待翻译块（不调用任何模型）
powershell -ExecutionPolicy Bypass -File pipeline\run_all.ps1

# 用本机 claude CLI 自动翻译（需先执行 `claude` 完成登录）
powershell -ExecutionPolicy Bypass -File pipeline\run_all.ps1 -Backend cli:claude

# 用 OpenAI 兼容接口（需环境变量 OPENAI_API_KEY / OPENAI_BASE_URL / OPENAI_MODEL）
powershell -ExecutionPolicy Bypass -File pipeline\run_all.ps1 -Backend openai
```

## 五个步骤

| 步骤 | 脚本 | 作用 | 输入 → 输出 |
|------|------|------|-------------|
| 1 提取 | `extract.py` | PDF/HTML → 干净纯文本（去导航/脚本/样式，按页保留边界） | `source/` → `work/extracted/` |
| 2 分块 | `chunk.py` | 按段落切块，并为每块生成带术语表的提示词包 | `work/extracted/` → `work/chunks/` |
| 3 翻译 | `translate.py` | 调可插拔后端逐块翻译 | `work/chunks/*.prompt.md` → `work/out/*.zh.md` |
| 4 装配 | `assemble.py` | 逐块译文依序合并成整篇中文译稿 + 总目录 | `work/out/` → `zh/` |
| 5 校验 | `verify.py` | 覆盖率、术语命中、未译段统计 | → `work/coverage_report.json` |

## 换一门课怎么用

1. 把新课程材料放进 `source/<课程名>/`（保持 `pdfs/`、`pages/` 两个子目录约定）；
2. 修改 `extract.py` 顶部的 `SRC` 常量指向新目录；
3. 更新 `glossary.json`（新增该课程专有术语，≥50 条更佳）；
4. 重跑 `run_all.ps1`。步骤 1/2/4/5 全自动，步骤 3 选择任一后端即可。

## 术语一致性怎么保证

- `glossary.json` 是唯一术语源；`chunk.py` 会把整张术语表注入每一块的提示词，
  因此同一术语在全文各块得到统一译法；
- `verify.py` 统计术语在成品译稿中的命中数，便于发现漏译术语；
- 翻译规则固定在 `chunk.py` 的 `SYSTEM` 模板中（保留 Markdown、代码/URL 不译、
  未收录专业词首次出现用「中文（English）」）。

## 说明

- 后端是「可插拔」的：本机 CLI、在线 API、或由外部 AI 智能体/人工逐块翻译后写回
  `work/out/<块id>.zh.md` 都能接入，流水线的其余部分完全一致。
- 所有中间产物都在 `work/` 下，可随时删除重跑，不影响 `source/` 原始材料。
