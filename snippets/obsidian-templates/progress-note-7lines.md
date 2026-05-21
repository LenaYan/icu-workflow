<%*
// ===== 夜班高危复评 · 7 行病程记录 =====
// 使用：Cmd+Shift+P (建议绑定)
// 7 个多行输入，留空可后续手填

const bed = await tp.system.prompt("床号 / 代号", "X");

const risk = await tp.system.prompt(
  "1. 当前主要风险（氧合/通气 ; 循环/灌注 ; 肾/液体 ; 意识/镇静）",
  "",
  false,
  true
);

const trend = await tp.system.prompt(
  "2. 趋势（MAP / 血管活性药 / 乳酸 / 尿量 / P/F / PaCO2·pH）",
  "",
  false,
  true
);

const bedside = await tp.system.prompt(
  "3. 床旁评估（气道·管路 / 肺超 / 心超·VExUS / 导尿·引流）",
  "",
  false,
  true
);

const judgment = await tp.system.prompt(
  "4. 最可能问题 + 主要鉴别",
  "",
  false,
  true
);

const action = await tp.system.prompt(
  "5. 处理（已完成 / 待完成）",
  "",
  false,
  true
);

const threshold = await tp.system.prompt(
  "6. 触发阈值（若 X，则 Y，并通知 Z）",
  "",
  false,
  true
);

const reeval = await tp.system.prompt(
  "7. 复评时间 + 结果回报路径",
  "",
  false,
  true
);
-%>
## 夜班复评 · <% bed %> 床 @ <% tp.date.now("MM-DD HH:mm") %>

**1. 当前主要风险**
<% risk %>

**2. 趋势**
<% trend %>

**3. 床旁评估**
<% bedside %>

**4. 判断**
<% judgment %>

**5. 处理**
<% action %>

**6. 触发阈值**
<% threshold %>

**7. 复评**
<% reeval %>

---
> *草稿，复核后再录入 PDMS/HIS · 不含病案号*
