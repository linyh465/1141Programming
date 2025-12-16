class Stats:
    @staticmethod
    def calculate_avg(scores_list):
        # 靜態方法 (Static Method) - 計算平均值
        if not scores_list:
            return 0.0
        return sum(scores_list) / len(scores_list)


class Student:
    # 類別屬性 - 儲存所有學生
    students = {}
    
    def __init__(self, name):
        # 實體屬性 (Instance Attribute)
        self.name = name
        self.scores = []  # List 儲存該學生的所有成績
        
        # 註冊到類別屬性中
        Student.students[name] = self
    
    def add_score(self, score):
        # 實體方法 (Instance Method) - 新增成績
        self.scores.append(score)
    
    def get_average(self):
        # 實體方法 (Instance Method) - 計算平均值
        # 內部呼叫靜態方法
        return Stats.calculate_avg(self.scores)


# 主程式
n = int(input())
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "add":
        name = command[1]
        score = int(command[2])
        
        # 若學生不存在則建立
        if name not in Student.students:
            Student(name)
        
        # 新增成績
        Student.students[name].add_score(score)
    
    elif command[0] == "query":
        name = command[1]
        
        if name in Student.students:
            avg = Student.students[name].get_average()
            print(f"{name} Average: {avg:.1f}")
