n = int(input())
if n < 2:
    print(0)
else:
    total = 0
    for i in range(2, n+1, 2):
        total += i
    print(total)
