# animal.py
class Animal:
    def eat(self):
        return "eating..."

# dog.py
from animal import Animal

class Dog(Animal):
    def bark(self):
        return "barking..."

# Testing the classes
dog = Dog()
print(dog.eat())  # Output: eating...
print(dog.bark())  # Output: barking...
