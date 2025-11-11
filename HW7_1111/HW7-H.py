import heapq

def main():
    try:
        n = int(input().strip())
    except Exception:
        return

    arr = []
    results = []
    for _ in range(n):
        try:
            x = int(input().strip())
        except Exception:
            x = 0
        arr.append(x)
        arr.sort()
        m = len(arr)
        if m % 2 == 1:
            median = float(arr[m // 2])
        else:
            median = (arr[m // 2 - 1] + arr[m // 2]) / 2.0
        results.append(median)

    for v in results:
        print(f"{v:.1f}")

if __name__ == "__main__":
    main()