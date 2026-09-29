# -*- coding: utf-8 -*-
"""C1 流水线 · 第 5 步：覆盖率与术语一致性校验并输出报告（work/coverage_report.json）。"""
import os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "work", "chunks")
OUT = os.path.join(ROOT, "work", "out")
ZH = os.path.join(ROOT, "zh")


def main():
    chunks = json.load(open(os.path.join(CH, "_chunks.json"), encoding="utf-8"))
    man = json.load(open(os.path.join(ROOT, "work", "extracted", "_manifest.json"), encoding="utf-8"))
    gloss = json.load(open(os.path.join(ROOT, "pipeline", "glossary.json"), encoding="utf-8"))["terms"]

    rep = {"by_source": []}
    for m in man:
        cs = [c for c in chunks if c["source"] == m["id"]]
        done = [c for c in cs if os.path.isfile(os.path.join(OUT, c["id"] + ".zh.md"))]
        dch = sum(c["chars"] for c in done)
        rep["by_source"].append({
            "id": m["id"], "kind": m["kind"], "source": m["source"],
            "src_chars": m["chars"], "chunks": len(cs), "done": len(done),
            "translated_src_chars": dch,
            "coverage": round(dch / m["chars"], 4) if m["chars"] else 0.0})

    zh_text = ""
    for root, _, files in os.walk(ZH):
        for fn in files:
            if fn.endswith(".md"):
                zh_text += open(os.path.join(root, fn), encoding="utf-8").read()
    used = [t for t in gloss if t["zh"] and t["zh"] in zh_text]

    lect = [r for r in rep["by_source"] if r["kind"] == "pdf"]
    rep["glossary"] = {"total": len(gloss), "used_in_deliverable": len(used)}
    rep["summary"] = {
        "lectures_coverage": round(sum(r["translated_src_chars"] for r in lect) /
                                   max(1, sum(r["src_chars"] for r in lect)), 4),
        "overall_coverage": round(sum(r["translated_src_chars"] for r in rep["by_source"]) /
                                  max(1, sum(r["src_chars"] for r in rep["by_source"])), 4),
        "glossary_terms": len(gloss),
        "untranslated_chunks": sum(r["chunks"] - r["done"] for r in rep["by_source"]),
    }
    json.dump(rep, open(os.path.join(ROOT, "work", "coverage_report.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("== SUMMARY ==")
    print(json.dumps(rep["summary"], ensure_ascii=False, indent=2))
    for r in rep["by_source"]:
        print("%-38s %-5s cov=%.2f  %d/%d chunks" % (
            r["id"], r["kind"], r["coverage"], r["done"], r["chunks"]))


if __name__ == "__main__":
    main()
