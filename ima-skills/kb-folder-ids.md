# ima 知识库文件夹 ID 对照

> 用途：通过 MCP `upload_file` / `import_urls` 上传文件时，传入 `folder_id` 可直接归档到对应子目录，避免落在知识库根目录。
> 目标库：**医学知识库**
> - openapi_knowledge_base_id（upload_file 等写入工具用）：`J7VJWjU_AhCpOXooNBpgPTnxq15tv7tglYGFSoH9kiM=`
> - cookie_knowledge_base_id（ask_knowledge_base 用）：`7514337728012128`

## 上传归档流程（每次上传前必走）

1. **定类别**：先看本地来源路径——`guidelines/_pdfs/<category>/` 下的文件归入同名子目录；不在该树下的按内容判断：NMPA 说明书 → `drug-labels`；剂量/给药参考 → `drug-reference`；国内指南共识 → `china-consensus`；国际指南/文献 → 按亚专业（sepsis、ARDS-ventilation、neuro-TBI、hemodynamics-fluids、kidney-AKI-CRRT、nutrition、transfusion-coagulation、sedation-delirium、infection-antimicrobials、general-ICU）
2. **查表取 `folder_id`**（下表），调 `upload_file` 时传入
3. **无匹配类别**：不要落根目录——先用 `AskUserQuestion` 问用户是否新建子目录（建议名称）；用户同意后 `python3 scripts/ima_kb_admin.py mkdir 7514337728012128 folder_7514873772640524 <名称>` 创建，**把新 folder_id 补进本文件下表**，再上传
4. 上传后可用 `python3 scripts/ima_kb_admin.py ls 7514337728012128 <folder_id>` 复核

## 根目录文件夹

| folder_id | 名称 |
|---|---|
| `folder_7514873772640524` | **指南/说明书/剂量参考**（本项目指南入库的主目录） |
| `folder_7514939883265559` | critical-care |
| `folder_7514940168478455` | respiratory |
| `folder_7514944434085492` | gastroenterology |
| `folder_7514944966754516` | nephrology |
| `folder_7514945612683982` | neurology |
| `folder_7514945826587854` | cardiology |
| `folder_7514946107610717` | neurosurgery |
| `folder_7515755700554477` | share |

## 指南/说明书/剂量参考 下的子文件夹（对应本地 `guidelines/_pdfs/` 分类）

| folder_id | 名称 |
|---|---|
| `folder_7514874703777786` | drug-labels（NMPA 说明书 MD） |
| `folder_7514874699582504` | drug-reference（CRRT 剂量等参考） |
| `folder_7514874745718988` | china-consensus（国内指南/共识 PDF） |
| `folder_7514874728939575` | hemodynamics-fluids |
| `folder_7514874674418329` | nutrition |
| `folder_7514874724748205` | transfusion-coagulation |
| `folder_7514874670221945` | sepsis |
| `folder_7514874741529880` | ARDS-ventilation |
| `folder_7514874749917376` | neuro-TBI |
| `folder_7514874695389520` | general-ICU |
| `folder_7514874691193458` | kidney-AKI-CRRT |
| `folder_7514874682806856` | sedation-delirium |
| `folder_7514874678614440` | infection-antimicrobials |

## 移动/整理已有条目

MCP 工具没有 move/delete 接口；批量整理用 `scripts/ima_kb_admin.py`（Cookie 认证，自动刷新 token）：

```bash
python3 scripts/ima_kb_admin.py kbs                      # 列知识库（名称 + cookie KB id）
python3 scripts/ima_kb_admin.py folders <kb_id>          # 列库根目录文件夹
python3 scripts/ima_kb_admin.py ls <kb_id> [folder_id]   # 列条目（默认根目录）
python3 scripts/ima_kb_admin.py mv <kb_id> <dst_folder_id> <media_id...>
python3 scripts/ima_kb_admin.py mv <kb_id> <dst_folder_id> --all-from <src_folder_id|root>
python3 scripts/ima_kb_admin.py mkdir <kb_id> <parent_folder_id|root> <名称>
python3 scripts/ima_kb_admin.py rm <kb_id> <media_id...>  # 删除（不可逆，谨慎）
```

底层接口：`knowledge_tab_reader/get_knowledge_list`（列目录）、`knowledge_tab_sse/move_knowledge`（移动，SSE）、`knowledge_tab_writer/create_folder` / `del_knowledge`。

## 附：ICU病例档案库（病例归档专用，与上面"医学知识库"是两个库）

> 目标库：**ICU病例档案**（自有私有库，脱敏病例分析归档处；红线见 `kb-ingest` skill §8——仅限脱敏后病例、且只入本库）
> - openapi_knowledge_base_id（upload_file 等写入工具用）：`CrPZPct-kywth1T9YIT7C1dC-JI_O06fRiVcrQ7OyHs=`
> - cookie_knowledge_base_id（ask_knowledge_base 用）：`7515792857921919`

| folder_id | 名称 |
|---|---|
| `folder_7516099784486279` | HTG-AP |
| `folder_7516099776095883` | sepsis |
| `folder_7516099776097272` | ARDS |
| `folder_7516099776096326` | neuro-critical |
| `folder_7516099780309448` | cardiogenic-shock |
| `folder_7516099780290279` | trauma-postop |
| `folder_7516099784503793` | kidney-AKI-CRRT |
| `folder_7516099784484253` | obstetric-critical |
| `folder_7516099788679612` | coagulation-DIC |
| `folder_7516099788679163` | metabolic-endocrine |
