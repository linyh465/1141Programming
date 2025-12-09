class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f"{self.name} the {self.breed} says Woof!"
        
        
name, breed = input().split()
dog = Dog(name, breed)
print(dog.bark())

