pw = input()
check_1 = 0
check_A = 0
check_a = 0

for c in pw:
    if c.isdigit():
            check_1 += 1

    if c.isupper():
            check_A += 1

    if c.islower():
            check_a += 1
            
if check_1 > 0 and check_A > 0 and check_a > 0 and len(pw) >= 8:
    print("Strong")
else:
    print("Weak")