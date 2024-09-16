class Hero:
    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level

    def __repr__(self):
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"

class Knight(Hero):
    def __init__(self, name: str, level: int):
        super().__init__(name,level)

class Wizard(Hero):
    def __init__(self, name: str, level: int):
        super().__init__(name,level)

class Elf(Hero):
    def __init__(self, name: str, level: int):
        super().__init__(name,level)
        
hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
        
        