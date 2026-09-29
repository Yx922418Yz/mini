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
Training and fine-tuning (on demand)
Worker
Worker
Workers
Source
repository
Comment
storage
Scheduler
Relevant
code
comments
Worker
Worker
Workers
Examples
(temporal
splits)
Worker
Worker
TPU pods
Tensorboard
Model
checkpoints
Input/target
format
Large-scale preprocessing (periodic)
Dataset curation (on demand)
Figure 2: Architecture of the model-training pipeline.
The readability process has some drawbacks. For authors, it in-
creases development time due to additional review rounds. For read-
ability mentors, it can become a monotonous and time-consuming
task. It requires mastering hundreds of evolving best practices, in-
cluding the identification and deprecation of outdated rules, and
documenting them (with relevant links) in the code-review sys-
tem. Additionally, it requires tracking, sometimes through multiple
iterations, ensuring that all violations have been remedied.
3
APPROACH
In response to the challenges described sections 2.1 and 2.2, we
developed AutoCommenter, a code analysis tool that automatically
detects best practice violations. It aims to provide timely feedback
for code authors and to alleviate the need for manual best-practice
reviews, thereby allowing reviewers to focus on code functionality.
3.1
Model and Task Definition
Automating best practice analysis requires a model that can rep-
resent source code, pinpoint violation locations, and identify the
violated best practice. We target a text-to-text transformation using
a traditional transformer approach based on T5, using T5X [22].
The best practice analysis is one task in a multi-task large se-
quence model. In addition to the standard pretraining task for T5,
span denoising (predicting masked tokens), other tasks used to
train this model include code-review comment resolution, next
edit prediction, variable renaming, and build-error repair [9]. The
training corpus consists of over 3 billion examples, of which the
best practice analysis dataset contributes about 800k examples. The
model was trained using the standard cross-entropy loss, typical for
such models, and tuned to maximize the sequence accuracy metric,
predicting the exact target text for each example.
For the best practice analysis, the input to the model is a task
prompt and source code, and the target is a source code loca-
tion and a URL for a best practice violation. The task prompt is
formatted as a fixed-text code comment, using the programming
language’s appropriate commenting style. It describes the task in
natural language and precedes the source code, which is a direct
textual representation of one file. If the input exceeds the model
context window, it is truncated. The location is a byte offset in the
source code, and the URL references the violated best practice. A do-
main specific language defines the target format, and a special case
is the “empty” target, if there are no violations. In addition to the
target, the model outputs a confidence score ranging from 0 to 1.
Consider the following input/target example for the Go language.
Input
/ /
[ ∗]
Task :
Check
language
b e s t
p r a c t i c e s .
/ /
Package
a d d i t i o n
p r o v i d e s
Add
package
a d d i t i o n
/ /
Return a sum
func Add ( value1 ,
value2
int )
int
{
return
value1 + value2
}
Target
INSERT 153 COMMENT h t t p s : / / go . dev / doc / comment # func
The first line of the input is the fixed-text task prompt; the rest is
the source code. The target gives the location (byte offset 153 corre-
sponds to the start of the Add function) and a go.dev URL, pointing
to the exact part of the Go language style guide that the function
comment violates (in this case, the usual practice of starting a com-
ment with the function name). Note that the target may contain no,
one, or multiple (concatenated) location-URL pairs, depending on
the number of violations in the source code.
3.2
Model Training
Figure 2 shows the architecture of the model-training pipeline,
which consists of three parts. We split dataset creation into two
steps (preprocessing and curation) because the first step is signifi-
cantly more expensive as it operates on a much larger amount of
data. The output of the preprocessing step is agnostic to the model’s
input/target representation. This separation improves feature ve-
locity by enabling quick iterations on example representations and
other example-level adjustments. The preprocessing step uses a
fault-tolerant scheduling system and periodically extracts relevant
code comments to ensure that new data is readily available.
3.2.1
Large-scale preprocessing. The training examples are created
from real code review data, but not all code comments are suitable
for model training. Therefore, the preprocessing step, identifies
relevant code comments—human authored comments that contain
a URL pointing to a best practice document. For each comment,
the preprocessing step then collects the corresponding source code
and relevant metadata, including the comment’s location in the
source code and its creation time. The output of this step is a set
of relevant code comments, each with all the data necessary for
curating examples for model training.