print("For 迴圈")
#迭代清單中的元素
print("#迭代清單中的元素")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit,end=" ")

print(" ",end="\n\n")

#迭代字串中的字元
print("#迭代字串中的字元")
message = "Hello, World!"
for char in message:
    print(char,end=" ")

print(" ",end="\n\n")

#迭代範圍內的數字
print("#迭代範圍內的數字")
for num in range(2,7,2):
    print(num,end=" ")

print(" ",end="\n\n")

#迭代字典中的鍵或值
print("#迭代字典中的鍵或值")
student_score = {"Alice": 85, "Bob": 92, "Carol": 78}
for name in student_score:
    print(f"{name}: {student_score[name]}")

print(" ",end="\n\n")

#使用 continue 跳過奇數
print("#使用 continue 跳過奇數")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 1:
        continue
    print(num, "是偶數")

print(" ",end="\n\n")



print("While 迴圈")
#使用 break 找到第一個費波那契數大於 100 的數
print("#使用 break 找到第一個費波那契數大於 100 的數")
a, b = 0, 1
while b < 100:
    print(b,end=" ")
    a, b = b, a + b # a = b : b賦值給a ; b = a + b : a+b賦值給
    if b > 100:
        break