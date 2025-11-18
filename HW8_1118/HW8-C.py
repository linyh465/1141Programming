try:
	n = int(input())
except Exception:
	n = 0

seen = set()
result = []
for _ in range(n):
	song = input().rstrip()
	if song not in seen:
		seen.add(song)
		result.append(song)

print(result)

