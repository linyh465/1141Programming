def read_board():
    board = []
    for _ in range(3):
        s = input().strip()
        # 去除空白並轉大寫，只保留 X/O/. 三種字元
        row = [c.upper() for c in s if c in ('X', 'O', '.', 'x', 'o')]
        # 若行末有空白導致長度不足，補齊為 3 格
        while len(row) < 3:
            row.append('.')
        board.append(row[:3])
    return board

def x_wins(board):
    # 檢查三行
    for i in range(3):
        if all(board[i][j] == 'X' for j in range(3)):
            return True
    # 檢查三列
    for j in range(3):
        if all(board[i][j] == 'X' for i in range(3)):
            return True
    # 檢查兩條對角線
    if all(board[i][i] == 'X' for i in range(3)):
        return True
    if all(board[i][2 - i] == 'X' for i in range(3)):
        return True
    return False

def main():
    board = read_board()
    print("X wins" if x_wins(board) else "In progress or Draw")

if __name__ == "__main__":
    main()