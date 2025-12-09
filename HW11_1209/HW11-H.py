class SmartHome:
    # 類別屬性 (Class Attribute) - 全家總耗電量
    total_load = 0
    
    # 類別屬性 - 家電記錄
    appliances = {}
    
    @staticmethod
    def is_safe_watts(watts):
        # 靜態方法 (Static Method) - 安全檢查
        # 電器瓦數不能超過 3000W
        return watts <= 3000
    
    def __init__(self, name, watts):
        # 實體屬性 (Instance Attribute) - 家電資訊
        self.name = name
        self.watts = watts
        self.is_on = False
        
        # 記錄到類別屬性中
        SmartHome.appliances[name] = self
    
    def turn_on(self):
        # 實體方法 (Instance Method) - 開啟家電
        if not self.is_on:
            self.is_on = True
            SmartHome.total_load += self.watts
    
    def turn_off(self):
        # 實體方法 (Instance Method) - 關閉家電
        if self.is_on:
            self.is_on = False
            SmartHome.total_load -= self.watts


# 主程式
n = int(input())
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "add":
        name = command[1]
        watts = int(command[2])
        
        # 先檢查瓦數是否安全
        if not SmartHome.is_safe_watts(watts):
            print("Overload Risk")
        else:
            # 建立家電物件
            SmartHome(name, watts)
            print("Installed")
    
    elif command[0] == "turn_on":
        name = command[1]
        if name in SmartHome.appliances:
            SmartHome.appliances[name].turn_on()
    
    elif command[0] == "turn_off":
        name = command[1]
        if name in SmartHome.appliances:
            SmartHome.appliances[name].turn_off()
    
    elif command[0] == "status":
        print(f"Current Load: {SmartHome.total_load}W")
