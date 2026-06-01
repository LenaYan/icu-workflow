---
template: references-style
deidentified: true
---

# 引用格式与标签体系

> **目的**：让所有病例分析、文献笔记、研究计划的引用风格统一，便于复用与审稿。

---

## 1. 行内引用

- 用方括号编号：`[N]`；多条并列：`[N][N]` 或 `[N, N]`
- **同一文献多次引用复用同一编号**（不重复加新号）
- 把 `[N]` 放在被支持的语义单元末尾（句号前），不要句首；不空格

✅ `…ISTH overt DIC ≥ 5 分明确诊断 [7]。`
✅ `…LMWH 优于 VKA 用于 CAT 长期抗凝 [4][8]。`
❌ `[4] LMWH 优于 VKA…`
❌ `…长期抗凝 [4] 。`（空格）

---

## 2. 参考文献条目格式

### 英文期刊论文
```
N. 一作 [et al.]. *标题*. 期刊 年;卷(期):页. [标签]
```
- 一作姓 + 名缩写。3 作及以上用 `et al.`
- 期刊用通行缩写（见 §5）
- 标题斜体
- 标签见 §3

**例**：
```
4. Lee AYY, et al. *LMWH vs coumarin for recurrent VTE in cancer (CLOT)*. NEJM. 2003;349(2):146-153. [RCT]
```

### 中文期刊论文
```
N. 一作, 等. 《标题》. 期刊. 年;卷(期):页. [标签]
```
**例**：
```
12. 张三, 等. 《颅内出血后重启抗血栓治疗的研究进展》. 中华神经科杂志. 2023;56(2):204-211. [综述]
```

### 指南 / 共识 / 立场文件
```
N. 组织. *指南名* (版本年). [指南] / [共识]
```
**例**：
```
3. 中国临床肿瘤学会 (CSCO). *肿瘤相关静脉血栓栓塞症预防与治疗指南* (2019). [指南]
8. NCCN. *Cancer-Associated VTE Disease, v3.2025*. [指南]
```

### 药品说明书
```
N. 药品名说明书. 监管机构, 修订年. [说明书]
```
**例**：
```
9. 利伐沙班片说明书. 国家药监局, 2025. [说明书]
```

### Cochrane / Meta
```
N. 一作, et al. *标题*. Cochrane Database Syst Rev. 年;期:文号. [Meta]
```

---

## 3. 标签体系（方括号末位）

| 标签 | 适用 | 例 |
|---|---|---|
| `[指南]` | 国家级 / 国际学会发布 | SSC、KDIGO、CSCO、NCCN、ESC |
| `[共识]` | 专家小组共识，证据等级低于指南 | 中国 XX 专家共识 |
| `[RCT]` | 随机对照试验 | CLOT、CARAVAGGIO、PROSEVA |
| `[Meta]` | 系统综述 / Meta-analysis | Cochrane review |
| `[综述]` | Narrative / 非系统综述 | NEJM Review、How I treat |
| `[队列]` | 前瞻 / 回顾队列研究 | observational cohort |
| `[病例]` | 病例报告 / 病例系列 | case report |
| `[说明书]` | 药品 / 器械说明书 | SmPC |
| `[基础]` | 机制 / 动物 / 体外研究 | preclinical |
| `[预印本]` | 未同行评议（preprint） | medRxiv、bioRxiv |

**证据等级直觉**：指南 > Meta > RCT > 队列 > 综述 > 病例 > 基础。临床决策时优先 RCT/指南，机制问题用综述/基础。

---

## 4. 何时引哪一类

| 场景 | 优先引 |
|---|---|
| 用药剂量、监测目标、给药方式 | 指南 + 说明书 |
| 替代方案对比 / 选哪个 | RCT + Meta |
| 病理生理、机制解释 | 综述 + 基础 |
| 罕见情景 / 灰区决策 | 共识 + 病例系列 |
| 新现象 / 尚无指南 | 队列 + 预印本（标注证据弱） |

---

## 5. 常用期刊缩写（ICU 高频）

| 全称 | 缩写 |
|---|---|
| New England Journal of Medicine | NEJM |
| Journal of the American Medical Association | JAMA |
| The Lancet | Lancet |
| The Lancet Respiratory Medicine | Lancet Respir Med |
| American Journal of Respiratory and Critical Care Medicine | AJRCCM |
| Critical Care Medicine | CCM |
| Intensive Care Medicine | ICM |
| Chest | Chest |
| Critical Care | Crit Care |
| Journal of Thrombosis and Haemostasis | J Thromb Haemost |
| Blood | Blood |
| British Journal of Haematology | Br J Haematol |
| Annals of Intensive Care | Ann Intensive Care |
| Resuscitation | Resuscitation |

---

## 6. 试验命名约定

- 引用关键试验首次出现时，用 `**TRIAL_NAME (Journal Year)**` 加粗
- 如 `**CLOT (NEJM 2003)**`、`**PROSEVA (NEJM 2013)**`、`**ARDSNet (NEJM 2000)**`
- 后续提及不必重复加粗
- 文末参考文献按正式条目格式收录

---

## 7. 避免

- ❌ 模糊引用："研究表明…"、"指南建议…"（不带 [N]）
- ❌ 把指南名称缩写当依据（如只写 "ISTH" 不指明 2015 vs 2024）
- ❌ 仅给 PubMed PMID / DOI 而无可读条目
- ❌ 同一证据在文中编两个号
- ❌ 引用预印本而不标注 `[预印本]`
