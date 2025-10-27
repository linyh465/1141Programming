A, B = map(int, input().split())
result = []

for i in range(A, B + 1):
    # 將數字轉成字串,再轉成串列取得各位數
    digits = str(i)
    n = len(digits)
    
    # 計算各位數的 n 次方和
    total = 0
    for d in digits:
        total += int(d) ** n
    
    # 如果等於原數字,就是阿姆斯壯數
    if total == i:
        result.append(i)

# 輸出結果,用空格分隔
for num in result:
    print(num, end=' ')
    