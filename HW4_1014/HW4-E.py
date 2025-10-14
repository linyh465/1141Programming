'''
A, B = map(int, input().split())

a, b = A, B

while b != 0:
    a, b = b, a % b
    
g = a

l = A * B // g

print(f"GCD: {g}, LCM: {l}")
'''


A, B = map(int, input().split())


g = 1
for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        g = i

l = A * B // g

print(f"GCD: {g}, LCM: {l}")