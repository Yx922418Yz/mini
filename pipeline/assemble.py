# -*- coding: utf-8 -*-
"""C1 流水线 · 第 4 步：装载译文/导读，装配成 zh/ 下的中文成品与总目录。

规则：
  - pdf 讲义 / site 主站：逐块译文 work/out/<块id>.zh.md → zh/lectures|site/<id>.zh.md（全文中文译稿）
  - html 阅读页：若已逐块全译则出全文译稿；否则用中文导读
    work/summaries/<id>.summary.md → zh/readings/<id>.summary.md，并在目录中如实标注覆盖缺口
"""
import os, json, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "work", "chunks")
OUT = os.path.join(ROOT, "work", "out")
SUM = os.path.join(ROOT, "work", "summaries")
ZH = os.path.join(ROOT, "zh")
KIND_DIR = {"pdf": "lectures", "html": "readings", "site": "site"}
KIND_ZH = {"pdf": "讲义（PDF 幻灯片）", "html": "阅读材料", "site": "课程主站"}
KIND_NOTE = {"pdf": "全文中文译稿", "html": "中文译稿 / 中文导读", "site": "中文译稿"}


def main():
    chunks = json.load(open(os.path.join(CH, "_chunks.json"), encoding="utf-8"))
    man = json.load(open(os.path.join(ROOT, "work", "extracted", "_manifest.json"), encoding="utf-8"))
    src = {m["id"]: m for m in man}
    groups = {}
    for c in chunks:
        groups.setdefault(c["source"], []).append(c)

    rows = []
    for sid, cs in groups.items():
        cs.sort(key=lambda c: c["part"])
        kind = src[sid]["kind"]
        d = os.path.join(ZH, KIND_DIR.get(kind, "misc"))
        os.makedirs(d, exist_ok=True)

        done = [c for c in cs if os.path.isfile(os.path.join(OUT, c["id"] + ".zh.md"))]
        if len(done) == len(cs):
            parts = [open(os.path.join(OUT, c["id"] + ".zh.md"), encoding="utf-8").read().strip() for c in cs]
            body = "# %s（中文译稿）\n\n> 原文：`%s` ｜ 段数：%d ｜ 原文字符：%d\n\n---\n\n%s\n" % (
                sid, src[sid]["source"], len(cs), src[sid]["chars"], "\n\n---\n\n".join(parts))
            open(os.path.join(d, sid + ".zh.md"), "w", encoding="utf-8").write(body)
            rows.append((kind, sid, src[sid]["source"], "全文译稿", src[sid]["chars"], 0))
            continue

        sp = os.path.join(SUM, sid + ".summary.md")
        if os.path.isfile(sp):
            shutil.copyfile(sp, os.path.join(d, sid + ".summary.md"))
            gap = src[sid]["chars"] - sum(c["chars"] for c in done)
            rows.append((kind, sid, src[sid]["source"], "中文导读", src[sid]["chars"], gap))
            continue

        parts, missing = [], 0
        for c in cs:
            p = os.path.join(OUT, c["id"] + ".zh.md")
            if os.path.isfile(p):
                parts.append(open(p, encoding="utf-8").read().strip())
            else:
                parts.append("> ⚠️ 本段尚未翻译（块 %s）。" % c["id"])
                missing += 1
        body = "# %s（中文译稿·部分）\n\n> 原文：`%s` ｜ 段数：%d ｜ 原文字符：%d ｜ 未译段：%d\n\n---\n\n%s\n" % (
            sid, src[sid]["source"], len(cs), src[sid]["chars"], missing, "\n\n---\n\n".join(parts))
        open(os.path.join(d, sid + ".zh.md"), "w", encoding="utf-8").write(body)
        rows.append((kind, sid, src[sid]["source"], "部分译稿(%d/%d段)" % (len(done), len(cs)),
                     src[sid]["chars"], src[sid]["chars"] - sum(c["chars"] for c in done)))

    lines = ["# CS146S 课程中文译稿 · 总目录", "",
             "由 `pipeline/assemble.py` 自动生成；覆盖率报告见 `work/coverage_report.json`。", "",
             "| 交付形式 | 说明 |", "|---|---|",
             "| 全文译稿 | 该材料已逐块全文中译 |",
             "| 中文导读 | 篇章极长的网络长文，按要点导读（附关键术语统一译法） |", ""]
    for kind in ["pdf", "html", "site"]:
        rs = [r for r in rows if r[0] == kind]
        if not rs:
            continue
        lines += ["## %s（%s）" % (KIND_ZH[kind], KIND_NOTE[kind]),
                  "| 成品 | 原文 | 形式 | 原文字符 | 未覆盖字符 |",
                  "|------|------|------|----------|------------|"]
        for _, sid, source, form, chars, gap in rs:
            ext = ".summary.md" if form == "中文导读" else ".zh.md"
            lines.append("| [%s](%s/%s%s) | `%s` | %s | %d | %d |" % (
                sid, KIND_DIR[kind], sid, ext, source, form, chars, gap))
        lines.append("")
    open(os.path.join(ZH, "index.md"), "w", encoding="utf-8").write("\n".join(lines))
    print("assembled %d sources -> %s" % (len(groups), ZH))
    print("full=%d summary=%d partial=%d" % (
        sum(1 for r in rows if r[3] == "全文译稿"),
        sum(1 for r in rows if r[3] == "中文导读"),
        sum(1 for r in rows if r[3].startswith("部分"))))


if __name__ == "__main__":
    main()
