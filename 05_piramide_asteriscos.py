print("PIRÁMIDE DE ASTERISCOS")

altura = int(input("Ingresa la altura de la pirámide: "))

if altura <= 0:
    print("La altura debe ser mayor que cero.")
else:
    for fila in range(1, altura + 1):
        espacios = " " * (altura - fila)
        asteriscos = "*" * (2 * fila - 1)
        print(espacios + asteriscos)
