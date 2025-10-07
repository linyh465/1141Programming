# 讀取學生分數和出席率
score, attendance = map(int, input().split())

# 判斷是否通過
if score >= 60 and attendance >= 75:
    print("Pass")
else:
    print("Retake")
