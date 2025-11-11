def main():
    try:
        n = int(input().strip())
    except Exception:
        return

    arr = []
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
        print(f"{median:.1f}")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass