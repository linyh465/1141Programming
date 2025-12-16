class ContactSystem:
    @staticmethod
    def is_valid_phone(phone):
        # 檢查是否為 10 碼且全為數字
        return len(phone) == 10 and phone.isdigit()

# 主程式
n = int(input())
students = {}

for _ in range(n):
# 讀取每行資料：學號 姓名 電話
    data = input().strip().split()
    student_id = data[0]  # <-- 將 data[0] (即學號，一個字串) 賦值給 student_id
    name = data[1]
    phone = data[2]
    
    # 呼叫靜態方法驗證電話
    if ContactSystem.is_valid_phone(phone):
        students[student_id] = name  # student_id 現在是字串，是可雜湊的
        print(f"{name} added")
    else:
        print("Invalid Phone")

# 依學號排序並輸出
sorted_ids = sorted(students.keys())
for sid in sorted_ids:
    print(f"{sid}: {students[sid]}")
    