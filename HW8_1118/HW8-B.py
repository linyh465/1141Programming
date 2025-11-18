#!/usr/bin/env python3
n = int(input())
prices = dict(input().split() for _ in range(n))
m = int(input())
for _ in range(m):
    print(prices[input().strip()])
import sys

lines = [l.rstrip() for l in sys.stdin if l.strip()]
if not lines:
    sys.exit(0)

i = 0
N = int(lines[i]); i += 1
price = {}
for _ in range(N):
    name, val = lines[i].rsplit(None, 1)
    i += 1
    price[name] = int(val)

M = int(lines[i]); i += 1
out = []
for _ in range(M):
    fruit = lines[i].strip(); i += 1
    out.append(str(price[fruit]))

print("\n".join(out))