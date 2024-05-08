def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except (ValueError, TypeError):
        print("Error: Los valores ingresados no son válidos para la operación.")
    else:
        print(f"El resultado de la división es: {resultado}")

while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        dividir(num1, num2)
    except ValueError:
        print("Error: Los valores ingresados no son números válidos.")
    
    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != "s":
        break

print("Programa finalizado.")