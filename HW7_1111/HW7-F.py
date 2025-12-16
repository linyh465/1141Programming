'''
def parse_product_line(line: str):
    # line: "001 Apple 50" 或 "001 Fancy Apple 50"
    left, qty_str = line.rsplit(maxsplit=1)
    qty = int(qty_str)
    if " " in left:
        pid, name = left.split(maxsplit=1)
    else:
        pid, name = left, ""
    return pid, name, qty

def find_index_by_id(inventory, pid):
    for i, (p, _, _) in enumerate(inventory):
        if p == pid:
            return i
    return -1

def update_stock(inventory, pid, delta):
    idx = find_index_by_id(inventory, pid)
    p, name, qty = inventory[idx]
    inventory[idx] = (p, name, qty + delta)

def format_query(inventory, pid):
    idx = find_index_by_id(inventory, pid)
    p, name, qty = inventory[idx]
    return f"ID: {p}, Name: {name}, Stock: {qty}"

def main():
    n = int(input().strip())
    inventory = []
    for _ in range(n):
        line = input().rstrip()
        pid, name, qty = parse_product_line(line)
        inventory.append((pid, name, qty))

    m = int(input().strip())
    for _ in range(m):
        parts = input().split()
        cmd = parts[0]
        if cmd == "UPDATE":
            pid = parts[1]
            delta = int(parts[2])
            update_stock(inventory, pid, delta)
        elif cmd == "QUERY":
            pid = parts[1]
            print(format_query(inventory, pid))

if __name__ == "__main__":
    main()
'''


'''
# 建立一個全域變數的串列來當作倉庫
storehouse = []

def update(target_id, change):
    # 遍歷倉庫，我們需要索引值 (index) 才能替換串列中的元素
    # 所以使用 range(len(storehouse))
    for i in range(len(storehouse)):
        item = storehouse[i] # 取得目前的元組，例如 ('001', 'Apple', 50)
        
        # 檢查 ID 是否符合
        if item[0] == target_id:
            # 1. 計算新的庫存量 (原本數量 + 變動量)
            # 注意：這裡讀進來的 change 可能是字串，要轉成 int
            new_stock = item[2] + int(change)
            
            # 2. 建立一個新的元組 (因為舊的元組不能直接改)
            new_item = (item[0], item[1], new_stock)
            
            # 3. 替換掉串列中該索引位置的舊元組
            storehouse[i] = new_item
            
            # 找到後就可以離開迴圈，節省資源
            return

def query(target_id):
    # 查詢只需要讀取，直接遍歷即可
    for item in storehouse:
        if item[0] == target_id:
            # 格式化輸出 f-string
            print(f"ID: {item[0]}, Name: {item[1]}, Stock: {item[2]}")
            return

# --- 主程式區塊 ---

N = int(input())

for _ in range(N):
    raw_data = input().split()
    # 修正重點：讀入初始資料時，數量 (index 2) 必須轉成整數 int
    # 這樣存入元組時才會是 (str, str, int)
    data = (raw_data[0], raw_data[1], int(raw_data[2]))
    storehouse.append(data)

M = int(input())

for _ in range(M):
    active = input().split()

    if active[0] == "UPDATE":
        # 傳入 ID 和 變動數量
        update(active[1], active[2])

    else:
        # 傳入 ID
        query(active[1])
'''