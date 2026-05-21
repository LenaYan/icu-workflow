<%*
// ===== 夜班整夜笔记骨架 =====
// 使用：Cmd+Shift+N (建议绑定)，建议在新建文件时触发
// 自动重命名为 "夜班 YYYY-MM-DD"

const date = tp.date.now("YYYY-MM-DD");
const shift_start = await tp.system.prompt("接班时间", tp.date.now("HH:mm"));
const beds = await tp.system.prompt("今晚重点盯哪几个床（逗号分隔）", "");
const worry = await tp.system.prompt("最担心今晚出什么事（一句话）", "");

// 拆分床号生成各床位卡
const bedList = beds.split(/[,，]/).map(s => s.trim()).filter(Boolean);
let bedBlocks = "";
for (const b of bedList) {
  bedBlocks += `\n### ${b} 床\n- **风险**：\n- **趋势**：\n- **触发阈值**：\n- **复评时间**：\n`;
}

// 自动重命名（如果是新文件）
try {
  await tp.file.rename(`夜班 ${date}`);
} catch (e) {}
-%>
# 夜班 · <% date %>（接班 <% shift_start %>）

> 接班 5 问 · 30 min 床旁脚本 · 每床触发阈值 · 处置后必复评

## 接班速记
- 重点床位：<% beds %>
- 最担心：<% worry %>

## 30 分钟床旁扫描
- [ ] **看屏幕**（只看趋势）：BP / 升压药 / HR / SpO₂ / FiO₂ / PEEP / RR / UO / T / RASS
- [ ] **看管路**：插管深度·固定 / 呼吸机管路冷凝 / CVC·A-line / 引流 / 导尿 / 泵速·剩余量
- [ ] **问护士**：今晚最担心 / 白天最不稳 / pending / 家属会诊
- [ ] **写阈值**：每个高危床 ≥ 1 条 "如果…就…"

## 接班 5 问回顾
1. 今晚最可能出事的 3 个床？分别可能出什么事？
2. 升压药剂量 + 6-12 h 趋势 + MAP 目标 + 灌注证据 + 反应性·耐受性？
3. 呼吸机：模式 / Vt(PBW) / Pplat / ΔP / PEEP / FiO₂ / 最近调参原因？
4. 乳酸·血气·尿量·电解质 — 趋势？
5. pending = 时间 + 责任人 + 触发阈值 + 升级对象？

## 各床触发阈值
<% bedBlocks %>
> 在每个床下方可用 **Cmd+Shift+R** 插入更详细的触发块；用 **Cmd+Shift+P** 写 7 行复评

## 复评日志

| 时间 | 床 | 动作 | 复评时间 | 结果 | 闭环？ |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

## 升级 / SBAR 通话记录
> 用 **Cmd+Shift+S** 生成 SBAR 草稿后粘贴到此处

## 交班给白班
- **处理过的**：
- **未闭环 pending**：
- **复评未完成**：
- **建议白班关注**：

---
> *本笔记仅供个人备忘 · 已规避病案号·姓名 · 任何写入 PDMS/HIS 的内容需复核*
