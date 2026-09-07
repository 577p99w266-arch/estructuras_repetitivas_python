print("CONTADOR DE DÍGITOS")

numero = int(input("Ingresa un número entero: "))
numero_temporal = abs(numero)
cantidad_digitos = 0

if numero_temporal == 0:
    cantidad_digitos = 1
else:
    while numero_temporal > 0:
        numero_temporal //= 10
        cantidad_digitos += 1

print(f"El número {numero} tiene {cantidad_digitos} dígito(s).")
