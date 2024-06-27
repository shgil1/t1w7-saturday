class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def bark(self):
        return f"{self.name} says Woof!"
    
my_dog = Dog("Buddy", "Golden Retriever", "golden")
neighbors_dog = Dog("Bella", "Labrador", "Black")


# Fetching the attributes of the class using objects
print(my_dog.name)

print(my_dog.bark())

print(neighbors_dog.bark())