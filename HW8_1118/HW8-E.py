try:
	n = int(input())
except Exception:
	n = 0

present = set()
for _ in range(n):
	try:
		seat = int(input())
	except Exception:
		continue
	present.add(seat)

expected = set(range(1, 11))
absent = sorted(expected - present)
print(absent)

