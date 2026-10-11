## 1. Required structure gate

- [x] 1.1 實作 **Every article SHALL pass a four-part structure gate before full drafting**：在訪談後、大綱前建立 `破`、`例`、`感`、`觀` 內部地圖；用完整地圖情境驗證。
- [x] 1.2 實作 **The four parts SHALL describe reader tasks rather than fixed public headings**：允許零件調整順序、合併段落，預設不把四個標籤輸出到文章；用合併段落和作者要求外顯標籤情境驗證。
- [x] 1.3 實作 **Missing structure material SHALL return to one-question interviewing**，落實 design 的 **Decision: Missing material returns to interview instead of invention**：任一零件缺料就停止全文生成，一題一問補齊，禁止捏造人物、對話、動機、數字和結論；用缺例和缺觀情境驗證。
- [x] 1.4 實作 **The structure map SHALL be confirmed before the outline is approved**：大綱審閱時展示四零件地圖，作者可修改後再進入完整初稿；用作者修正地圖和過早要求全文情境驗證。
- [x] 1.5 實作 **Current-news integration SHALL be explicitly confirmed before research**：查證前先問是否要結合目前最新時事；作者拒絕時不抓新聞，作者同意時逐題確認範圍、時間和連結觀點；用拒絕、同意和範圍不清情境驗證。

## 2. Skill and workflow integration

- [x] 2.1 將必要關卡寫入 `SKILL.md`：完整文章流程必須在訪談後先完成破例感觀地圖，再研究、定大綱和起草；依 design 的 **Goals / Non-Goals** 保留「不是固定四段、不是作者文風」邊界；用核心流程契約檢查驗證。
- [x] 2.2 將 `po-li-gan-guan` 設為文章寫作必載模組，並保留「不是固定四段、不是作者文風」的邊界；用 `skills/manifest.md` 和 `skills/po-li-gan-guan/SKILL.md` 內容審查驗證。
- [x] 2.3 保留當篇語境隔離和作者私人設定邊界，讓四零件只能使用當篇素材或清楚標示的外部／假設來源；用防污染情境和 `scripts/check-contamination.py` 驗證。

## 3. Scenarios and verification

- [x] 3.1 在 `tests/writing-assistant-scenarios.md` 加入破例感觀四零件完整、缺料退回、公開不外顯標籤、作者要求外顯標籤、作者修正結構、過早要求全文，以及時事結合拒絕／同意／範圍不清情境；逐項確認每個情境有可觀察結果。
- [x] 3.2 依 design 的 **Observable behavior**、**Data shape**、**Failure behavior**、**Acceptance criteria** 和 **Scope boundaries**，執行 `spectra validate mandatory-article-structure-gate`、`spectra analyze mandatory-article-structure-gate`、YAML/frontmatter、契約詞和防污染檢查；記錄實際輸出後才提交。
