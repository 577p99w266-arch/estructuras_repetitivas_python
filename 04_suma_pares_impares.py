print("SUMA DE PARES E IMPARES")

n = int(input("Ingresa un número entero positivo: "))
suma_pares = 0
suma_impares = 0

if n <= 0:
    print("El número debe ser mayor que cero.")
else:
    for numero in range(1, n + 1):
        if numero % 2 == 0:
            suma_pares += numero
        else:
            suma_impares += numero

    print(f"La suma de los números pares hasta {n} es: {suma_pares}")
    print(f"La suma de los números impares hasta {n} es: {suma_impares}")
