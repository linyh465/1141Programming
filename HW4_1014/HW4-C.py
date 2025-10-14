n, k = map(int, input().split())

# 計算 n 的階乘
fact = 1
for i in range(1, n + 1):
    fact *= i

# 用 for 迴圈和 % // 提取第 k 位數字
digit = 0
for i in range(k):
    digit = fact % 10
    fact //= 10

if fact == 0 and k > i + 1:
    print(0)
else:
    print(digit)

