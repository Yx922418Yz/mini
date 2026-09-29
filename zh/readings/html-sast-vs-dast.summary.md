# SAST vs. DAST vs. RASP：应用安全测试方法对比（导读）

> 来源：Splunk（作者 Shanika Wickramasinghe，2024-12-18） · 文章 id：`html-sast-vs-dast` · 原文约 21.1K 字符

## 核心主张
本文对比应用安全测试的三种方法 SAST、DAST 与 RASP，指出面对日益严峻的威胁，企业需要超越传统方法的多层防护策略。核心论点是：SAST 与 DAST 角色互补——SAST 在开发早期从静态源码找漏洞、修复成本更低；DAST 在运行期从外部模拟攻击、覆盖运行时与环境相关问题；二者叠加（并可加入 IAST/RASP）并自动化进 CI/CD，才能形成覆盖整个软件开发生命周期（SDLC）的完整安全策略。

## 关键要点（原文引用）
- 背景数据：全球信息安全支出预计 2025 年达到 $212 billion，较 2024 年增长 15%；据 Gartner，到 2027 年 GenAI 将参与 17% 的网络攻击。
- SAST = Static Application Security Testing，白盒测试，基于应用的静态源码或二进制，在应用不运行时工作。
- DAST = Dynamic Application Security Testing，黑盒测试，在应用运行时从外部模拟攻击者，且无需访问源码。
- RASP = Runtime Application Self-Protection，直接安装在应用运行的服务器上，实时检测异常行为并即时阻断，而不仅是告警。
- 常见 SAST 方法：pattern matching、data flow analysis、control flow analysis、custom rule creation、dependency scanning、semantic analysis、machine learning models。
- 自定义规则示例：标记 SQL 查询中未净化输入、输出未转义的用户数据、使用 eval() in JavaScript 或 strcpy() in C 等危险函数、硬编码 API keys and passwords。
- 性能：SAST 全量扫描百万行代码可能消耗数 GB RAM，耗时从小项目几分钟到企业级应用数小时；建议采用支持 incremental scanning 的工具并做规则与范围调优。
- DAST 四步流程：Step 1 Scanning → Step 2 Attack simulation → Step 3 Vulnerability detection → Step 4 Reporting。
- DAST 性能瓶颈与缓解：扫描占用 CPU/内存与网络带宽、使缓存失效；应对措施包括在 off-peak hours 扫描、使用 staging 或 pre-production 环境、开启 throttling、增加线程池、为扫描器 IP 单独配置缓存策略、超过阈值自动暂停。
- 关键差异：SAST 假阳性更高但能定位代码级漏洞；DAST 假阳性更低但假阴性风险高、缺乏内部可见性；SAST 依赖编程语言与框架，DAST 与语言无关。
- 原文举例：用不安全随机数生成器（如 Math.random() in JavaScript）创建 session token 的缺陷，DAST 只测运行时行为会漏掉，而 SAST 能检测到。
- 未来方向：AI/ML 将减少假阳性、提升威胁检测；SAST 查固件漏洞、DAST 测通信协议、RASP 监控已部署设备，三者在金融与 IoT/edge 场景协同。

## 术语与译法
- `SAST` → 静态应用安全测试（SAST）
- `DAST` → 动态应用安全测试（DAST）
- `Static Analysis` → 静态分析
- `Vulnerability` → 漏洞
- `Injection` → 注入
- `OWASP Top Ten` → OWASP 十大安全风险
- `Continuous Integration` → 持续集成

## 结论
SAST 与 DAST 并非二选一，而是互补两层：SAST 在早期深入代码、降低修复成本并推动安全编码，DAST 在预生产与部署后暴露运行时漏洞；把两者连同 IAST/RASP 自动化进 CI/CD，才能获得覆盖静态代码与运行环境的持续安全防护。
