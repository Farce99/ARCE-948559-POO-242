# class Person:
#     def __init__(self,name,lastname,age,isMarriedwith,nationality="colombia"):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.isMarriedwith = isMarriedwith
#         self.nationality=nationality


#     def __repr__(self):
#         return f"Person(name={self.name},lastname={self.lastname},age={self.age},spose={self.isMarriedwith} nationality={self.nationality})"


# person_1 = Person(name="james", lastname="rodriguez", age="33",isMarriedwith="Daniela Ospina")

# print(person_1)

# class Person:
#     def __init__(self, name: str, lastname: str, age: int):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.isMarriedWith = None
#         self.nationality = None

#     def __str__(self):

#         return f"name={self.name}, spouse={spouse_name}"


#     def get_married(self, person: 'Person'):
#         self.isMarriedWith = person
#         person.isMarriedWith = self




# person_1 = Person(name='James', lastname='Rodriguez', age=33)
# person_2 = Person(name='Luis', lastname='Diaz', age=25)
# person_3 = Person(name='Luisa', lastname='Perez', age=24)


# person_1.get_married(person_3)
# # person_3.get_married(person_1)


# print(person_2)

class Person:
    def __init__(self, name: str, lastname: str, age: int):
        self.__name = name
        self.__lastname = lastname
        self.__age = age

    def get_name(self):
        return self.__name 

    def set_name(self,name):
        self.__name = name


    def get_lastname(self):
        return self.__lastname

    def set_lastname(self,lastname):
        self.__lastname = lastname


    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age


    def __repr__(self):
        return f"name={self.get_name()},lastname={self.get_lastname()},age={self.__age}"



person_1 = Person(name='James', lastname='Rodriguez', age=33)
person_2 = Person(name='Luis', lastname='Diaz', age=25)
person_3 = Person(name='Luisa', lastname='Perez', age=24)

person_1.set_name("Rodrigo") #para modificar

print(person_1)