from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age

    #     @property
    #     def name(self):
    #         returnself.__name
        
    #     @name.setter
    #     def name (self,name):
    #         self.__name=name

    # def __str__ (self):
    #     return f"Person(name={self.__name},age={self.age})"


#contrato que si o si debe pasar
    @abstractmethod
    def sayHello(self):
        pass
