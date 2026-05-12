# ScholarFit 理论框架

## 0. 项目定位

ScholarFit / 学术罗盘不是“博士天赋测试”，而是一个开源的、故事化的科研自我理解与博士路径适配系统。它通过情境判断题、研究行为证据、人格与动机测量、方向兴趣、导师环境匹配、压力恢复方式等维度，帮助用户理解自己当前是否准备好进入博士训练，以及更适合什么样的研究方向、导师和课题组。

核心原则：

1. 不做诊断：不诊断心理疾病，不判断人格缺陷。
2. 不做淘汰：不输出“你不适合读博”这种封闭结论。
3. 不迷信 MBTI：Jung/MBTI 只做叙事层，不做预测核心。
4. 强调发展性：输出优势、风险、适配环境和成长建议。
5. 强调验证：题库、评分逻辑和报告语言都要接受信度、效度、公平性与隐私审查。

## 1. 总体理论地图

```text
ScholarFit 理论结构
├── 核心测量层 Core Measurement
│   ├── SJT 情境判断测验
│   ├── Contextualized Personality 情境化人格
│   ├── Big Five / HEXACO / IPIP
│   ├── Research Self-Efficacy 科研自我效能
│   ├── Self-Determination Theory 读博动机
│   ├── RIASEC + Research Interest Ontology 方向兴趣
│   └── Person-Environment Fit 人-环境匹配
│
├── 情境叙事层 Narrative Layer
│   ├── PhD Journey 故事章节
│   ├── 导师塔 / 文献迷宫 / 实验废墟 / 同行审判
│   └── Jung / MBTI 风格语言
│
└── 评估与治理层 Validation & Governance
    ├── Psychometric Validation 信效度验证
    ├── Forced-choice / IRT Scoring 强制选择建模
    ├── Fairness / Measurement Invariance 公平性
    ├── Privacy / Digital Phenotyping Ethics 隐私伦理
    └── Open-source Transparency 开源透明
```

## 2. 核心理论模块

### 2.1 Situational Judgment Tests, SJT

SJT 让用户面对接近真实工作或学习场景的情境，然后选择、排序或评价可能行动。SJT 可被设计为测量多种构念，但前提是先明确 construct，再写情境和选项 [@christian2010situational; @lievens2016situational]。

PhD 训练高度情境化：选导师、读文献、复现实验、面对失败、处理审稿意见、决定是否转方向、应对长期不确定性。这些行为很难只靠抽象 Likert 题捕捉。因此，SJT 是 ScholarFit 的主干题型。

| PhD 情境 | 可测 construct |
| --- | --- |
| 文献读不懂 | 学习策略、问题抽象、求助倾向 |
| 实验失败 | debug 思维、抗挫、系统复盘 |
| 导师放养 | 自主性、结构需求、反馈需求 |
| 被 reviewer 批评 | 反馈接受、学术自尊稳定性 |
| 方向变化 | 探索/收敛平衡、风险偏好 |
| 论文压力 | 学术诚信、短期产出取向 |
| 长期孤独 | 压力恢复、支持系统 |

设计原则：不要写“你遇到困难会坚持吗？”；应写“你复现一篇机器人操作论文，官方代码能跑，但结果比论文低 20%。你已经检查三天仍然找不到原因。你下一步最可能怎么做？”

### 2.2 情境化人格测量

情境化人格测量把普通人格题嵌入具体工作、学习或科研场景。Frame-of-reference personality assessment 的研究指出，情境化题项通常更贴近特定结果变量，也更便于解释为行为倾向 [@shaffer2012meta]。

普通题：

```text
我是一个有条理的人。
```

科研情境化题：

```text
我会系统记录实验配置、失败原因和下一步修改，而不是只记录成功结果。
```

| 维度 | 科研语境含义 |
| --- | --- |
| Openness | 跨学科连接、抽象建模、问题发现 |
| Conscientiousness | 实验记录、长期推进、复现耐心 |
| Emotional Stability | 面对失败、批评、不确定性的恢复力 |
| Agreeableness | 合作、接受反馈、组内沟通 |
| Extraversion | 学术社交、主动讨论、合作驱动 |
| Honesty-Humility | 学术诚信、如实报告失败、承认不懂 |

### 2.3 游戏化与故事化测评

故事化测评可以改善参与体验，但不能替代 construct validity。ScholarFit 的叙事应服务于测量：每个剧情节点都必须对应明确 construct，每个选项都要有可解释的行为倾向，且后续需要验证故事版与非故事版题项的相关性、信度和公平性。

建议章节：

```text
Chapter 1：研究之门
Chapter 2：文献迷宫
Chapter 3：实验废墟
Chapter 4：导师之塔
Chapter 5：同行审判
Chapter 6：方向岔路
Chapter 7：孤独长夜
Chapter 8：创造之火
```

### 2.4 Big Five / HEXACO / IPIP

Big Five 和 HEXACO 是成熟人格框架。HEXACO 增加 Honesty-Humility，有助于解释学术诚信、透明报告和承认不懂等科研伦理行为 [@lee2004psychometric]。IPIP 的优势是开放：公开题项可作为开源项目改写和本地化的基础 [@ipip2026]。

注意：不要直接复制受限制的官方量表题项。公开在线应用应优先使用 public-domain 题项或自行编写并验证的题项。

### 2.5 Research Self-Efficacy

科研自我效能比“我聪不聪明”更可操作。它关注用户是否相信自己能完成研究设计、文献整合、数据/计算、写作和实践推进等任务。SERM 及相关研究为该模块提供了可参考的维度结构 [@phillips1994research; @kahn1997short]。

| 章节 | 能力问题 |
| --- | --- |
| 文献迷宫 | 能否理解、比较和整合论文？ |
| 实验废墟 | 能否复现、debug、分析失败？ |
| 统计审判 | 能否解释指标、数据和实验结论？ |
| 论文工坊 | 能否表达贡献、写出清晰研究叙事？ |

### 2.6 Self-Determination Theory, SDT

SDT 区分自主性动机与受控性动机。对博士训练而言，健康动机通常不是“外界让我读博”，而是研究问题、长期目标和学术身份之间形成一定一致性 [@ryan2000self]。

| 动机类型 | 风险/意义 |
| --- | --- |
| Intrinsic motivation | 因问题本身有吸引力，适合长期探索 |
| Identified motivation | 读博与长期目标一致，较健康 |
| Introjected motivation | 想证明自己、害怕失败，容易焦虑 |
| External motivation | 为学历、身份、他人期待，长期风险较高 |
| Amotivation | 不清楚为什么读，退出风险较高 |

### 2.7 RIASEC + Research Interest Ontology

RIASEC 可作为兴趣结构底座，但对科研方向来说过粗 [@onet2021interest]。ScholarFit 在 RIASEC 上叠加研究兴趣本体。

| 类型 | 典型偏好 |
| --- | --- |
| Theoretical | 公式、证明、理论解释、泛化边界 |
| Experimental | benchmark、消融、指标、统计 |
| Engineering/System | 系统搭建、大规模训练、框架集成 |
| Robotic/Embodied | 感知-控制闭环、硬件、仿真到现实 |
| Cognitive/Agentic | world model、memory、planning、agent |
| Human/Social | HCI、教育、心理、用户研究 |
| Translational/Application | 医疗、工业、科学发现、实际落地 |

### 2.8 Person-Environment Fit

PhD 结果不只取决于学生，还取决于导师、实验室、资源、制度和压力文化。P-E Fit 理论认为，个人需求与环境供给、个人价值与环境价值之间的匹配会影响满意度、压力、表现和留存 [@kristofbrown2005consequences; @vanvianen2018person]。

| Fit 类型 | PhD 语境 |
| --- | --- |
| Person-Advisor Fit | 导师指导风格是否匹配 |
| Person-Lab Fit | 组会文化、合作方式、代码规范是否匹配 |
| Person-Topic Fit | 研究问题是否符合兴趣和能力结构 |
| Person-Resource Fit | 算力、数据、设备、经费是否满足需求 |
| Person-Autonomy Fit | 自由探索 vs 明确任务是否匹配 |
| Person-Pressure Fit | 高压产出文化是否可承受 |

### 2.9 博士导师关系与训练环境

博士经历研究显示，supervision、department socialization、financial support、motivation、writing skills、self-regulation 和 academic identity 都会影响博士完成、成就和幸福感 [@sverdlik2018phd]。因此，ScholarFit 把导师/实验室匹配作为独立模块，而不是附属问题。

可测维度：Feedback need、Structure need、Autonomy tolerance、Criticism tolerance、Resource dependency、Socialization need、Career alignment。

### 2.10 博士心理健康与压力风险

博士心理健康模块必须谨慎。它不能输出诊断，只能输出科研压力风险提示、适应风险、支持系统脆弱点和需要寻求现实支持的信号。研究生心理健康文献显示，博士群体存在显著压力与心理健康风险，但具体判断必须由专业人士完成 [@evans2018evidence; @satinsky2021systematic; @hazell2020understanding]。

正确输出：

```text
你在科研压力场景中表现出较高自我否定倾向，建议建立更明确的失败复盘机制和现实支持系统。
```

错误输出：

```text
你有抑郁倾向。
你心理不适合读博。
```

### 2.11 心理测量验证

AERA、APA、NCME 的测试标准强调，测验开发、使用和解释都需要证据链 [@aera2014standards]。量表开发通常包括题项生成、内容效度、预测试、结构验证、信度、效度和公平性评估 [@boateng2018best]。

验证路线：

```text
阶段 1：专家评审内容效度
阶段 2：认知访谈与小样本预试
阶段 3：EFA 探索性因子分析
阶段 4：CFA 验证性因子分析
阶段 5：信度：alpha / omega / test-retest
阶段 6：效标效度：科研行为、持续投入、满意度等
阶段 7：公平性：性别、专业、学历、文化背景测量不变性
阶段 8：版本迭代与题库删改
```

### 2.12 强制选择与 IRT

排序题和强制选择题能减少“所有好品质都选非常同意”的社会赞许性偏差，但传统 forced-choice 容易产生 ipsative data，影响跨个体比较。后续可引入 Thurstonian IRT 或 multidimensional forced-choice IRT [@brown2011thurstonian]。

v0.1 可以先使用规则评分，但必须保留原始排序数据，为后续模型升级做准备。

### 2.13 数字表型与隐私伦理

ScholarFit 可以有“行为证据分析”，但必须默认本地优先、用户主动上传、不后台监控、不抓取聊天/浏览器/手机数据、不做心理诊断、不向第三方共享、可删除、可导出、可解释。

允许用户主动上传：论文阅读笔记、GitHub README、项目报告、研究计划、失败复盘、时间投入记录。

不建议默认采集：键盘记录、浏览器历史、手机定位、社交聊天内容、后台行为轨迹。

## 3. 核心层与解释层

核心测量层：SJT、情境化人格、Big Five/HEXACO/IPIP、科研自我效能、SDT、P-E Fit、心理测量验证、forced-choice/IRT。

辅助解释层：Jung/MBTI、游戏化、数字表型、RIASEC。MBTI 只能用于风格化语言，例如“偏好深度独立工作”或“偏好讨论驱动探索”，不能用于预测读博成败或筛选。

## 4. 输出框架

报告不输出单一总分，而输出九个 profile：

```text
Research Motivation Profile
Research Self-Efficacy Profile
Research Behavior Profile
Personality-in-Research Profile
Research Direction Fit Profile
Advisor/Lab Fit Profile
Stress & Recovery Profile
Academic Integrity Profile
Growth Recommendation Profile
```

最终目标是科研路径规划工具，而不是人格标签工具；是博士适配反思系统，而不是博士天赋判定器；是开源心理测量实验项目，而不是伪科学测试网站。
