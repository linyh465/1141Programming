# 基礎運算子
a = 5 + 3  # 加法
print("加法:", a)

a += 2 # 等同於 a = a + 2
print("加法後:", a)


b = 5 - 3  # 減法
print("減法:", b)

c = 5 * 3  # 乘法
print("乘法:", c)

d = 5 / 3  # 除法
print("除法:", d)

e = 5 % 3  # 取餘數
print("餘數:", e)

f = 5 ** 3  # 次方
print("次方:", f)

g = 5 // 3  # 取商數
print("取商數:", g)

# math 模組
import math

print("絕對值:", abs(-10))  # 取絕對值
print("平方根:", math.sqrt(16))  # 開根號
print("最大值:", max(1, 2, 3))  # 取最大值
print("最小值:", min(1, 2, 3))  # 取最小值
print("四捨五入:", round(3.14159, 2))  # 四捨五入
print("無條件捨去:", math.floor(3.7))  # 無條件捨去
print("無條件進位:", math.ceil(3.2))  # 無條件進位
print("sin(90°):", math.sin(math.radians(90)))  # 三角函數
print("cos(0°):", math.cos(math.radians(0)))
print("tan(45°):", math.tan(math.radians(45)))
print("圓周率:", math.pi)  # 常數 pi
print("自然常數e:", math.e) # 常數 e

# random 模組
import random

print("隨機浮點數:", random.random())  # 產生 0~1 之間的隨機浮點數
print("隨機整數:", random.randint(1, 10))  # 產生指定範圍的隨機整數
print("隨機選取:", random.choice([1, 2, 3, 4, 5]))  # 從序列中隨機選取一個元素

# decimal 模組（高精度運算）
from decimal import Decimal

a_dec = Decimal('0.1')
b_dec = Decimal('0.2')
print("高精度加法:", a_dec + b_dec)  # 0.3