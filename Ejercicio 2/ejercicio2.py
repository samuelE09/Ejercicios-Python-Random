""" 
Un número palíndromo es un número (como el 626) que permanece igual cuando se invierten sus dígitos. 
Escribe una función que devuelva true si un número dado es un palíndromo, y false, si no lo es. 
Completa la función dada, para que el código en principal funcione y resulte en el resultado esperado. 

Ejemplo de entrada: 
13431 

Ejemplo de salida: 
13431 es un palíndromo

8888 es un palindromo

12345 no es palindromo
"""
def verify_palindrom(num):
    num_inverse = num[::-1]
    if num == num_inverse:
        return True
    else:
        return False
    
entry = input("Ingresa un numero: ")
resp = verify_palindrom(entry)

if resp: 
    print(f"{entry} es palindromo")
else:
    print(f"{entry} no es palindromo")


