▋ writing-editor

• 這是「責任編輯」的流程與 Cursor skill，不是某個作者本人。

• 你拿到的是說明書：怎麼對焦、組骨架、一題一題問、作者主筆。語氣、讀者、正在寫哪篇，要你自己填進 `constitution.md`。

• 這份流程會持續改。新能力往 `skills/` 加，不要期待一次就做完。怎麼迭代見 `docs/iterate.md`。


▋ 別人怎麼開始用

• 1. 用 Cursor 打開這個資料夾（clone 或 fork 都可以）。

• 2. 複製 `constitution.template.md` 成 `constitution.md`，填你的讀者、輸出方式、語料放哪。這一步不做，責編不該裝熟。

• 3. 對話裡說「責任編輯」或 `/writing-editor`。

• 4. 有畫面就先講。責編給可講骨架，你再講，再收成你會說的話。需要才變成可貼出去的稿。

• 5. 進行中的篇目大綱放 `drafts/`。暫停時大綱裡要有「下次從哪一段繼續」。

• `instances/` 只是範例。不要把裡面的人、讀者、半成品稿當成你的。


▋ 別人日常怎麼運作

• 開一篇：把素材丟進去，說要開編輯會。

• 卡住：說「只要骨架」或「這段還要資料」。

• 一段講完：只鎖門口句，再進下一段。不要一次重寫全文。

• 收工：說存檔。下次打開同一個 `drafts/` 檔接著講。


▋ 別人怎麼更新（重點）

• 核心流程會改：`SKILL.md`、`skills/`、模板、說明。這些可以 `git pull`。

• 你的人不能被蓋掉：`constitution.md` 跟 `drafts/` 裡正在寫的大綱是你的。

• 更新前先看 `CHANGELOG.md` 跟 `VERSION`。

• 若 `git pull` 撞到 `constitution.md`，留你自己的，只收核心檔。

• 不要把你的 `constitution.md` 當成 PR 送回這個 repo 的主線，除非你明確要貢獻模板本身。


▋ 維護者怎麼持續加東西

• 共用新能力 → 加 `skills/<名稱>/SKILL.md`，登記 `skills/manifest.md`，改版本與 CHANGELOG。細節：`skills/README.md`、`docs/iterate.md`。

• 只有你自己要的路徑、語氣、讀者 → 只改你的 `constitution.md`。

• 改主循環（對焦／骨架／重講）→ 改根目錄 `SKILL.md`，並註明舊大綱還能不能用。


▋ 它會做／不會做

• 會：對焦、組可講骨架、查核補料、收成你會說的話、存大綱斷點、按 manifest 載入額外模組

• 不會：沒授權就代寫發布稿、假裝認識你、把別人的稿當你的人格


▋ 這個 repo 裡有什麼

• `SKILL.md`：主流程入口

• `constitution.template.md`：空白契約

• `constitution.md`：你填的契約（你的；更新核心時不要覆蓋）

• `skills/`：可插拔模組

• `drafts/`：進行中大綱

• `instances/`：別人填法的範例

• `docs/iterate.md`：怎麼迭代

• `VERSION`、`CHANGELOG.md`：改了什麼
