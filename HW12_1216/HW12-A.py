class Drink:
    def __init__(self, name, price, sugar):
        self.name = name
        self.price = int(price)
        self.sugar = sugar

    def __str__(self):
        # 定義物件被 print 時顯示的字串格式
        return f"{self.name} ({self.sugar}) - ${self.price}"

# 主程式
n = int(input())
orders = []

# 讀取訂單並建立物件
for _ in range(n):
    data = input().strip().split()
    # 處理名稱可能包含空白的情況 (如 Milk Tea)
    sugar = data[-1]
    price = int(data[-2])
    name = " ".join(data[:-2])
    
    # 建立 Drink 物件並加入串列
    drink = Drink(name, price, sugar)
    orders.append(drink)

# 計算總金額並輸出
total = 0
for drink in orders:
    print(drink)  # 自動呼叫 __str__
    total += drink.price

print(f"Total: ${total}")