try:
    n = int(input().strip())
except Exception:
    n = 0

entries = []
for _ in range(n):
    try:
        parts = input().strip().split()
        name = parts[0] if parts else ""
        score = int(parts[1]) if len(parts) > 1 else 0
    except Exception:
        name = ""
        score = 0
    entries.append((score, name))

# 每次用 for 迴圈找出目前最高分的索引，印出姓名後移除該項
for _ in range(len(entries)):
    max_idx = 0
    for j in range(1, len(entries)):
        if entries[j][0] > entries[max_idx][0]:
            max_idx = j
    print(entries[max_idx][1])
    entries.pop(max_idx)