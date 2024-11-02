from abc import ABC

class Person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return f"name={self.name},age={self.age}"

class Student(Person):
    def __init__(self,name,age,code):
        super().__init__(name,age)
        self.code=code

student_1=Student("fabian",25,12345)
print(student_1)


