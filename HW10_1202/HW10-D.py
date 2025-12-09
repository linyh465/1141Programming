class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []  # 初始化一個空列表來儲存成績

    def add_score(self, score):
        """
        將成績加入列表中
        """
        self.scores.append(score)

    def calculate_average(self):
        """
        計算平均值：總分 / 科目數
        若列表為空，回傳 0.0 以避免除以零錯誤
        """
        if len(self.scores) == 0:
            return 0.0
        return sum(self.scores) / len(self.scores)

# --- 主程式區塊 ---

# 1. 讀取學生名字並建立物件
name = input()
student = Student(name)

# 2. 讀取操作次數 N
n = int(input())

# 3. 迴圈處理指令
for _ in range(n):
    line = input().split()
    command = line[0]

    if command == "add":
        # 取得分數並轉為整數
        score = int(line[1])
        student.add_score(score)
        
    elif command == "avg":
        # 計算平均並格式化輸出
        average = student.calculate_average()
        # {:.2f} 代表保留小數點後兩位
        print(f"{average:.2f}")