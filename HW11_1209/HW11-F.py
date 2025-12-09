class Flight:
    # 類別屬性 (Class Attribute) - 總座位數
    total_seats = 0
    
    @classmethod
    def set_capacity(cls, num):
        # 類別方法 (Class Method) - 更換機型座位數
        cls.total_seats = num
    
    @staticmethod
    def is_valid_passport(passport):
        # 靜態方法 (Static Method) - 驗證護照格式
        # 必須是 9 碼英數字
        if len(passport) != 9:
            return False
        return passport.isalnum()
    
    def __init__(self):
        # 實體屬性 (Instance Attribute) - 已訂位數量
        self.booked = 0
    
    def book(self, passport):
        # 實體方法 (Instance Method) - 處理訂位
        # 先驗證護照格式
        if not Flight.is_valid_passport(passport):
            return "Invalid Passport"
        
        # 檢查是否還有座位
        if self.booked >= Flight.total_seats:
            return "Flight Full"
        
        # 訂位成功
        self.booked += 1
        return "Booking Confirmed"


# 主程式
initial_capacity = int(input())
Flight.set_capacity(initial_capacity)

flight = Flight()

n = int(input())
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "config":
        new_capacity = int(command[1])
        Flight.set_capacity(new_capacity)
        print("Capacity Updated")
    
    elif command[0] == "book":
        passport = command[1]
        result = flight.book(passport)
        print(result)
