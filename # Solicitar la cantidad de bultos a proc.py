# Solicitar la cantidad de bultos a procesar
cant_bultos = int(input("Ingrese la cantidad de bultos a procesar: "))

# Validar que la cantidad de bultos sea mayor a cero
while cant_bultos <= 0:
    print("La cantidad de bultos debe ser un número entero positivo.")
    cant_bultos = int(input("Ingrese la cantidad de bultos a procesar: "))

# Inicializar variables
nroBulto = 1
total_peso = 0
bultos_pesados = 0
bultos_livianos = 0

# Procesar cada bulto
while nroBulto <= cant_bultos:
    peso_bulto = float(input(f"Ingrese el peso del bulto {nroBulto} en kilogramos: "))

    # Validar que el peso del bulto sea positivo
    while peso_bulto <= 0:
        print("El peso del bulto debe ser un número positivo.")
        peso_bulto = float(input(f"Ingrese el peso del bulto {nroBulto} en kilogramos: "))

    # Sumar el peso del bulto al total
    total_peso += peso_bulto

    # Determinar si el bulto es pesado o liviano
    if peso_bulto > 25:
        bultos_pesados += 1
    else:
        bultos_livianos += 1

    nroBulto += 1

# Calcular el peso promedio
peso_promedio = total_peso / cant_bultos

# Mostrar los resultados
print(f"\nCantidad de bultos procesados: {cant_bultos}")
print(f"Peso total de los bultos: {total_peso:.2f} kilogramos")
print(f"Peso promedio de los bultos: {peso_promedio:.2f} kilogramos")
print(f"Cantidad de bultos pesados (más de 25 kg): {bultos_pesados}")
print(f"Cantidad de bultos livianos (25 kg o menos): {bultos_livianos}")