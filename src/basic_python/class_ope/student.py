class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("hello world")


student = Student("wcx", 18)
student.sayHello()
print(student.name, student.age)
