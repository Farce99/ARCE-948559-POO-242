# Clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = True

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    def __str__(self):
        return f"'{self.__titulo}' por {self.__autor}"

    def __repr__(self):
        return f"Libro(titulo='{self.__titulo}', autor='{self.__autor}', isbn='{self.__isbn}', disponible={self.__disponible})"

class Miembro:
    def __init__(self, nombre, identificacion):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__libros_prestados = []

    def agregar_libro(self, libro):
        if libro.prestar():
            self.__libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            libro.devolver()
            self.__libros_prestados.remove(libro)
            return True
        return False

    def __str__(self):
        return f"{self.__nombre} (ID: {self.__identificacion})"

    def __repr__(self):
        libros = ', '.join([str(libro) for libro in self.__libros_prestados])
        return f"Miembro(nombre='{self.__nombre}', identificacion='{self.__identificacion}', libros_prestados=[{libros}])"

class MiembroVIP(Miembro):
    def __init__(self, nombre, identificacion, limite_prestamos=10):
        super().__init__(nombre, identificacion)
        self.__limite_prestamos = limite_prestamos

    def agregar_libro(self, libro):
        if len(self._Miembro__libros_prestados) < self.__limite_prestamos:
            return super().agregar_libro(libro)
        else:
            print(f"{self} ha alcanzado el límite de préstamos ({self.__limite_prestamos}).")
            return False

    def __repr__(self):
        return f"MiembroVIP(nombre='{self._Miembro__nombre}', identificacion='{self._Miembro__identificacion}', limite_prestamos={self.__limite_prestamos}, libros_prestados=[{', '.join(map(str, self._Miembro__libros_prestados))}])"

def prueba_sistema_biblioteca():
    libro1 = Libro("Alas de Hierro", "Rebecca Yaros", "12345")
    libro2 = Libro("Alas de Sangre", "Rebecca Yaros", "67890")

    miembro1 = Miembro("Fabian Arce", "001")
    miembro_vip = MiembroVIP("Nicolas Oviedo", "002", limite_prestamos=1)

    print(f"\nPréstamo de {libro1} por {miembro1}: {'Éxito' if miembro1.agregar_libro(libro1) else 'Fallido'}")
    print(f"Préstamo de {libro2} por {miembro_vip}: {'Éxito' if miembro_vip.agregar_libro(libro2) else 'Fallido'}")

    print(f"Préstamo adicional de {libro1} por {miembro_vip}: {'Éxito' if miembro_vip.agregar_libro(libro1) else 'Fallido'}")

    print(f"\nDevolución de {libro1} por {miembro1}: {'Éxito' if miembro1.devolver_libro(libro1) else 'Fallido'}")

    print("\nRepresentación de objetos:")
    print(miembro1)
    print(repr(miembro1))
    print(miembro_vip)
    print(repr(miembro_vip))

prueba_sistema_biblioteca()
