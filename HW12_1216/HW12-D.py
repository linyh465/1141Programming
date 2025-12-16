class Warehouse:
    def __init__(self, initial_items):
        # 實體屬性 (Instance Attribute)
        self.inventory = set(initial_items)  # 有貨的商品（Set）
        self.missing = []  # 缺貨的商品（List）
    
    def order(self, item):
        # 實體方法 (Instance Method) - 處理訂單
        if item in self.inventory:
            # 商品在庫存中
            return "Shipped"
        else:
            # 商品不在庫存中
            if item not in self.missing:
                self.missing.append(item)
            return "Out of Stock"
    
    def restock(self, item):
        # 實體方法 (Instance Method) - 補貨
        self.inventory.add(item)
    
    def get_missing_count(self):
        # 實體方法 (Instance Method) - 獲得缺貨清單長度
        return len(self.missing)


# 主程式
# 讀取初始庫存
initial_stock = input().strip().split()
warehouse = Warehouse(initial_stock)

# 讀取指令數
n = int(input())

# 執行指令
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "order":
        item = command[1]
        result = warehouse.order(item)
        print(result)
    
    elif command[0] == "restock":
        item = command[1]
        warehouse.restock(item)

# 輸出缺貨清單統計
missing_count = warehouse.get_missing_count()
print(f"Total Missing: {missing_count}")
