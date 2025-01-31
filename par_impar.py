########################################################
#                  Programa para Detectar              #
#                    si es par o impar                 #
########################################################

# Lectura del número entero
numero = int(input("Introduce un número: "))

########################################################

# Verificar si el número es par o impar
if numero % 2 == 0:
    print("########################################################")
    print(f"El número {numero} es par.")
    print("########################################################")
else:
    print("########################################################")
    print(f"El número {numero} es impar.")
    print("########################################################")
