你是资深技术译者，正在翻译斯坦福 CS146S《The Modern Software Developer》课程材料。
把下面的英文原文翻译成简体中文。要求：
1. 忠实、通顺，术语前后一致；保留原文的 Markdown 结构（标题/列表/表格/代码块）。
2. 代码、命令行、文件名、API/产品名、URL 一律保持原文，不要翻译。
3. 严格使用下方术语表给出的译法；术语表未覆盖的专业词，首次出现时写成「中文（English）」。
4. 只输出译文本身，不要输出任何说明、致谢或前后缀。

术语表（英文 = 中文）：
- Vibe Coding = 氛围编程
- Scaffolding = 脚手架
- Context Engineering = 上下文工程
- Context Rot = 上下文腐化
- Agent = 智能体
- Agentic AI = 智能体式 AI
- Coding Agent = 编码智能体
- LLM = 大语言模型
- Prompt = 提示词
- Prompt Engineering = 提示工程
- System Prompt = 系统提示词
- Token = 词元
- Context Window = 上下文窗口
- Long-context = 长上下文
- Hallucination = 幻觉
- Code Review = 代码评审
- Pull Request = 拉取请求
- Commit = 提交
- Repository = 仓库
- Monorepo = 单体仓库
- Refactor = 重构
- Linter = 静态检查器
- Static Analysis = 静态分析
- SAST = 静态应用安全测试（SAST）
- DAST = 动态应用安全测试（DAST）
- Vulnerability = 漏洞
- Injection = 注入
- Prompt Injection = 提示注入
- Remote Code Execution = 远程代码执行
- Supply Chain Attack = 供应链攻击
- OWASP Top Ten = OWASP 十大安全风险
- Model Context Protocol = 模型上下文协议
- MCP Server = MCP 服务器
- Tool Use = 工具调用
- Tool Definition = 工具定义
- Observability = 可观测性
- Telemetry = 遥测
- Distributed Tracing = 分布式链路追踪
- On-call = 值班
- Incident = 事故
- Site Reliability Engineering = 站点可靠性工程
- Service Level Agreement = 服务等级协议
- Multi-agent System = 多智能体系统
- Orchestration = 编排
- Sandbox = 沙箱
- Permission = 权限
- Approval Flow = 审批流
- Spec = 规格说明
- Spec-driven Development = 规格驱动开发
- Unit Test = 单元测试
- Continuous Integration = 持续集成
- Troubleshooting = 排障
- Retrieval-Augmented Generation = 检索增强生成
- Embedding = 嵌入向量
- Vector Database = 向量数据库
- Benchmark = 基准测试
- Evaluation = 评估
- Guardrail = 护栏
- Human-in-the-loop = 人在回路
- Autonomy = 自主性
- Latency = 延迟
- Throughput = 吞吐量
- Regression = 回归
- Pair Programming = 结对编程
- Technical Debt = 技术债
- Deterministic = 确定性的
- Rubber Duck Debugging = 小黄鸭调试法


--- 待翻译原文 ---

AI-Assisted Assessment of Coding Practices in Modern Code Review
AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
REFERENCES
[1] 2024. Google Style Guides. https://google.github.io/styleguide/.
Accessed:
2024-03-15.
[2] 2024. Linux kernel coding style. https://www.kernel.org/doc/html/v4.10/process/
coding-style.html. Accessed: 2024-03-15.
[3] 2024. PEP 8 – Style Guide for Python Code. https://peps.python.org/pep-0008/.
Accessed: 2024-03-15.
[4] 2024. Rust Style Guide. https://doc.rust-lang.org/nightly/style-guide/. Accessed:
2024-03-15.
[5] Alberto Bacchelli and Christian Bird. 2013. Expectations, outcomes, and chal-
lenges of modern code review. In 2013 35th International Conference on Software
Engineering (ICSE). 712–721. https://doi.org/10.1109/ICSE.2013.6606617
[6] Moritz Beller, Radjino Bholanath, Shane McIntosh, and Andy Zaidman. 2016.
Analyzing the state of static analysis: A large-scale evaluation in open source soft-
ware. In 2016 IEEE 23rd International Conference on Software Analysis, Evolution,
and Reengineering (SANER), Vol. 1. IEEE, 470–481.
[7] Zimin Chen, Małgorzata Salawa, Manushree Vijayvergiya, Goran Petrović, Marko
Ivanković, and René Just. 2023. MuRS: Mutant Ranking and Suppression using
Identifier Templates. In Proceedings of the Symposium on the Foundations of
Software Engineering (FSE). 1798–1808.
[8] M. E. Fagan. 1976. Design and code inspections to reduce errors in program
development. IBM Systems Journal 15, 3 (1976), 182–211. https://doi.org/10.1147/
sj.153.0182
[9] Alexander Frömmgen, Jacob Austin, Peter Choy, Nimesh Ghelani, Lera Kharatyan,
Gabriela Surita, Elena Khrapko, Pascal Lamblin, Pierre-Antoine Manzagol, Marcus
Revaj, Maxim Tabachnyk, Daniel Tarlow, Kevin Villela, Daniel Zheng, Satish
Chandra, and Petros Maniatis. 2024. Resolving Code Review Comments with
Machine Learning. In International Conference on Software Engineering: Software
Engineering in Practice (ICSE-SEIP).
[10] Sarah Heckman and Laurie Williams. 2011. A systematic literature review of
actionable alert identification techniques for automated static code analysis.
Information and Software Technology 53, 4 (2011), 363–387. https://doi.org/10.
1016/j.infsof.2010.12.007 Special section: Software Engineering track of the 24th
Annual Symposium on Applied Computing.
[11] Yang Hong, Chakkrit Tantithamthavorn, Patanamon Thongtanunam, and Aldeida
Aleti. 2022. Commentfinder: a simpler, faster, more accurate code review com-
ments recommendation. In Proceedings of the Joint Meeting of the European Soft-
ware Engineering Conference and the Symposium on the Foundations of Software
Engineering (ESEC/FSE). 507–519.
[12] Marko Ivanković, Goran Petrović, René Just, and Gordon Fraser. 2019. Code
Coverage at Google. In Proceedings of the Joint Meeting of the European Soft-
ware Engineering Conference and the Symposium on the Foundations of Software
Engineering (ESEC/FSE). 955–963.
[13] Marko Ivanković, Goran Petrović, Yana Kulizhskaya, Mateusz Lewko, Luka Kali-
novčić, René Just, and Gordon Fraser. 2024. Productive Coverage: Improving
the Actionability of Code Coverage. In International Conference on Software
Engineering: Software Engineering in Practice (ICSE-SEIP).
[14] Brittany Johnson, Yoonki Song, Emerson Murphy-Hill, and Robert Bowdidge.
2013. Why don’t software developers use static analysis tools to find bugs?. In
2013 35th International Conference on Software Engineering (ICSE). IEEE, 672–681.
[15] Stephen C Johnson. 1977. Lint, a C program checker. Bell Telephone Laboratories
Murray Hill.
[16] Lingwei Li, Li Yang, Huaxi Jiang, Jun Yan, Tiejian Luo, Zihan Hua, Geng Liang,
and Chun Zuo. 2022. Auger: Automatically generating review comments with
pre-training models. In Proceedings of the Joint Meeting of the European Soft-
ware Engineering Conference and the Symposium on the Foundations of Software
Engineering (ESEC/FSE). 1009–1021.
[17] Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep
Majumder, Jared Green, Alexey Svyatkovskiy, Shengyu Fu, and Neel Sundaresan.
2022. Automating code review activities by large-scale pre-training. In Proceedings
of the 30th ACM Joint European Software Engineering Conference and Symposium
on the Foundations of Software Engineering (<conf-loc>, <city>Singapore</city>,
<country>Singapore</country>, </conf-loc>) (ESEC/FSE 2022). Association for
Computing Machinery, New York, NY, USA, 1035–1047. https://doi.org/10.1145/
3540250.3549081
[18] Goran Petrović, Marko Ivanković, Gordon Fraser, and René Just. 2023. Please fix
this mutant: How do developers resolve mutants surfaced during code review?. In
International Conference on Software Engineering: Software Engineering in Practice
(ICSE-SEIP). 150–161.
[19] Rachel Potvin and Josh Levenberg. 2016. Why Google Stores Billions of Lines
of Code in a Single Repository. Communications of the ACM (CACM) 59 (2016),
78–87. http://dl.acm.org/citation.cfm?id=2854146
[20] Peter Rigby, Brendan Cleary, Frederic Painchaud, Margaret-Anne Storey, and
Daniel German. 2012. Contemporary Peer Review in Action: Lessons from Open
Source Development. IEEE Software 29, 6 (2012), 56–61. https://doi.org/10.1109/
MS.2012.24
[21] Peter C. Rigby and Christian Bird. 2013. Convergent contemporary software peer
review practices. In Proceedings of the 2013 9th Joint Meeting on Foundations of
Software Engineering (Saint Petersburg, Russia) (ESEC/FSE 2013). Association for
Computing Machinery, New York, NY, USA, 202–212. https://doi.org/10.1145/
2491411.2491444
[22] Adam Roberts, Hyung Won Chung, Gaurav Mishra, Anselm Levskaya, James
Bradbury, Daniel Andor, Sharan Narang, Brian Lester, Colin Gaffney, Afroz
Mohiuddin, et al. 2023. Scaling up models and data with t5x and seqio. Journal
of Machine Learning Research 24, 377 (2023), 1–8.
[23] Caitlin Sadowski, Emma Söderberg, Luke Church, Michal Sipko, and Alberto
Bacchelli. 2018. Modern Code Review: A Case Study at Google. In International
Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP).
181–190.
[24] Patanamon Thongtanunam, Chanathip Pornprasit, and Chakkrit Tantithamtha-
vorn. 2022. Autotransform: Automated code transformation to support modern
code review process. In Proceedings of the International Conference on Software
Engineering (ICSE). 237–248.
[25] Rosalia Tufano, Ozren Dabić, Antonio Mastropaolo, Matteo Ciniselli, and Gabriele
Bavota. 2024. Code Review Automation: Strengths and Weaknesses of the State
of the Art. IEEE Transactions on Software Engineering (TSE) (2024).
[26] Rosalia Tufano, Simone Masiero, Antonio Mastropaolo, Luca Pascarella, Denys
Poshyvanyk, and Gabriele Bavota. 2022. Using pre-trained models to boost code
review automation. In Proceedings of the International Conference on Software
Engineering (ICSE). 2291–2302.
[27] Carmine Vassallo, Sebastiano Panichella, Fabio Palomba, Sebastian Proksch, Har-
ald C Gall, and Andy Zaidman. 2020. How developers engage with static analysis
tools in different contexts. Empirical Software Engineering 25 (2020), 1419–1457.
[28] T. Winters, T. Manshreck, and H. Wright. 2020. Software Engineering at Google:
Lessons Learned from Programming Over Time. O’Reilly Media. https://books.
google.ch/books?id=TyIrywEACAAJ
Received 2024-04-05; accepted 2024-05-04