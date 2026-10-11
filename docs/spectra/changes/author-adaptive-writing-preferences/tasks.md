## 1. Preference interview contract

- [x] 1.1 實作 **First-use preference onboarding SHALL be optional and resumable**：新作者先收到一題開放問題，可略過並進入 neutral mode；用 `tests/writing-assistant-scenarios.md` 的新作者與略過情境驗證。
- [x] 1.2 實作 **Preference interviewing SHALL ask one open question at a time**：訪談可中斷續接、不重問已回答內容，並驗證 **The preference model SHALL separate shared protocol, private profile, and article context** 的未完成狀態；用中斷訪談與修正假設情境驗證。
- [x] 1.3 實作 **Sample-rewrite calibration SHALL use the author's correction as evidence**：沒有樣本時用當次主題產生短段落，作者可修改並得到偏好摘要與新示範；用校準與拒絕錯誤推論情境驗證。

## 2. Three-layer preference and context boundary

- [x] 2.1 依 **The preference model SHALL separate shared protocol, private profile, and article context** 定義三層資料責任；同時落實 design 的 **Goals / Non-Goals** 與 **Scope boundaries**，用內容審查和 `spectra analyze author-adaptive-writing-preferences` 驗證。
- [x] 2.2 依 design 的 **Data shape** 擴充私人 Markdown 設定，保存已確認的文體、可重用判準、平台差異、證據與限制；驗證既有設定可讀，缺少欄位不自行補造。
- [x] 2.3 依 **Decision: Keep style and philosophy private, keep context local to the article**，Prevent article-specific people, events, numbers, scenes, sources, and conclusions from entering the private profile without explicit promotion；驗證 anti-contamination 情境與 `scripts/check-contamination.py`。
- [x] 2.4 實作 **The profile SHALL be reviewable and explicitly consented before persistence**，並保持每位作者的設定位於 repo 外；用雙作者隔離、路徑安全、同意、拒絕、查看、更新與刪除情境驗證。

## 3. Reuse and update behavior

- [x] 3.1 實作 **Confirmed preferences SHALL be reused and updated only by author direction** 的載入行為：每篇新文章讀取已確認設定，不重做完整 onboarding，只問缺少的文章問題；用既有設定情境驗證。
- [x] 3.2 實作 **The profile SHALL be reviewable and explicitly consented before persistence** 的更新關卡：替換既有偏好前先展示 proposed replacement，未同意時保留原檔；用更新同意與拒絕情境驗證。

## 4. Documentation and regression verification

- [x] 4.1 依 design 的 **Decision: Use correction-led onboarding instead of a fixed style questionnaire** 與 **Decision: Apply confirmed profiles once per new article, not re-interview every time**，把 neutral mode、試寫校準、review card、失敗退路寫入 Skill 和使用說明；驗證內容沒有任何作者專屬預設。
- [x] 4.2 依 design 的 **Non-Goals** 與 **Acceptance criteria** 擴充 `tests/writing-assistant-scenarios.md`：加入六年級白話、直接對讀者、明確對比、動作與物件、自然對話、拒絕生硬旁白等「作者自行校準」情境；逐項確認有可觀察的通過條件。
- [x] 4.3 依 design 的 **Implementation Contract**、**Observable behavior** 和 **Failure behavior** 執行 `spectra validate author-adaptive-writing-preferences`、`spectra analyze author-adaptive-writing-preferences`、YAML/frontmatter 檢查與完整情境檢視；記錄實際輸出後才提交。
