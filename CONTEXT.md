---
updated: 2026-10-11
change: mandatory-article-structure-gate
---

## 這個專案在幹嘛
把現有老魚專用的寫作助手 Agent，整理成其他作者也能自訂與使用的單一寫作助手。

## 目前討論到哪
已確認只保留一個面向使用者的寫作助手 Agent。`author-adaptive-writing-preferences` 已加入三層偏好流程：共用訪談協議、作者私人偏好、當篇文章語境。新 SR `mandatory-article-structure-gate` 再把破、例、感、觀設為每篇文章的必要內部關卡，並在查證前詢問作者是否要結合目前最新時事；作者不要時不抓新聞，作者要時逐題確認範圍、時間、來源和文章連結。四零件不固定四段，也不預設外顯標籤。

## 未解問題
- `mandatory-article-structure-gate` 的 8 個 Ambiguity 建議是否要補成更細的 Given/When/Then 例子；目前沒有 Critical 或 Warning。
- 新 SR 是否需要結構化 evidence 欄位，或先以 Markdown 保存即可。
- 社群平台帳號讀取受平台限制；目前只驗證讀不到時的貼上／匯出退路，尚未對真實帳號連線驗收。

## 下一步
完成 `author-adaptive-writing-preferences` 的 Spectra validation/analyze；通過後再進入 apply 實作。
