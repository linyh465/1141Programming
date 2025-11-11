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