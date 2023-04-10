"""Escribe un programa que pueda calcular el area de 3 figuras geometricas, triangulo, rectangulo y circulo. En primer lugar pegunta de que figura se quiere calcular el area, despues solicita los datos que necesites para calcularlo."""
from math import pi

def area_triangulo(b,h):
    area = (b*h)/2
    return area

def area_rectangulo(b,h):
    area = b*h
    return area

def area_circulo(r):
    area = pi*(r**2)
    return area

def menu():
    print("======================")
    print("1.- Area del Triangulo")
    print("2.- Area del Rectangulo")
    print("3.- Area del Circulo")
    print("4.- Terminar Programa")
    print("======================")

if __name__ == "__main__": 
    while True:
        menu()
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            print("======================")
            print("Calculando el Area del Triangulo")
            base= float(input("Ingrese la base del Triangulo: "))
            altura= float(input("Ingrese la altura del Triangulo: "))
            area = area_triangulo(base,altura)
            print(f"El Area del Triangulo es: {area}\n")
            
        elif opcion == "2":
            print("======================")
            print("Calculando el Area del Rectangulo")
            base= float(input("Ingrese la base del Rectangulo: "))
            altura= float(input("Ingrese la altura del Rectangulo: "))
            area = area_rectangulo(base,altura)
            print(f"El Area del Rectangulo es: {area}\n")
            
        elif opcion == "3":
            print("======================")
            print("Calculando el Area del Circulo: ")
            radio= float(input("Ingrese el radio del Circulo: "))
            area = area_circulo(radio)
            print(f"El Area del Circulo es: {area}\n")
            
        elif opcion == "4":
            print("\nTerminando el programa......! ")
            break
        else: 
            print("\nElije una opcion valida......! ")