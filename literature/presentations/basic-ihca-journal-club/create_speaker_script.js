import fs from "node:fs";
import path from "node:path";
import {
  AlignmentType, Document, Footer, Header, HeadingLevel, ImportedXmlComponent,
  Packer, PageNumber, Paragraph, TextRun, convertInchesToTwip,
} from "docx";

const outputPath = process.argv[2];
if (!outputPath) throw new Error("Usage: node create_speaker_script.js /absolute/path/output.docx");

const T = String.raw;
const palette = { dark: "27231F", primary: "684765", accent: "C9828B", light: "9B9489", fill: "F2EDE2" };
const font = { ascii: "Times New Roman", hAnsi: "Times New Roman", cs: "Times New Roman", eastAsia: "SimSun" };

const run = (text, options = {}) => new TextRun({ text, font, size: 24, ...options });
const para = (children, options = {}) => new Paragraph({
  spacing: { after: 140, line: 300 }, ...options,
  children: Array.isArray(children) ? children : [children],
});
const body = (text, options = {}) => para(run(text), { indent: { firstLine: convertInchesToTwip(0.33) }, ...options });
const h1 = (text) => para(run(text, { bold: true, size: 30, color: palette.primary }), {
  heading: HeadingLevel.HEADING_1, spacing: { before: 280, after: 140 } });
const h2 = (text) => para(run(text, { bold: true, size: 26, color: palette.dark }), {
  heading: HeadingLevel.HEADING_2, spacing: { before: 220, after: 100 } });
const note = (text) => para(run(text, { italics: true, size: 21, color: palette.light }));

const opening = [
  T`各位老师、同事，大家好。今天由我来做文献分享，题目是发表在 Circulation 2026 年最新一期的原创文章——《中国院内心脏骤停的发病率、救治流程与预后：一项多中心前瞻性注册研究》，也就是 BASIC-IHCA 注册研究的主要结果。`,
  T`选这篇文章有三个理由：第一，它是迄今为止中国最大规模、覆盖 29 个省份的院内心脏骤停注册研究，数据质量有 Utstein 标准化模板和严格质控背书；第二，它同时报告了"疾病负担、救治流程、临床结局"三个维度，而且把复苏后救治的短板量化得非常清楚，对我们科室的质量改进有直接参考价值；第三，它提出的系统层面改进建议——结构化响应系统、重症资源优化、预立医疗照护计划——正是我们日常工作中可以落地的方向。`,
  T`整个分享预计四十五分钟左右，分为四个部分：背景与设计、研究结果、难点知识解析、讨论与启示。其中第三部分是我额外补充的，结合指南、教材和专家共识，把文里几个不太好消化的知识点给大家拆开讲一讲。`,
];

const slides = [
  { n: 1, t: "封面", dur: "约 1 分钟", paras: [
    T`首先介绍文献出处：通讯作者为山东大学齐鲁医院陈玉国教授、徐峰教授和中日友好医院张国强教授，第一作者包括王春义、郑佳琪、郑文、杨可慧等，协作组规模很大。这是开放获取文章，DOI 在屏幕左下角，大家可以会后下载原文。`,
  ]},
  { n: 2, t: "目录", dur: "约 30 秒", paras: [
    T`今天的内容分四个部分。前两部分是文章本身：背景设计和研究结果；第三部分是我从知识库补充的难点解析，约占三分之一时间；最后结合我们的 ICU 实践谈启示。`,
  ]},
  { n: 3, t: "章节页 01 · 研究背景与设计", dur: "约 20 秒", paras: [
    T`先回答一个问题：为什么中国需要一项全国性的 IHCA 注册研究？`,
  ]},
  { n: 4, t: "研究背景", dur: "约 3 分钟", paras: [
    T`院内心脏骤停是住院患者死亡和神经功能致残的重要原因。过去二十年，高收入国家靠大型注册研究持续改进，出院存活率已经到了百分之十八到三十五这个区间。而中低收入国家的证据基本停留在单中心、单城市层面，没法做全球基准比较。`,
    T`中国此前只有一项有代表性的研究：2014 年北京 12 家医院，报告发生率千分之十七点五、出院存活百分之九点一。但它只覆盖首都医院，流程记录很有限。BASIC-IHCA 就是为了填补这个空白而建立的，用标准化的 Utstein 模板做全国多中心前瞻性注册。`,
    T`请大家在心里带着三个问题听后面的结果：负担有多重？救治流程和国际差距在哪？系统上能怎么改？`,
  ]},
  { n: 5, t: "BASIC-IHCA 研究设计", dur: "约 3 分钟", paras: [
    T`设计上几个关键点：全国七大地理区域选点，城市选三级医院、农村选县级医院；2019 年 7 月到 2020 年 12 月连续入组；同一住院期多次骤停只记第一次，排除院外骤停。质控上是培训过的调查员用专用电子采集系统，预定义核查规则、中心统计验证、每三到六个月现场审计，伦理上豁免知情同意。`,
    T`统计上有两点值得注意：发生率按 Utstein 口径只算"接受 CPR 的人"；主要模型是多变量混合效应 logistic 回归，把医院作为随机截距——这比单纯把医院当固定效应更合理。`,
    T`筛选流程看下面：识别三万两千五百多例成人 IHCA，其中百分之五十四点四接受了 CPR，最终纳入一万七千六百零二例。注意这个 54.4% 的 CPR 尝试率，后面讲 DNACPR 文化时还会回到这个数字。`,
  ]},
  { n: 6, t: "研究人群与基线特征", dur: "约 2.5 分钟", paras: [
    T`基线特征五个数字：一万七千六百零二例，中位年龄 66 岁，男性 65.5%，初始可电击心律只有 13.5%，心源病因 37.3%。两个非常重要的背景数字：目击率 98.1%、监护率 95.5%——这解释了后面"复苏启动非常快"的现象：ICU 和急诊密切观察，病房多人同住、家属在场、巡视频繁。`,
    T`地点分布上 ICU 占 40.2%，远高于欧洲的 9% 到 17%，提示我们的骤停患者共病负担更重。发生率千分之四点一，按全国年住院 2.27 亿人次推算，每年约 93 万例成人 IHCA——这个数字请大家记住，它是所有系统改进的"分母背景"。`,
  ]},
  { n: 7, t: "章节页 02 · 研究结果", dur: "约 15 秒", paras: [
    T`接下来是核心结果：流程、复苏后救治、结局和影响因素。`,
  ]},
  { n: 8, t: "复苏期救治流程", dur: "约 3 分钟", paras: [
    T`复苏期可以用一句话概括：启动非常快，环节基本达标，但结构上依赖"人肉响应"。95.9% 的患者一分钟内启动按压或除颤；可电击心律及时除颤率 71.4%，不可电击心律及时肾上腺素率 84.4%，都达到国际基准。`,
    T`但缺口也很清楚：可电击心律里 16.2% 全程没除颤，普通病房的及时除颤率最低——除颤仪可及性问题；全国 40 家医院里只有 3 家有结构化快速反应系统，这 3 家病房骤停的团队激活率 70.7%。我们的现行模式是 ICU、急诊就地抢救，病房靠病区人员起步、电话呼叫支援。CPR 中位时长 30 分钟，拿到持续 ROSC 的只要 11 分钟。`,
  ]},
  { n: 9, t: "复苏后救治缺口", dur: "约 3 分钟", paras: [
    T`这是全文我最想让大家记住的一页。持续 ROSC 的 6200 例患者里：任何温度控制只有 3.6%，规范 TTM 只有 0.8%；冠脉造影 5.2%，PCI 4.3%。对照高收入国家：温度控制 6% 到 10%，造影 17.7% 到 31.2%。`,
    T`注意一个细节：可电击心律患者接受造影和 PCI 的比例明显更高，15.6% 对 1.8%。这说明不是"没有这个意识"，而是资源可及性问题——ICU 床位、导管室、高级心脏照护的整体短缺，让指南推荐的复苏后干预落不了地。`,
  ]},
  { n: 10, t: "临床结局", dur: "约 2.5 分钟", paras: [
    T`结局呈漏斗式递减：任何 ROSC 40.9%，持续 ROSC 35.2%，然后陡降到 30 天存活 9.1%，神经功能良好 7.1%，12 个月存活 6.1%。持续 ROSC 处于国际范围下限，30 天存活远低于高收入国家。`,
    T`但有半句话同样重要：能出院的人，长期预后不差——出院者 6 个月存活 72.2%、一年存活 66.8%，和国际持平。也就是说死亡高度集中在骤停后早期，ROSC 之后的复苏后救治阶段是损耗最大的环节。单把反应时间做得更快，救不了这个漏斗的"脖子"。`,
  ]},
  { n: 11, t: "初始心律与预后", dur: "约 2.5 分钟", paras: [
    T`初始心律是最大的预后分水岭。可电击心律占 13.5%，低于国际的 17% 到 27%。可电击心律组：持续 ROSC 63.2%，30 天存活 34.0%；不可电击组分别只有 30.9% 和 5.3%。多变量模型里可电击心律的优势比 6.39，是最强的单一有利因素。机理层面为什么差这么多，第 16 页会展开。`,
  ]},
  { n: 12, t: "多因素回归", dur: "约 2 分钟", paras: [
    T`多变量模型其他结果快速过一遍：年轻、骤停发生在手术室/导管室/ICU、心源病因有利；低血压休克、肿瘤、卒中、肝肾功能不全不利。`,
    T`请特别看两个"反常"数字：骤停前已建立高级气道 aOR 0.58、已置 IABP aOR 0.41。这两个不是"插管有害""IABP 有害"，而是病情严重度标志——需要这些支持的患者本身就快不行了。读注册研究回归结果时要区分"干预效应"和"严重程度代理变量"。`,
  ]},
  { n: 13, t: "亚组分析", dur: "约 1.5 分钟", paras: [
    T`亚组两点：医院等级与急性期结局独立相关——三级医院 ROSC 和 30 天存活更好，但与神经和长期结局无关，再次提示"急性期能力"和"复苏后链条"是两件事。COVID-19 三时期分析：暴发期可电击心律和心源病因更少、ROSC 更低，但存活和神经预后没有显著差异，说明研究结论不太可能是疫情假象。`,
  ]},
  { n: 14, t: "章节页 03 · 难点知识解析", dur: "约 30 秒", paras: [
    T`下面这部分是知识库补充内容，我把文中最值得展开的概念分成五块：核心定义、复苏期技术、复苏后综合征与 TTM、神经预后与 ECPR、以及快速反应系统和 DNACPR 这两个制度性话题。`,
  ]},
  { n: 15, t: "Utstein 模板与核心定义", dur: "约 3 分钟", paras: [
    T`Utstein 模板是 1991 年起源的国际统一报告标准，目的只有一个：让不同国家的数据可比较。它定义了四块内容：患者特征、事件变量、救治流程、结局。本文的"及时除颤 2 分钟""及时肾上腺素 5 分钟""持续 ROSC 20 分钟"都来自这个体系。`,
    T`ROSC 的床旁判定要点：可触及脉搏血压、动脉波形恢复，呼气末二氧化碳突然升高是最早信号——所以我们抢救车上配 ETCO₂ 监测很有价值。CPC 分级 1 到 5 级，1 是良好、2 是轻度残疾、3 重度、4 植物状态、5 脑死亡；本文把 1 到 2 级定义为神经功能预后良好，这是国际通用标准。`,
  ]},
  { n: 16, t: "复苏期关键技术", dur: "约 4 分钟", paras: [
    T`可电击和不可电击心律的本质区别：可电击心律是"有折返环路、可被电击终止"，所以电除颤是确定性治疗，每延迟一分钟存活率降 7% 到 10%；而不可电击心律没有可被电击终止的节律，除颤无效，只能靠按压加药物。这就是两组预后六倍差距的病理生理基础。`,
    T`2025 版 AHA 指南对按压的要求：频率 100 到 120，深度 5 到 6 厘米，按压分数至少 80%，中断小于 10 秒，每两分钟换人。除颤用双相波 120 到 200 焦，默认 200，单次电击、电击后立即按压。肾上腺素 1 毫克静注每三到五分钟，不可电击心律要尽早给、可电击心律首次除颤失败后给；新版强调静脉优先。对照本文数据，我们的及时除颤率和及时肾上腺素率其实不差，差在设备可及性和按压质量的客观监测。`,
  ]},
  { n: 17, t: "复苏后综合征与 TTM", dur: "约 4 分钟", paras: [
    T`复苏后综合征 PCAS 是 ILCOR 2008 年命名的概念，四个成分：脑损伤——缺血再灌注的"双重打击"，决定神经预后；心肌功能障碍——心肌顿抑；全身缺血再灌注损伤——内皮损伤、无复流、可走向 MODS；还有未纠正的原发病因。ROSC 到出院之间 26 个百分点的落差，主要就消耗在这里。`,
    T`TTM 方案要点：ROSC 后昏迷者无论初始心律都做；中国共识 32 到 36 度选一个恒定温度，维持至少 24 小时，复温每小时 0.25 度，复温后 72 小时内避免发热反弹；2025 版 AHA 放宽到 32 到 37.5 度至少 36 小时，理念核心是积极防发热。寒战用丙泊酚、右美托咪定管理。对照本文 0.8% 的实施率——这是指南推荐和低资源现实之间最大的鸿沟，也是我们科室最可行的改进点。`,
  ]},
  { n: 18, t: "神经预后评估与 ECPR", dur: "约 3 分钟", paras: [
    T`神经预后强调多模态：EEG 看恶性模式；体感诱发电位双侧 N20 消失；NSE 48 到 72 小时大于 60 预测不良预后；S100B 特异高但敏感性太低，指南不推荐。原则是 ROSC 或复温后至少 72 小时再评估、多手段联合、避免自我实现预言——不要因为一个指标就过早谈撤治。`,
    T`ECPR 的适应证共识：70 岁以下、目击骤停加旁观者按压、无灌注时间小于 5 分钟、初始可电击心律、可逆病因、常规 CPR 20 分钟无效。本文 ECPR 只有 55 例。ECPR 在院内心脏骤停中的获益证据比院外更一致，但对组织化程度要求极高，不是买个 ECMO 就能开展的。`,
  ]},
  { n: 19, t: "RRT 与 DNACPR", dur: "约 3 分钟", paras: [
    T`制度层面两个短板。第一，快速反应系统：它的定位是"在骤停之前行动"。中国共识给了三级架构——科室、片区十分钟到达、院级；启动标准可参考 MEWS 评分，五分以上高危。美国 SCCM 2023 是指南级强推荐。我们 40 家医院里只有 3 家有，这就是普通病房除颤慢的根子。`,
    T`第二，DNACPR。它是有法律效力的医学命令，伦理依据是患者自主权加不伤害原则；患者意愿不明时必须按常规复苏。中国的问题是正式 DNACPR 很少、家属决策占主导，这造成双向偏倚：家属不放弃，分母里多了无效复苏；费用和预后顾虑，又让一部分本可救治的人过早撤治。这也是中国存活率不能和西方注册研究直接比较的原因。改进方向是文化适配的预立医疗照护计划。`,
  ]},
  { n: 20, t: "章节页 04 · 讨论与启示", dur: "约 15 秒", paras: [ T`最后回到那三个研究问题，总结并落到我们科室。` ]},
  { n: 21, t: "主要结论", dur: "约 2 分钟", paras: [
    T`六条结论：负担重，每年约 93 万例；反应快但存活率低，9.1% 对 18.4 到 35.6；复苏后缺口最大；死亡集中在骤停后早期，出院者预后不差；系统与文化因素塑造数字；改进路径是结构化响应系统、重症资源优化和文化适配的预立照护计划。原文有一句话我放在这里：改善存活，除了快速初始反应，更需要复苏后重症救治和结构化响应系统。`,
  ]},
  { n: 22, t: "局限性", dur: "约 1.5 分钟", paras: [
    T`局限性三点：一是代表性，城市为主、非概率抽样；二是没有按压质量的客观数据，CPR 质量对存活的影响没法评估；三是与疫情重叠，虽然三时期分析显示主要结论稳健。我个人补充一条：DNACPR 文化差异让跨国比较有固有偏倚，大家引用数据时要小心。`,
  ]},
  { n: 23, t: "对 ICU 实践的启示", dur: "约 3 分钟", paras: [
    T`落到我们科室，六条行动建议：第一，补齐病房骤停短板，推动 RRT 建设和除颤仪可及；第二，建立复苏后管理 bundle——ROSC 后尽早 TTM、目标血压 65 以上、氧合滴定、冠脉评估；第三，病因导向的冠脉策略，STEMI 或血流动力学不稳的两小时内造影，稳定的非 ST 段抬高者按 2025 版新推荐不再常规紧急造影；第四，把按压质量纳入质控，上反馈装置和 ETCO₂ 监测，对照复苏中心二十项质控指标；第五，推动 DNACPR 和预立照护的文化建设；第六，用 Utstein 模板建科室自己的骤停登记，让改进可测量。`,
  ]},
  { n: 24, t: "参考文献", dur: "约 20 秒", paras: [ T`参考文献列了原文核心引用和本次知识库补充的来源，不一一念了，会后发给大家。` ]},
  { n: 25, t: "结束页", dur: "约 1 分钟", paras: [
    T`最后用一句话收个尾：复苏成功不止于 ROSC——结构化响应系统和复苏后重症救治体系，才决定患者最终能不能活着出院、带着好的神经功能出院。今天的分享就到这里，谢谢大家，欢迎讨论。`,
  ]},
];

const qa = [
  { q: T`为什么 2014 年北京研究发生率千分之十七点五，本文只有千分之四点一？`,
    a: T`主要是口径不同：北京研究纳入"所有骤停事件"，本文按 Utstein 口径只统计"接受 CPR 者"。再加上 DNACPR 使用差异、医院构成不同，两个数字不能直接比较。这正是 Utstein 模板存在的意义。` },
  { q: T`TTM 实施率只有 0.8%，是否说明 TTM 在中国"不该做"？`,
    a: T`不能这样推。低实施率反映的是资源与流程问题——镇静寒战管理人力、监测条件、ICU 床位，而不是疗法无效。指南对 ROSC 后昏迷者的推荐没有变。合理的策略是从"积极防发热"做起，逐步建立 TTM 能力。` },
  { q: T`数据来自 2019–2020 年，对 2026 年的今天还有参考价值吗？`,
    a: T`这篇文章的价值恰恰在于它是"基线调查"——告诉我们系统缺口在哪里。治疗手段这几年变化不大，而系统性短板（RRT 覆盖、复苏后干预可及性、DNACPR 文化）改变更慢，所以结论仍然成立，甚至更需要更新数据来评估改进效果。` },
  { q: T`骤停前已建立高级气道 aOR 0.58，是不是说明插管反而有害？`,
    a: T`这是典型的混杂：需要提前插管的患者本身就是病情最重的群体，高级气道是严重程度标志而不是病因。注册研究的回归只能控制已测量变量，不能替代随机试验回答因果问题。` },
  { q: T`对我们科室，最优先做的一件事是什么？`,
    a: T`如果只选一件：ROSC 后的复苏后管理 bundle 落地——TTM 或至少积极防发热、血流动力学与氧合目标化、72 小时后多模态神经预后评估。因为它不依赖大规模基建，收益最直接，而且能带动团队对骤停后管理的整体重视。` },
];

const xmlEscape = (v) => String(v).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
const toc = (entries) => {
  const cached = entries.map(({ title, level, page }) => {
    const indent = Math.max(0, level - 1) * 360;
    return `<w:p><w:pPr><w:pStyle w:val="TOC${level}"/><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9000"/></w:tabs><w:ind w:left="${indent}"/></w:pPr><w:r><w:t>${xmlEscape(title)}</w:t></w:r><w:r><w:tab/></w:r><w:r><w:t>${xmlEscape(page)}</w:t></w:r></w:p>`;
  }).join("");
  return ImportedXmlComponent.fromXmlString(`<w:sdt xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:sdtPr><w:alias w:val="目录"/></w:sdtPr><w:sdtContent><w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText><w:fldChar w:fldCharType="separate"/></w:r></w:p>${cached}<w:p><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:sdtContent></w:sdt>`).root[0];
};

const tocEntries = [
  { title: T`开场白`, level: 1, page: 1 },
  ...slides.map((s) => ({ title: T`第 ${s.n} 页｜${s.t}`, level: 2, page: s.n + 2 })),
  { title: T`讨论环节预设问答`, level: 1, page: 28 },
];

const children = [];
children.push(para(run(T`《中国院内心脏骤停的发病率、救治流程与预后》`, { bold: true, size: 34, color: palette.dark }), {
  heading: HeadingLevel.TITLE, alignment: AlignmentType.CENTER, spacing: { before: 480, after: 200 } }));
children.push(para(run(T`BASIC-IHCA 注册研究（Circulation 2026）文献分享讲稿`, { size: 26, color: palette.primary }), { alignment: AlignmentType.CENTER, spacing: { after: 120 } }));
children.push(para(run(T`配套 PPT：basic-ihca-journal-club（25 页）　｜　建议总时长：约 45 分钟`, { size: 21, color: palette.light }), { alignment: AlignmentType.CENTER, spacing: { after: 480 } }));
children.push(h1(T`目录`));
children.push(note(T`右键目录，选择“更新域”可刷新页码。`));
children.push(toc(tocEntries));

children.push(h1(T`开场白`));
for (const t of opening) children.push(body(t));

for (const s of slides) {
  children.push(h2(T`第 ${s.n} 页｜${s.t}`));
  children.push(note(T`【建议时长 ${s.dur}】`));
  for (const t of s.paras) children.push(body(t));
}

children.push(h1(T`讨论环节预设问答`));
for (const { q, a } of qa) {
  children.push(para([run(T`Q：`, { bold: true, color: palette.primary }), run(q)], { spacing: { before: 120, after: 60 } }));
  children.push(body(T`A：${a}`));
}

const doc = new Document({
  features: { updateFields: true },
  styles: {
    paragraphStyles: [
      { id: "TOC1", name: "TOC 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font, size: 24, bold: true, color: palette.primary } },
      { id: "TOC2", name: "TOC 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font, size: 22, color: palette.dark } },
    ],
  },
  sections: [{
    properties: { page: { margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    headers: { default: new Header({ children: [para(run(T`BASIC-IHCA 文献分享讲稿`, { size: 18, color: palette.light }), { alignment: AlignmentType.CENTER })] }) },
    footers: { default: new Footer({ children: [para(new TextRun({ children: [PageNumber.CURRENT], font, size: 18 }), { alignment: AlignmentType.CENTER })] }) },
    children,
  }],
});

fs.writeFileSync(outputPath, await Packer.toBuffer(doc));
