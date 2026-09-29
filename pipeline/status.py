import json, os, collections

BASE = r"D:\.cogseed\userWorkSpace\把我的挑战下载到我的电脑上\C1_课程翻译"
CH = os.path.join(BASE, "work", "chunks", "_chunks.json")
OUT = os.path.join(BASE, "work", "out")

d = json.load(open(CH, encoding="utf-8"))
items = d if isinstance(d, list) else d.get("chunks", d)

done = set()
for f in os.listdir(OUT):
    if f.endswith(".zh.md"):
        done.add(f[:-6])

pend = []
for it in items:
    cid = it.get("id")
    kind = it.get("kind", "?")
    n = it.get("chars") or len(it.get("text", "") or "")
    if cid not in done:
        pend.append((cid, kind, n))

print("TOTAL", len(items), "DONE", len(items) - len(pend), "PENDING", len(pend))
print("pending_kinds", dict(collections.Counter(k for _, k, _ in pend)))
print("--- pending ---")
for cid, kind, n in pend:
    print(cid, kind, n)
print("--- zh dir ---")
zh = os.path.join(BASE, "zh")
print("zh_exists", os.path.isdir(zh), len(os.listdir(zh)) if os.path.isdir(zh) else 0)
print("--- out files ---")
for f in sorted(os.listdir(OUT)):
    print(f, os.path.getsize(os.path.join(OUT, f)))
