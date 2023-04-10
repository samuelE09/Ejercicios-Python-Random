# **Ejercicio 6**

Escribir una clase en python que obtenga todos los posibles subconjuntos únicos de un conjunto de números enteros distintos.

* Entrada: [4, 5, 6]

* Salida: [ [ ], [ 6 ], [ 5 ], [5, 6], [ 4 ], [4, 6], [4, 5], [4, 5, 6] ]

## **Solución**

[Codigo de Solucion - ejercicio6.py](ejercicio6.py)


## **Explicacion**

conjunto = [ 4, 5, 6 ]

* Primera interacion

        resultado =  [ [] ]
        dato1 = 4 
        n = 1 

        - Primera iteracion n = 1

            j = 0
            add resultado = resultado[0] + [4]
                          = [ ] + [4]
                          = [4]

            


* Segunda interacion

        resultado = [ [] , [4] ]
        dato1 = 5 
        n = 2 

        - Primera iteracion n = 2
            j = 0
            add resultado = resultado[0] + [5]
                          = [ ] + [5]
                          = [5]
            resultado = [ [] , [4] , [5] ]

        - Segunda iteracion n = 2
            j = 1
            add resultado = resultado[1] + [5]
                          = [4] + [5]
                          = [ 4, 5]
            resultado = [ [] , [4] , [5] , [4,5]  ] 
            

* Tercera interacion

        resultado = [ [] , [4] , [5] , [4,5]  ]
        dato1 = 6 
        n = 4 

        - Primera iteracion n = 4
            j = 0
            add resultado = resultado[0] + [6]
                          = [ ] + [6]
                          = [6]
            resultado = [ [] , [4] , [5] , [4,5] , [6] ] 

        - Segunda iteracion n = 4
            j = 1
            add resultado = resultado[1] + [6]
                          = [ 4 ] + [6]
                          = [ 4, 6]
            resultado = [ [] , [4] , [5] , [4,5] , [6] , [4,6] ]


        - Tercera iteracion n = 4
            j = 2
            add resultado = resultado[2] + [6]
                          = [5] + [6]
                          = [ 5, 6]
            resultado = [ [] , [4] , [5] , [4,5] , [6] , [4,6] , [5,6] ]

        - Cuarta iteracion n = 4
            j = 3
            add resultado = resultado[3] + [6]
                          = [ 4,5 ] + [6]
                          = [ 4, 5 , 6]
                          
            resultado = [ [] , [4] , [5] , [4,5] , [6] , [4,6] , [5,6] , [ 4, 5 , 6]] 

## **Resultado Final** 

**Conjunto de Entrada** = [4,5,6]

**Subconjuntos Salida** = [ [] , [4] , [5] , [4,5] , [6] , [4,6] , [5,6] , [ 4, 5 , 6]] 



