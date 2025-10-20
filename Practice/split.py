'''
# Python 會自動將 split() 產生的列表解包 (unpack) 到變數中
name, age_str = input("請輸入姓名和年齡，以空格隔開：").split()

# 進行必要的型別轉換
age = int(age_str)

print(f"姓名: {name}")
print(f"年齡: {age}")
print(f"十年後，{name} 將是 {age + 10} 歲。")

'''
# Python 會自動將 split() 產生的列表解包 (unpack) 到變數中
name, age = map(str, input("請輸入姓名和年齡，以空格隔開：").split())

age = int(age)

print(f"姓名: {name}")
print(f"年齡: {age}")
print(f"十年後，{name} 將是 {age + 10} 歲。")