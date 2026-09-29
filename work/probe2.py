import re, os, json, html as _html

ROOT = r"D:\.cogseed\userWorkSpace\把我的挑战下载到我的电脑上\C1_课程翻译"
PAGES = os.path.join(ROOT, "source", "CS146S_offline", "pages")
REC = os.path.join(ROOT, "work", "recovered")
os.makedirs(REC, exist_ok=True)

DROP = ["script", "style", "nav", "footer", "header", "aside",
        "noscript", "svg", "form", "iframe", "button"]


def strip2(raw, hijack=True):
    raw = re.sub(r"(?is)<!--.*?-->", " ", raw)
    for t in DROP:
        raw = re.sub(r"(?is)<%s\b.*?</%s>" % (t, t), " ", raw)
    if hijack:
        m = re.search(r"(?is)<(main|article)\b[^>]*>(.*?)</\1>", raw)
        if m:
            raw = m.group(2)
    txt = re.sub(r"(?s)<br\s*/?>", "\n", raw)
    txt = re.sub(r"(?s)</(p|div|li|h[1-6]|tr|blockquote|section)>", "\n", txt)
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


TARGETS = ["benefits-agentic-ai-oncall", "kubernetes-troubleshooting-ai",
           "multi-agent-systems-ai-native", "prompt-engineering-guide",
           "how-warp-uses-warp", "good-context-good-code",
           "peeking-under-the-hood-of-claude-code", "lessons-from-ai-code-reviews"]

for slug_ in TARGETS:
    p = os.path.join(PAGES, slug_ + ".html")
    if not os.path.exists(p):
        print("MISSING", slug_); continue
    raw = open(p, encoding="utf-8", errors="ignore").read()
    a = strip2(raw, hijack=True)
    b = strip2(raw, hijack=False)
    print("=" * 72)
    print(slug_, "hijack_chars=", len(a), "nohijack_chars=", len(b))
    best = a if len(a) >= len(b) else b
    print("  best_head=", repr(best[:220]))
    print("  best_tail=", repr(best[-220:]))
    if len(best) > 400:
        with open(os.path.join(REC, slug_ + ".txt"), "w", encoding="utf-8") as f:
            f.write(best)
        print("  -> wrote work/recovered/" + slug_ + ".txt")

print("=" * 72)
pm = os.path.join(ROOT, "source", "CS146S_offline", "page_map.json")
if os.path.isfile(pm):
    txt = open(pm, encoding="utf-8", errors="ignore").read()
    print("page_map.json chars=", len(txt))
    try:
        data = json.loads(txt)
        if isinstance(data, dict):
            for k, v in list(data.items())[:60]:
                print("   ", k, "=", repr(v)[:160])
        else:
            print(repr(data)[:1500])
    except Exception as e:
        print("parse err", e, repr(txt[:800]))

au = os.path.join(ROOT, "source", "CS146S_offline", "all_urls.txt")
if os.path.isfile(au):
    lines = open(au, encoding="utf-8", errors="ignore").read().splitlines()
    print("all_urls.txt lines=", len(lines))
    for kw in ["benefits-agentic-ai-oncall", "kubernetes-troubleshooting",
               "multi-agent-systems", "prompt-engineering-guide",
               "warp-uses-warp", "good-context", "peeking-under-the-hood",
               "lessons-from-ai-code-reviews", "medium.com", "notion", "stockapp"]:
        hits = [l for l in lines if kw in l]
        if hits:
            print("  KW", kw, "->", hits[:3])
