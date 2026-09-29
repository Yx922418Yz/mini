# -*- coding: utf-8 -*-
"""C1 流水线 · 第 3 步：调用可插拔翻译后端，把 work/chunks/*.prompt.md 翻成 work/out/<id>.zh.md。

后端（--backend）：
  cli:claude   本机 claude CLI 无头模式（需先执行 `claude` 登录）
  cli:codex    本机 codex CLI
  openai       OpenAI 兼容接口（环境变量 OPENAI_API_KEY / OPENAI_BASE_URL / OPENAI_MODEL）
  none         不翻译，仅列出待翻译块（由外部 AI 智能体或人工把译文写回 work/out/）

示例：
  python translate.py --backend none
  python translate.py --backend cli:claude --parallel 4
  python translate.py --backend openai --model gpt-4o-mini --only pdf-
"""
import os, json, argparse, subprocess
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "work", "chunks")
OUT = os.path.join(ROOT, "work", "out")


def pending():
    chunks = json.load(open(os.path.join(CH, "_chunks.json"), encoding="utf-8"))
    return chunks, [c for c in chunks if not os.path.isfile(os.path.join(OUT, c["id"] + ".zh.md"))]


def run_cli(cli, prompt):
    if cli == "claude":
        exe = os.path.expanduser(r"~\.local\bin\claude.exe")
        cmd = [exe if os.path.isfile(exe) else "claude", "-p", prompt, "--output-format", "text"]
    else:
        cmd = ["codex", "exec", prompt]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=3600)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "")[:500])
    return p.stdout.strip()


def run_openai(prompt, model):
    import urllib.request
    base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    body = json.dumps({"model": model, "temperature": 0.2,
                       "messages": [{"role": "user", "content": prompt}]}).encode("utf-8")
    req = urllib.request.Request(base + "/chat/completions", data=body, headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]})
    with urllib.request.urlopen(req, timeout=3600) as r:
        return json.loads(r.read().decode("utf-8"))["choices"][0]["message"]["content"].strip()


def do_one(c, backend, model):
    prompt = open(os.path.join(CH, c["id"] + ".prompt.md"), encoding="utf-8").read()
    zh = run_cli(backend.split(":", 1)[1], prompt) if backend.startswith("cli:") else run_openai(prompt, model)
    open(os.path.join(OUT, c["id"] + ".zh.md"), "w", encoding="utf-8").write(zh)
    return c["id"], len(zh)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", default="none")
    ap.add_argument("--model", default=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"))
    ap.add_argument("--parallel", type=int, default=2)
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    chunks, todo = pending()
    if a.only:
        todo = [c for c in todo if c["source"].startswith(a.only)]
    print("chunks=%d pending=%d backend=%s" % (len(chunks), len(todo), a.backend))
    if a.backend == "none":
        for c in todo:
            print("  TODO %-34s %6d" % (c["id"], c["chars"]))
        print("提示：把每块译文写到 work/out/<id>.zh.md；可用 --only 分批。")
        return
    with ThreadPoolExecutor(max_workers=max(1, a.parallel)) as ex:
        for f in [ex.submit(do_one, c, a.backend, a.model) for c in todo]:
            print("done", f.result())


if __name__ == "__main__":
    main()
