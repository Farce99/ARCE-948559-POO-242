class Person:
    def __init__ (self,dni,name,age):
        self.__dni = dni
        self.__name = name
        self.age = age

    def __str__ (self):
        return f"Person(name={self.__name},age={self.age})"

person_1 = Person(1234,"luis",20)

print(person_1)


class Productinventory:
    def __init__(self,product):
        self.product = product
        self.__stock = 0


    def add_stock(self, quantity):
        self.__stock += quantity

    def remove_stock(self,quantity):
        if quantity <=self.__stock:
            self.__stock -= quantity

    def show_stock(self):
        return f"Para el producto{self.product} hay un stock de {self.__stock}"

    def __str__(self):
        pass

inventory=Productinventory("Coca-cola")
inventory.add_stock(100)
inventory.remove_stock(20)


print(inventory.show_stock())



