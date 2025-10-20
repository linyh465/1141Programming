#Python of list

fruits = ["apple","orange", "banana", "coconut"]

print("print fruits[0]") 
print(fruits[0]) #apple

print() 

print("for_loop print fruits[0]") 
for i in fruits:
    print(i)

print() 

print("append guava") 
fruits.append("guava")
print(fruits) #apple

print() 

print("remove coconut") 
fruits.remove("coconut")
print(fruits)

print() 

print("fruits.index banana") 
print(fruits.index("banana"))

print() 

print("append apple") 
fruits.append("apple")
print(fruits)

print()

print("fruits.count apple")
print(fruits.count("apple"))

print()

fruits.reverse()
print("reverse fruits")
print(fruits)
