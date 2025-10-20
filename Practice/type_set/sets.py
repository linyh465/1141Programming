#Python of sets

fruits_set = {"🍎","🍊", "🍌"}
fruits_set.add("🍎") #set 不會重複儲存同一值
fruits_set.add("🥥")
for fruit in fruits_set:
    print(fruit, end=" ") #set 不會按照順序輸出

print()

if "🍎" in fruits_set:
    print("有一顆蘋果🍎", end="\n")
else:
    print("沒有蘋果🍎", end="\n")


if "🍒" in fruits_set:
    print("有一顆櫻桃🍒", end="\n")
else:
    print("沒有櫻桃🍒", end="\n")