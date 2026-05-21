<%*
// ===== 触发阈值快速块 =====
// 使用：Cmd+Shift+R (建议绑定)
// 6 选 1 → 插入默认骨架 → 三处 cursor 跳位手动微调

const scenario = await tp.system.suggester(
  ["氧合下降", "低血压 / 升压加量", "乳酸不清", "少尿", "躁动 / 镇静变深", "pending 操作"],
  ["oxygen", "shock", "lactate", "oliguria", "sedation", "pending"],
  false,
  "选择触发场景"
);

const presets = {
  oxygen: {
    title: "氧合下降",
    signal: "FiO₂ 或 PEEP 需求 ↑、PaO₂/FiO₂ ↓、呼吸功 ↑、意识变差",
    reeval: "管路·气囊·分泌物 / 血气 / 肺超或 CXR / 鉴别气胸·肺不张·肺水肿·PE·感染",
    escalation: "通知上级；准备 HFNC/NIV 失败后的插管方案；严重低氧讨论俯卧位与肺保护策略"
  },
  shock: {
    title: "低血压 / 升压加量",
    signal: "MAP 低于个体目标、NE 持续上调、脉压变小、乳酸 ↑、尿量 ↓",
    reeval: "休克分型 / PLR + 小量液体挑战 + VTI / 心超·肺超·VExUS / 出血·感染源·心律",
    escalation: "反应性 + 耐受才补液；血管张力低优先升压药；疑心源/阻塞性早叫上级+专科"
  },
  lactate: {
    title: "乳酸不清",
    signal: "乳酸不降或反升，尤其合并升压药增加或尿量下降",
    reeval: "氧输送 / 灌注 / 感染源 / 出血·缺血 / 肝肾清除 / 药物·惊厥",
    escalation: "写明复查时间；明确源控·抗菌药·影像·外科介入阈值；不简单等同缺液"
  },
  oliguria: {
    title: "少尿",
    signal: "尿量持续下降或 < 0.5 mL/kg/h 趋势，合并肌酐 / K⁺ / 酸中毒恶化",
    reeval: "导尿管 / 入出量 / MAP·灌注 / VExUS·腹压 / 肾毒药 / 电解质 + 血气",
    escalation: "若高钾·难治酸中毒·容量过负荷·尿毒症并发症 → 提前通知肾科 / 上级评估 RRT"
  },
  sedation: {
    title: "躁动 / 镇静变深",
    signal: "RASS 偏离目标、突然躁动、谵妄或嗜睡",
    reeval: "ABC / 疼痛 / 血气 / 血糖·电解质 / 感染 / 撤药 / 药物蓄积",
    escalation: "先纠正生理问题再调镇静；不用单纯加镇静掩盖低氧·高 CO₂·休克"
  },
  pending: {
    title: "pending 操作",
    signal: "血气·影像·复查·电解质·换管·会诊未列时间点",
    reeval: "查医嘱 / 执行人 / 完成时间 / 结果回报路径",
    escalation: "每项 pending 写明：未完成由谁追踪、异常结果通知谁"
  }
};

const p = presets[scenario];
-%>
### 触发阈值 · <%- p.title %> @ <% tp.date.now("HH:mm") %>

- **触发信号**：<% p.signal %>
- **立刻复评**：<% p.reeval %>
- **预设升级动作**：<% p.escalation %>
- **本床个性化阈值**：<% tp.file.cursor(1) %>
- **本床通知对象**：<% tp.file.cursor(2) %>
- **下次复评时间**：<% tp.file.cursor(3) %>

