'''
def main():
    try:
        n = int(input().strip())
    except Exception:
        n = 0

    expenses = []
    for _ in range(n):
        try:
            expenses.append(int(input().strip()))
        except Exception:
            expenses.append(0)

    total = sum(expenses)
    average = total / n if n > 0 else 0.0
    print(f"Total: {total}, Average: {average:.2f}")

if __name__ == "__main__":
    main()
'''

N = int(input())
money_list = []
for i in range(N):
    money = int(input())
    money_list.append(money)

T = sum(money_list)
# 避免 N=0 時的錯誤
if N > 0:
    A = T / N
else:
    A = 0.0

print(f"Total: {T}, Average: {A:.2f}")

