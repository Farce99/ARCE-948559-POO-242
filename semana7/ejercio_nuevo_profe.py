alumnos = []
empleados = []
vigilancia = []

def agregar_individuo():
    while True:
        print("Seleccione su rol:")
        print("1. Alumno")
        print("2. Empleado")
        print("3. Vigilancia")
        print("4. Salir")
        
        eleccion = input("Ingrese el número correspondiente: ")
        
        if eleccion in ["1", "2", "3"]:
            nombre_completo = input("Ingrese su nombre: ")
            identificador = input("Ingrese su ID: ")
            años = input("Ingrese su edad: ")
            
            individuo = {
                "nombre": nombre_completo,
                "id": identificador,
                "edad": años,
                "rol": eleccion
            }
            
            if eleccion == "1":
                alumnos.append(individuo)
                print(f"Alumno {nombre_completo} registrado.\n")
            elif eleccion == "2":
                empleados.append(individuo)
                print(f"Empleado {nombre_completo} registrado.\n")
            elif eleccion == "3":
                vigilancia.append(individuo)
                print(f"Personal de vigilancia {nombre_completo} registrado.\n")
        
        elif eleccion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.\n")
            continue
        
        otra_entrada = input("¿Desea agregar otra persona? (si/no): ").lower()
        if otra_entrada != "si":
            break


agregar_individuo()

print("\nIndividuos registrados:")
print("Alumnos:", alumnos)
print("Empleados:", empleados)
print("Vigilancia:", vigilancia)