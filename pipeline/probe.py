# -*- coding: utf-8 -*-
"""C1 材料体量探测：统计 PDF 页数/字符数与 HTML 正文规模，判断翻译工作量。"""
import os, re, json, sys

ROOT = r"D:\.cogseed\userWorkSpace\把我的挑战下载到我的电脑上\C1_课程翻译"
SRC = os.path.join(ROOT, "source", "CS146S_offline")

def pdf_text_engine():
    try:
        import fitz  # PyMuPDF
        return ("pymupdf", fitz)
    except Exception:
        pass
    try:
        import pdfplumber
        return ("pdfplumber", pdfplumber)
    except Exception:
        return (None, None)

def strip_html(html):
    html = re.sub(r"(?is)<script.*?</script>", " ", html)
    html = re.sub(r"(?is)<style.*?</style>", " ", html)
    html = re.sub(r"(?is)<nav.*?</nav>", " ", html)
    html = re.sub(r"(?is)<footer.*?</footer>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    import html as _h
    text = _h.unescape(text)
    text = re.sub(r"[ \t\u00a0]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()

def main():
    rep = {}
    eng, mod = pdf_text_engine()
    rep["pdf_engine"] = eng
    pdfs = []
    pdir = os.path.join(SRC, "pdfs")
    if os.path.isdir(pdir):
        for name in sorted(os.listdir(pdir)):
            if not name.lower().endswith(".pdf"):
                continue
            p = os.path.join(pdir, name)
            item = {"name": name, "bytes": os.path.getsize(p)}
            try:
                if eng == "pymupdf":
                    doc = mod.open(p)
                    item["pages"] = doc.page_count
                    chars = 0
                    for pg in doc:
                        chars += len(pg.get_text("text"))
                    item["chars"] = chars
                    doc.close()
                elif eng == "pdfplumber":
                    import pdfplumber
                    with pdfplumber.open(p) as pdf:
                        item["pages"] = len(pdf.pages)
                        item["chars"] = sum(len((pg.extract_text() or "")) for pg in pdf.pages)
                else:
                    item["pages"] = None
                    item["chars"] = None
            except Exception as e:
                item["error"] = repr(e)
            pdfs.append(item)
    rep["pdfs"] = pdfs

    pages = []
    hdir = os.path.join(SRC, "pages")
    if os.path.isdir(hdir):
        for name in sorted(os.listdir(hdir)):
            if not name.lower().endswith(".html"):
                continue
            p = os.path.join(hdir, name)
            try:
                with open(p, "r", encoding="utf-8", errors="ignore") as f:
                    raw = f.read()
                t = strip_html(raw)
                pages.append({"name": name, "raw_bytes": os.path.getsize(p), "text_chars": len(t)})
            except Exception as e:
                pages.append({"name": name, "error": repr(e)})
    rep["pages"] = pages

    site = os.path.join(SRC, "site", "themodernsoftware.dev")
    siteinfo = []
    if os.path.isdir(site):
        for name in sorted(os.listdir(site)):
            fp = os.path.join(site, name)
            if os.path.isfile(fp):
                siteinfo.append({"name": name, "bytes": os.path.getsize(fp)})
    rep["site_files"] = siteinfo

    total_pdf_chars = sum((x.get("chars") or 0) for x in pdfs)
    total_html_chars = sum((x.get("text_chars") or 0) for x in pages)
    rep["summary"] = {
        "pdf_total_chars": total_pdf_chars,
        "html_total_chars": total_html_chars,
        "combined": total_pdf_chars + total_html_chars,
    }
    out = os.path.join(ROOT, "pipeline", "probe_report.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(rep, f, ensure_ascii=False, indent=2)
    print(json.dumps(rep["summary"], ensure_ascii=False))
    print("engine:", eng)
    for x in pdfs:
        print("PDF", x.get("name"), "pages=", x.get("pages"), "chars=", x.get("chars"))
    print("html files:", len(pages), "site files:", len(siteinfo))
    print("report ->", out)

if __name__ == "__main__":
    main()
