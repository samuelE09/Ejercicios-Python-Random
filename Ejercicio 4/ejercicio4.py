""" 
Diseñe un programa que genere numeros aleatorios enteros del intervalo 10 a 70 hasta obtener un numero par mayor a 35 pero menor que 45. El programa mostrará: 
    
- los numeros generados
- La suma de todos los numeros generados
- La cantidad de numeros generados del intervalo 10 a 30 
- la cantida de numeros generados del intervalo 31 a 50
- la cantidad de numeros generados del intervalo 51 a 70 
"""

import random

num_generados = []
lst_num10_30 = []
lst_num31_50 = []
lst_num51_70 = []

while True: 
    num = random.randint(10, 71)
    if num % 2 == 0 and num > 35 and num < 45:
        print(f"=====================================")
        print(f"El numero par es {num}\n")
        print(f"Fin del Programa\n")
        break
    elif num >= 10 and num <= 30:
        print(f"\nSe agrega el numero {num} a la lista\n")
        lst_num10_30.append(num)
    elif num >= 31 and num <= 50:
        print(f"\nSe agrega el numero {num} a la lista\n")
        lst_num31_50.append(num)
    else:
        print(f"\nSe agrega el numero {num} a la lista\n")
        lst_num51_70.append(num)
    
    num_generados.append(num)
        
print(f"=====================================")
print(f"Lista de todos los numero generados\n")
print(num_generados)
print(f"=====================================\n")
print(f"Suma de todos los numero generados\n")
print(f"La suma de los numeros generados es: {sum(num_generados)}")
print(f"=====================================\n")
print(f"Cantidad de Numeros Generados entre 10 y 30\n")
print(lst_num10_30)
print(f"La cantidad de numeros es de : {len(lst_num10_30)}")
print(f"=====================================\n")
print(f"Cantidad de Numeros Generados entre 31 y 50\n")
print(lst_num31_50)
print(f"La cantidad de numeros es de : {len(lst_num31_50)}")
print(f"=====================================\n")
print(f"Cantidad de Numeros Generados entre 51 y 70\n")
print(lst_num51_70)
print(f"La cantidad de numeros es de : {len(lst_num51_70)}")
print(f"=====================================\n")