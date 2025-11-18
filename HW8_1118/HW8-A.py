n = int(input())
guests = set()
for _ in range(n):
    guests.add(input().strip())
print(f"Unique guests: {len(guests)}")

