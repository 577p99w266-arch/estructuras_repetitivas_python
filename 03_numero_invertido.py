print("NÚMERO INVERTIDO")

numero = int(input("Ingresa un número entero: "))
signo = -1 if numero < 0 else 1
numero_temporal = abs(numero)
numero_invertido = 0

while numero_temporal > 0:
    digito = numero_temporal % 10
    numero_invertido = numero_invertido * 10 + digito
    numero_temporal //= 10

numero_invertido *= signo
print(f"El número invertido es: {numero_invertido}")
