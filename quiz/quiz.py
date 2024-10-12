class Coche:
    def __init__ (self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __repr__(self):
        return f"Coche(marca={self.marca}, modelo={self.modelo}, año={self.año})" 

    def __str__(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"



coche_1 = Coche("Toyota", "Corolla", 2022)

print(coche_1)


class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito de {monto} realizado con éxito.")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro de {monto} realizado con éxito.")
        else:
            print("Fondos insuficientes o monto inválido.")

    def mostrar_saldo(self):
        return f"Saldo actual: {self.__saldo}"

cuenta = CuentaBancaria("Juan Perez")

cuenta.depositar(1000)
cuenta.retirar(500)

print(cuenta.mostrar_saldo())
