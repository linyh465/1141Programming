N = int(input())

while N >= 10:
    n_sum = 0
    temp = N
    while temp > 0:
        n_sum += temp % 10   
        temp //= 10         
    N = n_sum

print(N)