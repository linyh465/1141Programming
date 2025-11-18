#!/usr/bin/env python3
# 讀取 N 行句子，統計單字出現次數：轉小寫、移除 . , ! ?，以空格切分
try:
    n = int(input())
except Exception:
    n = 0

counts = {}
for _ in range(n):
    line = input().lower()
    for p in '.,!?':
        line = line.replace(p, '')
    for w in line.split():
        counts[w] = counts.get(w, 0) + 1

for word in sorted(counts.keys()):
    print(f"{word}: {counts[word]}")
