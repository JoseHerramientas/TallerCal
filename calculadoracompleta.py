# Función para sumar dos números
def suma(a, b):
    resultado = a + b
    return resultado

# Función para restar dos números
def resta(a, b):
    resultado = a - b
    return resultado

# Función para multiplicar dos números
def multiplicacion(a, b):
    resultado = a * b
    return resultado

# Función para dividir dos números
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    resultado = a / b
    return resultado

# Función para calcular la potencia de un número
def potencia(base, exponente):
    resultado = base ** exponente
    return resultado

# Función para calcular la raíz cuadrada de un número
def raiz_cuadrada(a):
    import math
    resultado = math.sqrt(a)
    return resultado

# Función para calcular el valor absoluto de un número
def valor_absoluto(a):
    resultado = abs(a)
    return resultado

# Función para calcular el porcentaje de un número
def porcentaje(numero, porcentaje):
    resultado = (numero * porcentaje) / 100
    return resultado

while True:
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Valor Absoluto")
    print("8. Porcentaje")
    print("0. Salir")

    opcion = input("Elija una operación (0/1/2/3/4/5/6/7/8): ")

    if opcion == "0":
        break

    if opcion in ("1", "2", "3", "4", "5", "6", "7", "8"):
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = suma(a, b)
        elif opcion == "2":
            resultado = resta(a, b)
        elif opcion == "3":
            resultado = multiplicacion(a, b)
        elif opcion == "4":
            resultado = division(a, b)
        elif opcion == "5":
            resultado = potencia(a, b)
        elif opcion == "6":
            resultado = raiz_cuadrada(a)
        elif opcion == "7":
            resultado = valor_absoluto(a)
        elif opcion == "8":
            resultado = porcentaje(a, b)

        print("Resultado: ", resultado)

    else:
        print("Opción no válida. Por favor, elija una opción válida.")
