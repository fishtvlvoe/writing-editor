#!/usr/bin/env python3
"""寫作防污染檢查工具 (Anti-Contamination Checker)

功能：
1. 比對目標草稿與歷史文章的敘事重疊（連續重複情節與句型）。
2. 檢查是否有非當次主題的專屬故事黑名單（如日本亞運、2016 嘉年華倒賠 80 萬等）。
3. 發現跨篇故事污染即 Exit 1，保護老魚文章獨立性。
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

# 跨主題專屬的故事片段關鍵字（不可出現在其他主題文章中）
TOPIC_STORY_SIGNATURES: dict[str, list[str]] = {
    "日本亞運與2016嘉年華故事": [
        "倒賠八十萬",
        "大同電鍋蓋一掀開",
        "吃拜拜吃剩的年菜",
        "換成厚厚一把紅色的一百塊",
        "躲進沒開燈的廁所",
        "名古屋亞運",
        "大停水十幾天沒辦法洗澡",
        "春節嘉年華",
        "如果你完全相信過一個人，最後卻失望摔在地上",
    ],
}

# 允許的全局價值觀簽名金句（老魚做人三大底線）
ALLOWED_SIGNATURE_PATTERNS = [
    r"做人有三個最基本的底線",
    r"要開心喜悅",
    r"要樂於分享",
    r"最核心的，是要有無條件的愛",
    r"事情發生了，去怪別人.*一點用都沒有",
]


def clean_text(text: str) -> str:
    """去除 markdown 標記、空白與換行，取得純字串"""
    text = re.sub(r"#+\s*", "", text)
    text = re.sub(r"[*_`>~-]", "", text)
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"\s+", "", text)
    return text


def is_allowed_signature(sub: str) -> bool:
    for pattern in ALLOWED_SIGNATURE_PATTERNS:
        clean_pat = re.sub(r"\s+", "", pattern)
        if re.search(clean_pat, sub):
            return True
    return False


def find_long_common_substrings(s1: str, s2: str, min_len: int = 18) -> list[str]:
    """尋找兩字串中大於等於 min_len 的連續相同子字串"""
    matches = []
    for i in range(len(s1) - min_len + 1):
        sub = s1[i : i + min_len]
        if sub in s2:
            if is_allowed_signature(sub):
                continue
            if any(sub in m for m in matches):
                continue
            # 嘗試向後擴展
            extended = sub
            while i + len(extended) < len(s1) and (extended + s1[i + len(extended)]) in s2:
                extended += s1[i + len(extended)]
            if not is_allowed_signature(extended):
                matches.append(extended)
    return matches


def check_file(target_path: Path, repo_root: Path) -> int:
    if not target_path.exists():
        print(f"❌ Target file not found: {target_path}")
        return 1

    target_content = target_path.read_text(encoding="utf-8")
    target_clean = clean_text(target_content)

    print(f"🔍 檢查草稿: {target_path.name}")
    errors = 0

    # 1. 專屬故事黑名單檢查（若非該主題專屬文章，不得包含該故事特徵）
    is_carnival_story = "體制之所以縮手" in target_path.name
    if not is_carnival_story:
        for topic, sigs in TOPIC_STORY_SIGNATURES.items():
            for sig in sigs:
                if sig in target_content:
                    print(f"❌ [故事跨篇污染] 偵測到來自「{topic}」的專屬故事文字: 「{sig}」")
                    errors += 1

    # 2. 與 01-未發表的文章 其他歷史檔案比對重疊度（排除自身發布檔）
    history_dir = repo_root / "01-未發表的文章"
    if history_dir.exists():
        for hist_file in history_dir.glob("*.md"):
            # 排除同篇文章的不同副本
            if hist_file.resolve() == target_path.resolve():
                continue
            # 檢查是否為同一篇的命名關聯
            if "虧損二百零九億" in target_path.name and "虧損二百零九億" in hist_file.name:
                continue
            if "writing-trump-si" in str(target_path) and "虧損二百零九億" in hist_file.name:
                continue

            hist_content = hist_file.read_text(encoding="utf-8")
            hist_clean = clean_text(hist_content)

            matches = find_long_common_substrings(target_clean, hist_clean, min_len=18)
            if matches:
                for m in matches[:3]:
                    print(f"❌ [跨篇文字抄錄] 與歷史文章「{hist_file.name}」重疊: 「{m[:30]}...」")
                    errors += 1

    if errors > 0:
        print(f"\n🚨 檢查失敗：發現 {errors} 處跨篇故事或文字重複！請立即修改。")
        return 1

    print("✅ 通過防污染檢查：0 跨篇重複故事，內容 100% 獨立。")
    return 0


def main():
    parser = argparse.ArgumentParser(description="寫作防污染檢查工具")
    parser.add_argument("file", nargs="?", help="要檢查的 markdown 檔案路徑")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    if args.file:
        target_path = Path(args.file).resolve()
    else:
        drafts = list(repo_root.glob("changes/writing-*/draft.md"))
        if not drafts:
            print("❌ 未指定檔案且未找到 changes/writing-*/draft.md")
            sys.exit(1)
        target_path = drafts[0]

    code = check_file(target_path, repo_root)
    sys.exit(code)


if __name__ == "__main__":
    main()
