class Employee:
    # 類別屬性 (Class Attribute) - 全公司共享
    total_employees = 0
    next_id = 1
    
    def __init__(self, name):
        # 實體屬性 (Instance Attribute) - 員工個人資訊
        self.name = name
        self.id = Employee.next_id
        
        # 更新類別屬性
        Employee.next_id += 1
        Employee.total_employees += 1
        
        # 輸出員工資訊
        print(f"{self.name} ID: {self.id}, Total Staff: {Employee.total_employees}")


# 主程式
n = int(input())
for _ in range(n):
    name = input().strip()
    Employee(name)
