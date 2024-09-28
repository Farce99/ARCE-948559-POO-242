from faker import Faker

fake = Faker()



class Person:
    def __init__(self,dni,name,lastname):
        self.dni=dni
        self.name=name
        self.lastname=lastname

    def __str__(self):
        return f"person(DNI={self.dni},name={self.name},lastname={self.lastname})"

    #numero de personas que vamos a crear
def generate_poeple(count):
    people=[]
    for _ in range (count):
        dni=fake.ssn()
        name=fake.first_name()
        lastname=fake.last_name()

        person = Person(dni,name,lastname)
        people.append(person)

    return people

# mostrar el contenido de la lista de personas
def get_poeple(people_list):
    for person in people_list:
        print(person)

number = int(input("por favor ingrese el numero de personas a agregar:\n "))
array_people=generate_poeple(number)
get_poeple(array_people)

#person1=person(dni="123",name="Fabian",lastname="Arce")

#print(person1)
