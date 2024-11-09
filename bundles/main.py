from models.student import Student
from models.professor import Professor

person_1=Student(
    name="Fabian",
    lastname="Arce",
    age=25,
    code=2310
)

print(person_1.sayHello())


professor_1=Professor(
    name="Andres",
    lastname="Gordillo",
    age=25
)

print(professor_1.sayHello())