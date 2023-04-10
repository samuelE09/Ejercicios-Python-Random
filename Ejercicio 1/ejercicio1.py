"""
Realizar u algoritmo que permita realizar el calculo del tiempo en dias de entrega de un proyecto de software con las siguientes consideraciones

* El numero de programadores y sus horas trabajadas es variable, se define a la hora de contratacion, considerar que como minimo se deben tener 4 programadores y con 3 horas diarias cada uno.
* Las horas claculadas para el desarrollo del proyecto total son: 1500 horas.
"""
import math

MAX_PROGRAMADORES = 4
MAX_HORAS = 3
HORAS_PROYECTO = 1500


lst_programdores = []
lst_horas = []

num_programadores = int(input("Ingresa el numero de programadores: "))
count=1

if  num_programadores >=4 :
    while count <= num_programadores:
        programador = input("Ingresa el nombre del programador: " )
        lst_programdores.append(programador)
        horas_trabajo = int(input("Ingresa las Horas que Trabajará: "))
        while horas_trabajo < 3:
            horas_trabajo = int(input("Ingresa las Horas que Trabajará: "))
        else:
            lst_horas.append(horas_trabajo)
        count += 1
else:
    print(f"El proyecto debe tener minimo 4 programadores")
    
total_horas = sum(lst_horas)
total_dias = math.ceil(HORAS_PROYECTO/total_horas)

print(f"El proyecto se realizará con {len(lst_programdores)} programadores trabajando {total_horas} horas por dia en un tiempo de {total_dias} dias")