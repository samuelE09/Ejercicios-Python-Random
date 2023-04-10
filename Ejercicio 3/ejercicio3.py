""" 
Pedir el ingreso por teclado de 3 valores numericos enteros entre 1 y 10 correspondientes a las notas de un alumno.
En base al promedio final de las tres notas, mostrar un mensaje por pantalla que indique si el alumno promociona la materia(nota final 7,8,9 o 10), debe rendir final(notal final 4,5o 6) o recursa (nota 1,2,3)
"""
alumno = input("Ingrese el nombre del Alumno: ")
num_notas = int(input("\nIngrese el numero de notas a registrar: "))
count = 1
lst_notas = []

while count <= num_notas:
    try:
        nota = float(input("\nIngrese la nota del alumno: "))
        if nota >= 1 and nota <=10 :
            lst_notas.append(nota)
            count += 1
        else:
            print("\n[!] Porfavor ingrese un numero entre 1 y 10")
            nota = float(input("Ingrese la nota del alumno: "))
            lst_notas.append(nota)
            count += 1
    except :
        print("Ingresa un valor valido")
        
print(f"\n[!] Lista de Notas del Alumno {alumno}")
print(lst_notas)

prom_final = sum(lst_notas)/len(lst_notas)
print(f"\n[!] Promedio Final - {alumno} es {prom_final}")

if prom_final <= 3:
    print(f"{alumno} tiene que recursar los cursos")
elif prom_final <= 6:
    print(f"{alumno} tiene que rendir final")
else:
    print(f"{alumno} tiene que promocionar la materia")