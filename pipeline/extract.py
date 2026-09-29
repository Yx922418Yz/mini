# -*- coding: utf-8 -*-
"""C1 流水线 · 第 1 步：从原始材料提取干净文本。

用法:  python extract.py
输入:  source/CS146S_offline/{pdfs,pages,index.html}
输出:  work/extracted/<slug>.json (含 pages/字符数) 与 <slug>.txt 与 _manifest.json
"""
import os, re, json
import html as _html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "CS146S_offline")
OUT = os.path.join(ROOT, "work", "extracted")

DROP_TAGS = ["script", "style", "nav", "footer", "header", "aside",
             "noscript", "svg", "form", "iframe", "button"]


def _to_text(raw):
    txt = re.sub(r"(?s)<br\s*/?>", "\n", raw)
    txt = re.sub(r"(?s)</(p|div|li|h[1-6]|tr|blockquote)>", "\n", txt)
    txt = re.sub(r"(?s)<[^>]+>", "", txt)
    txt = _html.unescape(txt).replace("\u00a0", " ")
    out, prev = [], None
    for line in txt.split("\n"):
        line = re.sub(r"[ \t]+", " ", line).strip()
        if not line or line == prev:
            continue
        out.append(line)
        prev = line
    return "\n".join(out)


def strip_html(raw):
    raw = re.sub(r"(?is)<!--.*?-->", " ", raw)
    for t in DROP_TAGS:
        raw = re.sub(r"(?is)<%s\b.*?</%s>" % (t, t), " ", raw)
    whole = _to_text(raw)
    m = re.search(r"(?is)<(main|article)\b[^>]*>(.*?)</\1>", raw)
    if m:
        inner = _to_text(m.group(2))
        # React/Next 流式渲染页面常常是空的 <main> 外壳，此时回退到整页正文
        if len(inner) >= 600 or len(inner) >= 0.5 * len(whole):
            return inner
    return whole


def clean_pdf(text):
    t = text.replace("\u00a0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    out, blank = [], 0
    for line in t.split("\n"):
        line = line.strip()
        if not line:
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(line)
    return "\n".join(out).strip()


def slug(name):
    s = re.sub(r"\.[A-Za-z0-9]+$", "", name)
    return re.sub(r"[^0-9A-Za-z._-]+", "-", s).strip("-").lower()


def write_rec(rec):
    with open(os.path.join(OUT, rec["id"] + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=2)
    txt = "\n\n".join(p["text"] for p in rec["pages"])
    with open(os.path.join(OUT, rec["id"] + ".txt"), "w", encoding="utf-8") as f:
        f.write(txt)


def meta(rec):
    return {"id": rec["id"], "kind": rec["kind"],
            "source": rec["source"], "chars": rec["chars"]}


def add(manifest, rec):
    write_rec(rec)
    manifest.append(meta(rec))


def main():
    os.makedirs(OUT, exist_ok=True)
    manifest = []

    pdir = os.path.join(SRC, "pdfs")
    if os.path.isdir(pdir):
        import pymupdf
        for name in sorted(os.listdir(pdir)):
            if not name.lower().endswith(".pdf"):
                continue
            doc = pymupdf.open(os.path.join(pdir, name))
            pages = []
            for i, pg in enumerate(doc, 1):
                t = clean_pdf(pg.get_text("text"))
                if t:
                    pages.append({"i": i, "text": t})
            doc.close()
            add(manifest, {"id": "pdf-" + slug(name), "kind": "pdf", "source": name,
                           "chars": sum(len(p["text"]) for p in pages), "pages": pages})

    hdir = os.path.join(SRC, "pages")
    if os.path.isdir(hdir):
        for name in sorted(os.listdir(hdir)):
            if not name.lower().endswith(".html"):
                continue
            raw = open(os.path.join(hdir, name), encoding="utf-8", errors="ignore").read()
            t = strip_html(raw)
            add(manifest, {"id": "html-" + slug(name), "kind": "html", "source": name,
                           "chars": len(t), "pages": [{"i": 1, "text": t}] if t else []})

    idx = os.path.join(SRC, "index.html")
    if os.path.isfile(idx):
        t = strip_html(open(idx, encoding="utf-8", errors="ignore").read())
        add(manifest, {"id": "site-themodernsoftware", "kind": "site", "source": "index.html",
                       "chars": len(t), "pages": [{"i": 1, "text": t}] if t else []})

    with open(os.path.join(OUT, "_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("sources:", len(manifest), "total_chars:", sum(m["chars"] for m in manifest))
    for m in manifest:
        print("%-40s %-6s %8d" % (m["id"], m["kind"], m["chars"]))


if __name__ == "__main__":
    main()
