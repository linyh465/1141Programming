ts = input().split() 
s = []

for t in ts:
    if t.isdigit():
        s.append(int(t))
    else:
        b = s.pop()
        a = s.pop()
        if t == '+':
            s.append(a + b)
        elif t == '-':
            s.append(a - b)
        elif t == '*':
            s.append(a * b)

print(s[0])