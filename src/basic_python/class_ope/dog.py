"""
错误的 不应该当做类变量
"""
from src.basic_python.class_ope.animals import Animals

class Dog(Animals):

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('fido')
e = Dog('Buddy')
d.add_trick('role over')
e.add_trick('play dead')
print(d.tricks)  # ['role over', 'play dead']



