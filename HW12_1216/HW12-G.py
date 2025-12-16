class Account:
    """
    銀行帳戶類別，包含 Static (格式驗證), Class (全行凍結), Instance (轉帳) 方法。
    """
    is_frozen = False  # Class Attribute: 全行凍結狀態
    accounts = {}      # Class Attribute: 儲存所有帳戶實例 {AccID: AccountInstance}
    
    def __init__(self, acc_id, balance):
        self.acc_id = acc_id
        self.balance = balance
        Account.accounts[acc_id] = self
    
    @staticmethod
    def is_valid_account(acc_id):
        """
        Static Method: 驗證帳號格式。
        必須以 'A' 開頭且後接 5 位數字 (共 6 碼)。
        """
        return len(acc_id) == 6 and acc_id[0] == 'A' and acc_id[1:].isdigit()
    
    @classmethod
    def freeze(cls):
        """
        Class Method: 宣告全行凍結。
        """
        cls.is_frozen = True
    
    @classmethod
    def unfreeze(cls):
        """
        Class Method: 解除全行凍結。
        """
        cls.is_frozen = False
    
    def transfer(self, to_acc_id, amount):
        """
        Instance Method: 轉帳操作 (self 為轉出帳戶)。
        """
        # 1. 檢查全行凍結
        if Account.is_frozen:
            return "Frozen"
        
        # 2. 檢查帳號格式 (檢查轉出帳戶和轉入帳戶的格式)
        # 註: 假設創建時格式正確，這裡主要檢查 to_acc_id
        if not Account.is_valid_account(self.acc_id) or not Account.is_valid_account(to_acc_id):
            return "Invalid Account"
        
        # 3. 檢查目標帳戶是否存在 (轉入帳戶必須存在)
        if to_acc_id not in Account.accounts:
            return "Invalid Account"
        
        # 4. 檢查餘額 (轉出帳戶餘額必須足夠)
        if self.balance < amount:
            return "Insufficient Funds"
        
        # 5. 執行轉帳
        self.balance -= amount
        Account.accounts[to_acc_id].balance += amount
        return "Success"

# 外部輸入處理邏輯
try:
    n = int(input())
except EOFError:
    n = 0

for _ in range(n):
    try:
        command = input().split()
    except EOFError:
        break
    except ValueError:
        continue # 忽略無效的輸入行
    
    if not command:
        continue
        
    action = command[0]
    
    if action == "create":
        if len(command) == 3:
            acc_id = command[1]
            try:
                balance = int(command[2])
                # 忽略帳號格式不正確的創建 (雖然題目未要求輸出，但最好只創建有效帳戶)
                if Account.is_valid_account(acc_id):
                    Account(acc_id, balance)
            except ValueError:
                continue # 忽略餘額不是數字的創建
    
    elif action == "transfer":
        if len(command) == 4:
            from_id = command[1]
            to_id = command[2]
            
            try:
                amount = int(command[3])
            except ValueError:
                continue # 忽略金額不是數字的轉帳

            # **【關鍵修正點】**
            # 如果轉出帳戶 (from_id) 不存在，無法呼叫其實例方法，應直接返回錯誤
            if from_id in Account.accounts:
                result = Account.accounts[from_id].transfer(to_id, amount)
                print(result)
            else:
                print("Invalid Account")
    
    elif action == "freeze":
        Account.freeze()
    
    elif action == "unfreeze":
        Account.unfreeze()

#錯誤版
'''
class Account:

    is_frozen = False

    accounts = {}

   

    def __init__(self, acc_id, balance):

        self.acc_id = acc_id

        self.balance = balance

        Account.accounts[acc_id] = self

   

    @staticmethod

    def is_valid_account(acc_id):

        """驗證帳號格式：必須以'A'開頭且後接5位數字"""

        return len(acc_id) == 6 and acc_id[0] == 'A' and acc_id[1:].isdigit()

   

    @classmethod

    def freeze(cls):

        """全行凍結"""

        cls.is_frozen = True

   

    @classmethod

    def unfreeze(cls):

        """全行解凍"""

        cls.is_frozen = False

   

    def transfer(self, to_acc_id, amount):

        """轉帳操作"""

        # 1. 檢查全行凍結

        if Account.is_frozen:

            return "Frozen"

       

        # 2. 檢查帳號格式

        if not Account.is_valid_account(self.acc_id) or not Account.is_valid_account(to_acc_id):

            return "Invalid Account"

       

        # 3. 檢查目標帳戶是否存在

        if to_acc_id not in Account.accounts:

            return "Invalid Account"

       

        # 4. 檢查餘額

        if self.balance < amount:

            return "Insufficient Funds"

       

        # 5. 執行轉帳

        self.balance -= amount

        Account.accounts[to_acc_id].balance += amount

        return "Success"



n = int(input())

for _ in range(n):

    command = input().split()

   

    if command[0] == "create":

        acc_id = command[1]

        balance = int(command[2])

        Account(acc_id, balance)

   

    elif command[0] == "transfer":

        from_id = command[1]

        to_id = command[2]

        amount = int(command[3])

        if from_id in Account.accounts:

            print(Account.accounts[from_id].transfer(to_id, amount))

   

    elif command[0] == "freeze":

        Account.freeze()

   

    elif command[0] == "unfreeze":

        Account.unfreeze()
'''