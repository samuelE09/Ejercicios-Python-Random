
try:
    entry = int(input("Ingresa un número: "))
    for num in range(entry):
        if num % 2 == 0:
            print(f" {num} es par")
        else:
            print(f" {num} es impar")   
except ValueError:
    print("Por favor ingresa un numero Valido")

    