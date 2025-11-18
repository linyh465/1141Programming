
# 讀取 N 筆成績資料，建立巢狀字典 student -> {subject: score}
try:
	n = int(input())
except Exception:
	n = 0

grades = {}
for _ in range(n):
	parts = input().split()
	if len(parts) < 3:
		continue
	name, subj, score = parts[0], parts[1], parts[2]
	grades.setdefault(name, {})[subj] = int(score)

try:
	m = int(input())
except Exception:
	m = 0

for _ in range(m):
	parts = input().split()
	if len(parts) < 2:
		continue
	name, subj = parts[0], parts[1]
	print(grades[name][subj])

