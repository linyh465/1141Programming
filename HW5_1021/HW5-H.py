# 讀取輸入
A, B = map(int, input().split())

# 尋找迴文質數
result = []
for num in range(A, B + 1):
    # 判斷是否為迴文數
    s_num = str(num)
    if s_num != s_num[::-1]:
        continue
    
    # 判斷是否為質數
    if num < 2:
        continue
    if num == 2:
        result.append(num)
        continue
    if num % 2 == 0:
        continue
    
    is_prime = True
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        result.append(num)

# 輸出結果
print(result)