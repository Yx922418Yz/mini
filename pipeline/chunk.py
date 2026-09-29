# -*- coding: utf-8 -*-
"""C1 流水线 · 第 2 步：把提取文本切成翻译块，并生成带术语表的提示词包。

用法:  python chunk.py [--max-chars 9000]
输入:  work/extracted/*.json + pipeline/glossary.json
输出:  work/chunks/<block_id>.src.txt / <block_id>.prompt.md / _chunks.json
"""
import os, re, json, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EX = os.path.join(ROOT, "work", "extracted")
OUT = os.path.join(ROOT, "work", "chunks")
PIPE = os.path.join(ROOT, "pipeline")

SYSTEM = """你是资深技术译者，正在翻译斯坦福 CS146S《The Modern Software Developer》课程材料。
把下面的英文原文翻译成简体中文。要求：
1. 忠实、通顺，术语前后一致；保留原文的 Markdown 结构（标题/列表/表格/代码块）。
2. 代码、命令行、文件名、API/产品名、URL 一律保持原文，不要翻译。
3. 严格使用下方术语表给出的译法；术语表未覆盖的专业词，首次出现时写成「中文（English）」。
4. 只输出译文本身，不要输出任何说明、致谢或前后缀。

术语表（英文 = 中文）：
%s
"""


def load_glossary():
    p = os.path.join(PIPE, "glossary.json")
    g = json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else {"terms": []}
    return "\n".join("- %s = %s" % (t["en"], t["zh"]) for t in g.get("terms", []))


def split_paras(text, maxc):
    paras = [p for p in re.split(r"\n{2,}", text) if p.strip()]
    buf, size = [], 0
    for p in paras:
        if size + len(p) > maxc and buf:
            yield "\n\n".join(buf)
            buf, size = [], 0
        if len(p) > maxc:
            for s in re.split(r"(?<=[.!?])\s+", p):
                if size + len(s) > maxc and buf:
                    yield "\n\n".join(buf)
                    buf, size = [], 0
                buf.append(s)
                size += len(s)
            continue
        buf.append(p)
        size += len(p)
    if buf:
        yield "\n\n".join(buf)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-chars", type=int, default=9000)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    gl = load_glossary()
    man = json.load(open(os.path.join(EX, "_manifest.json"), encoding="utf-8"))
    chunks = []
    for m in man:
        rec = json.load(open(os.path.join(EX, m["id"] + ".json"), encoding="utf-8"))
        text = "\n\n".join(p["text"] for p in rec["pages"])
        n = 0
        for part in split_paras(text, a.max_chars):
            n += 1
            cid = "%s.p%02d" % (m["id"], n)
            open(os.path.join(OUT, cid + ".src.txt"), "w", encoding="utf-8").write(part)
            open(os.path.join(OUT, cid + ".prompt.md"), "w", encoding="utf-8").write(
                (SYSTEM % gl) + "\n\n--- 待翻译原文 ---\n\n" + part)
            chunks.append({"id": cid, "source": m["id"], "kind": m["kind"],
                           "chars": len(part), "part": n})
    json.dump(chunks, open(os.path.join(OUT, "_chunks.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("chunks:", len(chunks), "chars:", sum(c["chars"] for c in chunks))
    for c in chunks:
        print("%-34s %-6s %6d" % (c["id"], c["kind"], c["chars"]))


if __name__ == "__main__":
    main()
