class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        存款：直接將金額加到餘額上
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        提款：檢查餘額是否足夠
        足夠 -> 扣款並回傳 True
        不足 -> 不扣款並回傳 False
        """
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def check_balance(self):
        """
        回傳當前餘額
        """
        return self.balance

# --- 主程式區塊 ---

# 1. 讀取帳號與初始餘額
# input().split() 會將 "12345 1000" 切割成 ['12345', '1000']
line1 = input().split()
acc_num = line1[0]
init_bal = int(line1[1])

# 2. 建立 Account 物件
my_account = Account(acc_num, init_bal)

# 3. 讀取指令數量 N
n = int(input())

# 4. 處理 N 筆指令
for _ in range(n):
    command_line = input().split()
    command = command_line[0]      # 指令名稱 (deposit 或 withdraw)
    amount = int(command_line[1])  # 金額

    if command == "deposit":
        # 呼叫存款方法，修改物件內的 balance
        my_account.deposit(amount)
        
    elif command == "withdraw":
        # 呼叫提款方法，並根據回傳的 True/False 決定輸出內容
        is_success = my_account.withdraw(amount)
        if is_success:
            print("Success")
        else:
            print("Insufficient funds")

# 5. 輸出最終餘額
print(f"Final Balance: {my_account.check_balance()}")