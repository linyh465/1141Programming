s = 77
while True:
    n = int(input())
    if n == s:
        break
    elif n < s:
        print("Too low")
    else:
        print("Too high")

print("Correct!")