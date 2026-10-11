---
updated: 2026-10-11
change: author-adaptive-writing-preferences
---

## 這個專案在幹嘛
把現有老魚專用的寫作助手 Agent，整理成其他作者也能自訂與使用的單一寫作助手。

## 目前討論到哪
已確認只保留一個面向使用者的寫作助手 Agent。新 SR `author-adaptive-writing-preferences` 以三層設計補強通用流程：共用訪談協議、作者私人偏好、當篇文章語境。新作者第一次寫作時可做一題一問的偏好訪談，也可略過；沒有樣本時，可用當次主題的小段試寫讓作者直接修改，再由作者審閱偏好摘要與示範改寫後決定是否保存。Fish 的三庫可作私人設定參考，但不會變成其他用戶的預設。

## 未解問題
- 新 SR 是否需要結構化 evidence 欄位，或先以 Markdown 保存即可。
- 社群平台帳號讀取受平台限制；目前只驗證讀不到時的貼上／匯出退路，尚未對真實帳號連線驗收。

## 下一步
完成 `author-adaptive-writing-preferences` 的 Spectra validation/analyze；通過後再進入 apply 實作。
