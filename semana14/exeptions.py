while True:
    number_1=input("Digite un numero:\n")
    number_2=input("Digite otro numero:") 

    try:
        result=int(number_1)/int(number_2)
        print(f"el resultado es: {result}")

    # except ValueError:
    #     print("Por favor ingrese solo numeros")   

    # except ZeroDivisionError:
    #     print("No esta permitido dividir por cero")

    except Exception as e:
        print(f"Se produjo un error del tipo: {e}")

    finally:
        print("programa terminado")

  