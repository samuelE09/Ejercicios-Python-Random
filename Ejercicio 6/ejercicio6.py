""" 
Ejercicio 6

Escribir una clase en python que obtenga todos los posibles subconjuntos únicos de un conjunto de números enteros distintos. 
Entrada: [4, 5, 6]
Salida: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

"""

# Forma 1 
class Subconjuntos1:
    def obtener_subconjuntos(self, conjunto):

        resultado = [[]]

        #conjunto = [4, 5, 6]

        for i in conjunto:
          n = len(resultado)
          for j in range(n):
            resultado.append(resultado[j] + [i])
        return resultado
    
# Forma 2
class Subconjuntos2:
    def obtener_subconjuntos(self, conjunto):
        respuesta = [[]]

        for i in conjunto:
            respuesta += [j + [i] for j in respuesta]
            
        return respuesta

if __name__ == "__main__":
    
    conjunto = [4, 5, 6]
    
    # Forma 1
    subconjuntos1 = Subconjuntos1()
    resultado1 = subconjuntos1.obtener_subconjuntos(conjunto)
    print(resultado1) # [[], [4], [5], [4, 5], [6], [4, 6], [5, 6], [4, 5, 6]]
    
    # Forma 2
    subconjuntos2 = Subconjuntos2()
    resultado2 = subconjuntos2.obtener_subconjuntos(conjunto) 
    print(resultado2) # [[], [4], [5], [4, 5], [6], [4, 6], [5, 6], [4, 5, 6]]