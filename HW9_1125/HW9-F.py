def check_schedule_conflict():
    # 1. 讀取 N (行程數量)
    try:
        N = int(input())
    except Exception:
        # 如果讀取 N 失敗，則沒有行程，不衝突
        print("Schedule OK")
        return

    # 2. 讀取 N 個行程
    meetings = []
    for _ in range(N):
        try:
            # 讀取一行 Start End，並轉換為整數
            start, end = map(int, input().split())
            meetings.append((start, end))
        except Exception:
            # 忽略格式錯誤的行程
            continue

    # 如果行程數量不足 2 個，不可能有衝突
    if len(meetings) < 2:
        print("Schedule OK")
        return

    # 3. 核心步驟：依據開始時間對行程進行排序
    # key=lambda x: x[0] 表示以 tuple 的第一個元素 (開始時間) 排序
    meetings.sort(key=lambda x: x[0])

    # 4. 依序檢查相鄰行程是否衝突
    # 我們只需要檢查第 i 個行程和第 i+1 個行程
    for i in range(len(meetings) - 1):
        # 當前行程 (i)
        current_start, current_end = meetings[i]
        
        # 下一個行程 (i+1)
        next_start, next_end = meetings[i+1]

        # 衝突判斷邏輯：
        # 如果 [當前行程的結束時間] > [下一個行程的開始時間]，則發生衝突。
        # 注意：題目要求剛好接續 (1000 結束, 1000 開始) 不算衝突，
        # 所以我們使用嚴格大於號 (>)
        
        if current_end > next_start:
            # 一旦找到任何衝突，立即輸出結果並結束程式
            print("Conflict found")
            return

    # 5. 如果迴圈跑完都沒有找到衝突
    print("Schedule OK")

# 執行函式
check_schedule_conflict()