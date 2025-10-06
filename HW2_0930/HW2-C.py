#C
'''
import math

def c_diagonal(length, width):
    d = math.sqrt(length**2 + width**2)
    return round(d, 2)

length, width = map(int, input().split())

d_length = c_diagonal(length, width)
print(f"{d_length:.2f}")
'''

import math
l,w = map(int, input().split())
d = float(math.sqrt(l**2+w**2))
print(f"{d:.2f}")
