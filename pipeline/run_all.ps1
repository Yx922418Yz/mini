# C1 课程材料翻译流水线 · 一键复跑
# 用法：powershell -ExecutionPolicy Bypass -File pipeline\run_all.ps1 [-Backend none|cli:claude|cli:codex|openai]
param([string]$Backend = "none")

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $root

Write-Host "== [1/5] 提取原始材料 ==" -ForegroundColor Cyan
python pipeline\extract.py

Write-Host "== [2/5] 分块 + 生成提示词包 ==" -ForegroundColor Cyan
python pipeline\chunk.py

Write-Host "== [3/5] 翻译（后端: $Backend）==" -ForegroundColor Cyan
python pipeline\translate.py --backend $Backend

Write-Host "== [4/5] 装配中文译稿 ==" -ForegroundColor Cyan
python pipeline\assemble.py

Write-Host "== [5/5] 覆盖率 / 术语校验 ==" -ForegroundColor Cyan
python pipeline\verify.py

Write-Host "完成。译稿在 zh\ ，报告在 work\coverage_report.json" -ForegroundColor Green
