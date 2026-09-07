print("FIZZBUZZ")

n = int(input("Ingresa un número entero positivo: "))

if n <= 0:
    print("El número debe ser mayor que cero.")
else:
    for numero in range(1, n + 1):
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)
