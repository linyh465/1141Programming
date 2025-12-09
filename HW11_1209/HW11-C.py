class Wallet:
    # 類別屬性 (Class Attribute) - 所有錢包共享的匯率
    rate = 30.0
    
    def __init__(self, balance):
        # 實體屬性 (Instance Attribute) - 個人的美金餘額
        self.balance = balance
    
    @classmethod
    def set_rate(cls, new_rate):
        # 類別方法 (Class Method) - 修改全域匯率設定
        # 使用 cls 來存取和修改類別屬性
        cls.rate = new_rate
    
    def get_local_balance(self):
        # 實體方法 (Instance Method) - 計算當地貨幣金額
        # 使用 self.balance (實體屬性) 和 Wallet.rate (類別屬性)
        return int(self.balance * Wallet.rate)


# 主程式
initial_balance = float(input())
wallet = Wallet(initial_balance)

n = int(input())
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "check":
        print(wallet.get_local_balance())
    elif command[0] == "set":
        new_rate = float(command[1])
        Wallet.set_rate(new_rate)
