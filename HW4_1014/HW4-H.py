n = int(input())

steps = 0
max_n = n

while n != 1:
    if n % 2 == 0:
        n = n // 2

    else:
        n = 3 * n + 1
    steps += 1

    if n > max_n:
        max_n = n

print(f"Steps: {steps}, Max: {max_n}")