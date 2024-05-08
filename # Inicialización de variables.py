# Inicialización de variables
bultos_livianos = 0
bultos_normales = 0
total_pagar_livianos = 0
total_pagar_normales = 0

# Solicitar la cantidad de bultos
cantidad_bultos = int(input("Ingrese la cantidad de bultos: "))

# Procesar cada bulto
for i in range(cantidad_bultos):
    while True:
        try:
            peso_bulto = float(input(f"Ingrese el peso del bulto {i+1} (en kg): "))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    # Determinar la categoría del bulto
    if peso_bulto >= 1 and peso_bulto <= 5:
        bultos_livianos += 1
        total_pagar_livianos += 1000
    elif peso_bulto >= 6 and peso_bulto <= 10:
        bultos_normales += 1
        total_pagar_normales += 2000
    else:
        print(f"El bulto {i+1} no se encuentra en las categorías establecidas.")

# Imprimir resultados
print("\nResultados:")
if bultos_livianos > 0:
    print(f"{bultos_livianos} bulto(s) liviano(s) $1,000 c/u = ${total_pagar_livianos}")
if bultos_normales > 0:
    print(f"{bultos_normales} bulto(s) normal(es) $2,000 c/u = ${total_pagar_normales}")

total_pagar = total_pagar_livianos + total_pagar_normales
print(f"\nValor total a pagar: ${total_pagar}")