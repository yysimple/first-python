class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

x = MyClass("wcx", 18)
print(x.name, x.age)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)


