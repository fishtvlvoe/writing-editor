## 1. 通用寫作助手與文章流程

- [ ] 1.1 落實 Keep one user-facing writing assistant; put capabilities in Skills：將 `agents/writing-assistant.yaml` 改成通用入口，不把老魚偏好寫成共同預設；檢查預設提示不含老魚專屬稱呼、口吻或故事，且 `agents/openai.yaml` 未變。
- [ ] 1.2 落實 The writing assistant SHALL interview one question at a time：用對話情境確認每輪只有一個開放問題；使用者卡住時以啟發式追問協助思考。
- [ ] 1.3 落實 The writing assistant SHALL separate suggestions from the author's position：確認未要求發想時不塞入新觀點；要求發想時，建議有標示，且須經作者挑選才能進大綱。
- [ ] 1.4 落實 The writing assistant SHALL confirm the article direction and outline before drafting：確認方向與大綱未獲作者核准前，不會產出全文初稿。
- [ ] 1.5 落實 The writing assistant SHALL verify external factual claims when research is needed：用查證情境確認外部事實有來源、無法核實的內容會標為不確定。
- [ ] 1.6 落實 The writing assistant SHALL draft and revise within the confirmed direction：用修稿情境確認局部回饋只改相關段落；主張改變時退回訪談或大綱確認。
- [ ] 1.7 落實 The writing assistant SHALL require author approval before marking an article final：確認未經作者同意的文章仍維持草稿狀態。
- [ ] 1.8 落實 The writing assistant SHALL not publish without explicit instruction：確認作者只核准定稿、但未要求發布時，不會對外發布。
- [ ] 1.9 落實 The first release SHALL focus on social posts and web articles：以社群貼文、部落格和網路文章驗收；對企劃書、報告或電子郵件不宣稱支援。

## 2. 作者風格設定

- [ ] 2.1 落實 Style onboarding SHALL be optional：用沒有樣本的使用情境確認作者可跳過設定，直接開始談文章主題。
- [ ] 2.2 落實 Account-level style analysis SHALL require explicit scope and consent：確認只分析使用者指定的平台、期間與可讀取的原創內容；連結讀不到時請使用者貼文或提供匯出，不索取帳密。
- [ ] 2.3 落實 A style profile SHALL be reviewed before persistence：確認先提供風格摘要與示範改寫，作者可修正；未明確同意前不保存。
- [ ] 2.4 落實作者個人設定是私人且須主動同意保存 (Treat each author profile as private, opt-in data) 與 Author profiles SHALL be isolated and user-controlled：選定共享套件以外的個人保存位置；驗收檢視、修改、刪除、作者間隔離，且單篇素材不自動寫入長期設定。
- [ ] 2.5 落實 A style profile SHALL support a shared voice and optional platform variants：確認平台偏好會疊加在共通口吻上，未設定的平台不會被假裝已設定。

## 3. 整合與驗收

- [ ] 3.1 落實風格分析是可跳過的首次使用路徑 (Make style analysis an optional first-use path) 與 Use an author-confirmed style card and rewrite：確認使用者可接受、修正、跳過分析或拒絕保存風格卡。
- [ ] 3.2 落實訪談與發想都保留作者決定權 (Preserve author agency during interviews and ideation)：確認開放提問不預設答案；只有作者要求且確認後的建議才能進入文章。
- [ ] 3.3 落實第一版聚焦文章，不擴成萬用寫作工具 (Keep the first release focused on articles)：確認驗收案例涵蓋社群貼文、部落格和網路文章，不擴到報告、企劃或電子郵件。
- [ ] 3.4 執行作者與個人設定情境矩陣，並跑 `spectra validate writing-assistant-generalization` 與 `spectra analyze writing-assistant-generalization`：驗證作者隔離、可跳過設定、連結讀取失敗退路、平台差異、修稿回圈、作者定稿確認與禁止未授權發布；修完所有驗證錯誤與分析器重大缺口。
