'''
try:
    n = int(input().strip())
except Exception:
    n = 0

entries = []
for _ in range(n):
    try:
        parts = input().strip().split()
        name = parts[0] if parts else ""
        score = int(parts[1]) if len(parts) > 1 else 0
    except Exception:
        name = ""
        score = 0
    entries.append((score, name))

# 每次用 for 迴圈找出目前最高分的索引，印出姓名後移除該項
for _ in range(len(entries)):
    max_idx = 0
    for j in range(1, len(entries)):
        if entries[j][0] > entries[max_idx][0]:
            max_idx = j
    print(entries[max_idx][1])
    entries.pop(max_idx)
'''

'''
grade = int(input())
all_grade = []
for i in range(grade):
    grade_list = tuple(input().split())
    all_grade.append(grade_list)

for j in range(grade):
    max_index = 0
    for k in range(1, len(all_grade)):
        if int(all_grade[k][1]) > int(all_grade[max_index][1]):
            max_index = k

    print(all_grade[max_index][0])
    all_grade.pop(max_index)
'''



n = int(input())

grade_list = [] # 初始化一個空列表，用於儲存所有學生的資料

for i in range(n):
    grade = tuple(input().split())
    grade_list.append(grade) # 將該學生的元組新增到列表中


# 使用列表的 sort() 方法進行原地排序
# key=lambda x: int(x[1]) 定義了排序的依據：
# 1. x[1] 是元組中的第二個元素 (成績，如 '85')
# 2. int() 確保在比較時將字串成績轉換為數字，避免 '100' < '90' 的錯誤
# reverse=True 設置為降序排列 (分數從高到低)
grade_list.sort(key=lambda x:int(x[1]), reverse=True)



#Pythonic
for name, grade in grade_list:
    print(name)

'''
for j in range(n):
    print(grade_list[0][0])
    grade_list.pop(0)
'''


# sorted 參考 https://www.runoob.com/python/python-func-sorted.html