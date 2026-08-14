▋ 迭代原則

• 改「怎麼當責編」→ 改核心檔（`SKILL.md`、`skills/`、模板）

• 改「我是誰、寫給誰」→ 只改你的 `constitution.md`，不要開新 skill 硬塞人格

• 先試跑一篇再升版本。沒驗證過的模組不要寫進 manifest 當預設載入


▋ 兩種檔，不要混

• 核心（大家一起更新）：`SKILL.md`、`skills/`、`constitution.template.md`、`docs/`、`README.md`、`VERSION`、`CHANGELOG.md`

• 個人（更新時要保住）：`constitution.md`、`drafts/` 裡你正在寫的大綱


▋ 加功能的固定步驟

• 1. 判斷：這是所有作者都該有的能力，還是只有你要？只有你要 → 寫進自己的 constitution「可選零件路徑」，不要進 `skills/`

• 2. 若是共用能力：依 `skills/README.md` 加模組並登記 manifest

• 3. 若是改主循環：改根目錄 `SKILL.md`，並在 CHANGELOG 標「作者要不要重填契約」

• 4.  bump `VERSION`

• 5. 寫 `CHANGELOG.md`

• 6. 拿進行中的一篇走一次循環

• 7. push。另一台 `git pull` 後先看 CHANGELOG


▋ 版本怎麼加

• 0.0.x 文件、範例、錯字

• 0.x.0 新模組、新模式、主循環有加步驟

• x.0.0 舊大綱／舊契約可能不能直接用，README 要寫遷移


▋ 另一台電腦

• `git pull`

• 讀 `CHANGELOG.md`

• `constitution.md` 若有衝突，留你自己那份，只收核心檔
