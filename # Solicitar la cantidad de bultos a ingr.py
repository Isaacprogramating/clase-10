# Solicitar la cantidad de bultos a ingresar
cant_bultos = int(input("Ingrese la cantidad de bultos a procesar: "))

# Validar que la cantidad ingresada sea mayor a cero
while cant_bultos <= 0:
    print("La cantidad de bultos debe ser un número entero positivo.")
    cant_bultos = int(input("Ingrese la cantidad de bultos a procesar: "))

# Inicializar variables
nroBulto = 1
total_peso = 0
bultos_pesados = 0

# Procesar cada bulto
while nroBulto <= cant_bultos:
    peso_bulto = float(input(f"Ingrese el peso del bulto {nroBulto} en kilogramos: "))
    
    # Validar que el peso ingresado sea positivo
    while peso_bulto <= 0:
        print("El peso del bulto debe ser un número positivo.")
        peso_bulto = float(input(f"Ingrese el peso del bulto {nroBulto} en kilogramos: "))
    
    total_peso += peso_bulto
    
    # Verificar si el bulto es pesado
    if peso_bulto > 25:
        bultos_pesados += 1
    
    nroBulto += 1

# Calcular el peso promedio
peso_promedio = total_peso / cant_bultos

# Mostrar resultados
print(f"\nCantidad de bultos procesados: {cant_bultos}")
print(f"Peso total de los bultos: {total_peso:.2f} kilogramos")
print(f"Peso promedio de los bultos: {peso_promedio:.2f} kilogramos")
print(f"Cantidad de bultos pesados (más de 25 kg): {bultos_pesados}")