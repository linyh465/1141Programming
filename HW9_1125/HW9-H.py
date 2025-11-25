import sys

# 讀取輸入（兩個整數 N K）
data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
try:
    n = int(data[0])
    k = int(data[1])
except Exception:
    sys.exit(0)

# Josephus 迭代公式（0-based）
# f(1) = 0
# f(i) = (f(i-1) + k) % i
winner = 0
for i in range(1, n + 1):
    winner = (winner + k) % i

# 輸出 1-based 編號
print(f"Winner is {winner + 1}")
