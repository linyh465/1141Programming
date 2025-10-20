#Python of Dictionary

# 鍵 => 值
 #Key => Value

capitals = {
    "Taiwan": "Taipei",
    "Japan": "Tokyo",
    "United States" : "Washington D.C.",
    "France" : "Paris"
    }

#get() 取得鍵值對
print(capitals.get("Japan")) #Tokyo
print(capitals.get("Taiwan")) #Taipei

#update() 更新或新增鍵值對
capitals.update({"Germany": "Berlin"}) #新增
print(capitals)

#pop() 刪除鍵值對
capitals.pop("France")
print(capitals)

#values()獲得所有值
print(capitals.values())

#items() 獲得所有鍵值對
print(capitals.items())
