<%*
// ===== SBAR 草稿生成器 =====
// 使用：Cmd+Shift+S (建议绑定) 或 Cmd+T → 选 sbar
// 不写真实病案号/姓名；床号或代号即可

const bed = await tp.system.prompt("床号 / 代号", "X");
const hours = await tp.system.prompt("过去多少小时趋势在变坏", "4");
const main = await tp.system.prompt("S - 当前最主要的问题（一句话）", "NE 加量 + 乳酸上升 + 尿量下降");

const bg = await tp.system.prompt(
  "B - 背景一段话（基础病 / 入 ICU 原因 / 当前呼吸·循环·肾·感染源控）",
  "肺炎脓毒性休克 D3，AC 通气 FiO2 50% PEEP 8，NE 0.18，尿量 15 mL/h，美罗培南 D2",
  false,
  true
);

const shock = await tp.system.suggester(
  ["低容量", "分布性", "心源性", "阻塞性", "混合性", "呼吸衰竭进展", "AKI 进展", "其他"],
  ["低容量", "分布性", "心源性", "阻塞性", "混合性", "呼吸衰竭进展", "AKI 进展", "其他"],
  false,
  "A - 我判断更像哪一型"
);

const evidence = await tp.system.prompt(
  "A - 依据（POCUS / 趋势 / 反应性 / 耐受性）",
  "肺超 B 线增加，IVC 偏宽，VTI 对 PLR 无明显反应，考虑灌注失败合并液体耐受差"
);

const r = await tp.system.prompt(
  "R - 已做 / 准备 / 不改善等多久 / 想请上级做什么",
  "已复查血气+床旁超声；准备加用血管活性药；30 min 内不改善建议床旁评估升压策略与影像",
  false,
  true
);

const eval_time = await tp.system.suggester(
  ["现在", "30 分钟内", "1 小时内", "天亮前都可以"],
  ["现在", "30 分钟内", "1 小时内", "天亮前都可以"],
  false,
  "希望上级何时床旁评估"
);
-%>
## SBAR · <% bed %> 床 @ <% tp.date.now("MM-DD HH:mm") %>

**S（Situation）**：<% bed %> 床现在最主要的问题是 **<% main %>**，过去 **<% hours %> 小时**趋势在变坏。

**B（Background）**：
<% bg %>

**A（Assessment）**：我判断更像 **<% shock %>**，依据：
<% evidence %>

**R（Recommendation）**：
<% r %>

希望您 **<% eval_time %>** 床旁评估。

---
> *SBAR 草稿，仅供个人备忘 · 已规避病案号/姓名 · 复核后再向上级口述或写入病历*
