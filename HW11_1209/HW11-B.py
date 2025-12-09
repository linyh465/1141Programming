class Security:
    @staticmethod
    def is_valid(password):
        # 檢查密碼長度 >= 6
        if len(password) < 6:
            return False
        
        # 檢查是否包含至少一個數字
        has_digit = False
        for char in password:
            if char.isdigit():
                has_digit = True
                break
        
        return has_digit


# 主程式
n = int(input())
for _ in range(n):
    password = input().strip()
    if Security.is_valid(password):
        print("Valid")
    else:
        print("Weak")
