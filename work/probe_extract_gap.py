import re, os, json

ROOT = r"D:\.cogseed\userWorkSpace\把我的挑战下载到我的电脑上\C1_课程翻译"
PAGES = os.path.join(ROOT, "source", "CS146S_offline", "pages")

TARGETS = [
    "benefits-agentic-ai-oncall.html",
    "kubernetes-troubleshooting-ai.html",
    "multi-agent-systems-ai-native.html",
    "prompt-engineering-guide.html",
    "how-warp-uses-warp.html",
    "good-context-good-code.html",
    "peeking-under-the-hood-of-claude-code.html",
    "lessons-from-ai-code-reviews.html",
]

def strip_scripts(h):
    h = re.sub(r"(?is)<script.*?</script>", " ", h)
    h = re.sub(r"(?is)<style.*?</style>", " ", h)
    return h

for name in TARGETS:
    p = os.path.join(PAGES, name)
    if not os.path.exists(p):
        print("MISSING", name); continue
    raw = open(p, "r", encoding="utf-8", errors="replace").read()
    print("=" * 70)
    print(name, "bytes_on_disk=", os.path.getsize(p), "chars_read=", len(raw))
    print("  counts: <p=", len(re.findall(r"(?i)<p[ >]", raw)),
          " <div=", len(re.findall(r"(?i)<div[ >]", raw)),
          " <script=", len(re.findall(r"(?i)<script", raw)),
          " <article=", len(re.findall(r"(?i)<article", raw)))
    joined = ""
    for m in re.findall(r'(?is)<script[^>]*>(.*?)</script>', raw):
        joined += m
    print("  script_payload_chars=", len(joined))
    print("  markers: __NEXT_DATA__=", "__NEXT_DATA__" in raw,
          " __NUXT__=", "__NUXT__" in raw,
          " window.__=", "window.__" in raw,
          " self.__next_f=", "self.__next_f" in raw,
          " apollo=", "apolloState" in raw,
          " props=", '"props"' in raw)
    body = strip_scripts(raw)
    body = re.sub(r"(?is)<(br|/p|/div|/h[1-6]|/li)[^>]*>", "\n", body)
    txt = re.sub(r"(?s)<[^>]+>", " ", body)
    txt = re.sub(r"&nbsp;?", " ", txt)
    txt = re.sub(r"[ \t]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt).strip()
    print("  tagstrip_visible_chars=", len(txt))
    print("  tagstrip_head=", repr(txt[:300]))
    # look into the biggest script payload
    if joined:
        # try to find long runs of readable text inside script payloads
        chunks = re.findall(r"(?s)[\"']([^\"'\\]{120,})[\"']", joined)
        chunks.sort(key=len, reverse=True)
        print("  script_str_count=", len(chunks), " top3_len=", [len(c) for c in chunks[:3]])
        for c in chunks[:2]:
            print("   sample=", repr(c[:240]))
    # tail of file (SSR body sometimes at end)
    print("  tail=", repr(raw[-400:]))
