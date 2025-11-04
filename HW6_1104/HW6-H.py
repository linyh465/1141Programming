def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def GCD():
    a, b = map(int, input().split())
    return gcd(a, b)


print(GCD())
