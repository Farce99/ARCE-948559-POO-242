#Clase Abstracta
class Person:
    def __init__(self,dni,name,lastname,age):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.age = age

class Student(Person):
    def __init__(self,dni,name,lastname,age,code):
        super().__init__(dni,name,lastname,age)
        self.code = code
        self.__subjects =[]

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def __str__(self):
        return f"Nombre: {self.name}, Codigo: {self.code}, Asignaturas: {self.__subjects}"


class Professor(Person):
    def __init__(self,dni,name,lastname,age,device,desktop):
        super().__init__(dni,name,lastname,age)    
        self.device = device
        self.desktop = desktop

    def __str__(self):
        return f"Nombre: {self.name}, Dispositivo: {self.device}, Puesto a trabajar: {self.desktop}"

student_1 = Student(1234, "luis","soto",21,12233)
professor_1 = Professor(1234, "james","montaño",31,"laptop",16)

student_1.add_subject("Matemáticas")



print(student_1)
print(professor_1)
