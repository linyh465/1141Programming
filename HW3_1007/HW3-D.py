h1, m1, h2, m2 = map(int, input().split())
start = h1 * 60 + m1
end = h2 * 60 + m2
time = end - start

hours = (time + 59) // 60
if time <= 30:
    print(0)
elif hours <= 2:
    print(hours * 30)
elif hours <= 4:
    print(2 * 30 + (hours - 2) * 40)
else:
    print(2 * 30 + 2 * 40 + (hours - 4) * 60)