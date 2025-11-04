def factorial(n):
    if n > 1:  # 遞迴
        return n * factorial(n - 1)  # 傳回 n*n-1 的階乘
    else:
        return 1  # 終止條件，當n=1時傳回1


n = int(input())  

print(factorial(n)) 