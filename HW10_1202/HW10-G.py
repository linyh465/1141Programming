class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        # 初始化一個空列表，用來裝 Item 物件
        self.items = []

    def add_item(self, item):
        """
        參數 item: 預期是一個 Item 類別的物件
        """
        self.items.append(item)

    def remove_item(self, item_name):
        """
        移除第一個名稱符合 item_name 的商品
        """
        # 我們需要遍歷列表，找到第一個名字一樣的商品物件
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item) # 移除該物件
                return # 找到並移除後，立刻結束函式 (只移除一個)

    def get_total(self):
        """
        計算總金額
        """
        total = 0
        for item in self.items:
            total += item.price # 取出每個物件的 price 屬性累加
        return total

# --- 主程式區塊 ---

# 1. 建立購物車
cart = ShoppingCart()

# 2. 讀取指令數量
n = int(input())

# 3. 處理指令
for _ in range(n):
    line = input().split()
    command = line[0]

    if command == "add":
        # 格式: add [name] [price]
        name = line[1]
        price = int(line[2])
        
        # 建立 Item 物件，並加入購物車
        new_item = Item(name, price)
        cart.add_item(new_item)

    elif command == "remove":
        # 格式: remove [name]
        name = line[1]
        cart.remove_item(name)

    elif command == "total":
        # 格式: total
        print(f"Total: {cart.get_total()}")