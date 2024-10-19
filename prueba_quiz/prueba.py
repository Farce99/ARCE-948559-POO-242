class Persona:
    def __init__ (self, nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre (self):
        return self.__nombre
    
    def set_nombre (self,modificar_nombre):
        self.__nombre = modificar_nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self,modificar_Edad):
        if modificar_Edad>0:
            self.__edad = modificar_Edad
        
persona1= Persona("fabian",25)
persona1.set_edad(30)
persona1.set_nombre("andres")

print (persona1.get_nombre())
print (persona1.get_edad())