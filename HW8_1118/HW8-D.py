
# 讀取 N 張選票，使用字典計數，最後按姓名字母序輸出 "Name: Votes"
try:
	n = int(input())
except Exception:
	n = 0

counts = {}
for _ in range(n):
	name = input().strip()
	if name in counts:
		counts[name] += 1
	else:
		counts[name] = 1

for name in sorted(counts.keys()):
	print(f"{name}: {counts[name]}")

