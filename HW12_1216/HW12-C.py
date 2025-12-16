class Member:
    # 類別屬性 (Class Attribute) - 全家共享的點數倍率
    rate = 1.0
    
    @classmethod
    def set_rate(cls, value):
        # 類別方法 (Class Method) - 修改全域點數倍率
        cls.rate = value
    
    def __init__(self, name, spend):
        # 實體屬性 (Instance Attribute) - 成員個人資訊
        self.name = name
        self.spend = spend
    
    def get_points(self):
        # 實體方法 (Instance Method) - 計算獲得點數
        # 點數 = 消費金額 * 倍率（取整數）
        return int(self.spend * Member.rate)


# 主程式
n = int(input())
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "member":
        name = command[1]
        spend = float(command[2])
        
        # 建立成員物件
        member = Member(name, spend)
        points = member.get_points()
        print(f"{name} got {points} points")
    
    elif command[0] == "rate":
        new_rate = float(command[1])
        Member.set_rate(new_rate)
        print(f"Rate updated to {new_rate}")
