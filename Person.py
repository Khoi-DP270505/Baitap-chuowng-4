# person.py và child.py gộp chung

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

# test code
person = Person("Peter", 25)
child = Child("Peter Junior", 5)

print(person.name)  # Output: Peter
print(person.age)   # Output: 25
print(child.__class__.__bases__[0].__name__)  # Output: Person
