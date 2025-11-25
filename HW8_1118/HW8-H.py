'''
# 讀取 N 筆會員興趣資料，建立 interest -> set(names) 字典
try:
	n = int(input())
except Exception:
	n = 0

groups = {}
for _ in range(n):
	parts = input().split()
	if len(parts) < 2:
		continue
	name, interest = parts[0], parts[1]
	groups.setdefault(interest, set()).add(name)

try:
	m = int(input())
except Exception:
	m = 0

for _ in range(m):
	q = input().strip()
	members = sorted(groups.get(q, set()))
	print(members)

'''