def create_leaderboard():
    """
    讀取學生資料，依分數由高至低排序；分數相同時按姓名預設（A-Z）排序，並印出姓名。
    """
    students = []
    try:
        num_students = int(input())
    except (ValueError, EOFError):
        num_students = 0

    for _ in range(num_students):
        try:
            line = input().rstrip()
            if not line:
                continue
            # 支援姓名可能有空格，從右邊分割最後一個欄位為分數
            parts = line.rsplit(maxsplit=1)
            if len(parts) == 2:
                name, score_str = parts[0], parts[1]
            else:
                name, score_str = parts[0], "0"
            score = int(score_str)
            students.append((score, name))
        except (IndexError, ValueError, EOFError):
            continue

    # 依分數由高至低排序；分數相同時姓名由小到大（預設）
    students.sort(key=lambda t: (-t[0], t[1]))

    for score, name in students:
        print(name)

if __name__ == "__main__":
    create_leaderboard()