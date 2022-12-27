"""
Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano, elabore el algoritmo que permita obtener la distancia entre A y B.

Punto A (X1, Y1)
Punto B (X2, Y2)

distancia entre dos puntos: D(A,B) = sqrt( (X2 - X1)**2 + (Y2 - Y1)**2 )

Algoritmo: 

A(X,Y)

Ingresar coordenada Punto A - X1    A(X1, Y1)
Ingresar coordenada Punto A - Y1

Ingresar coordenada Punto B - X2    B(X2,Y2)
Ingresar coordenada Punto B - Y2

Hacer calculo matematico  (distancia entre dos puntos)

Imprimir Distancia entre los puntos

"""
import matplotlib.pyplot as plt
import math

print("----------------------------------------")
print("DISTANCIA ENTRE 2 PUNTOS A y B, en 2D.")
print("----------------------------------------")

X1 = float( input("Ingresar coordenada Punto A - X1 : "))
Y1 = float( input("Ingresar coordenada Punto A - Y1 : "))

X2 = float( input("Ingresar coordenada Punto B - X2 : "))
Y2 = float( input("Ingresar coordenada Punto B - Y2 : "))

distancia_A_B = round(math.sqrt( (X2 - X1)**2 + (Y2 - Y1)**2 ) , 2)

print("----------------------------------------")
print("--------------RESULTADO-----------------")
print(f" La distancia entre los puntos A({X1},{Y1}) y B({X2},{Y2}) es {distancia_A_B} ")

print("----------------------------------------")
print("--------------GRAFICANDO-----------------")

ejesX = [X1,X2]
ejesY = [Y1,Y2]

plt.plot(ejesX,ejesY,marker = 'o') # plot( ejes X , ejes Y ) 
plt.grid() 
plt.show()


