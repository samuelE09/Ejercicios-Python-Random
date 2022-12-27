num_elementos = 0  #Inicializas una variable de la cantidad de elementos de la lista
count_positivo = 0 #Inicializas el contador de numeros positivos
count_negativo = 0 #Inicializas el contador de numeros negativos

lista_numeros = [] #Inicializas una lista vacia

while num_elementos <= 6: # cantidad maxima de elementos en la lista es de 7 
    numero = int(input(f"Ingresa un numero {num_elementos} : ")) # Ingresas el numero
    lista_numeros.append(numero) #agregas ese numero a la lista vacia 
    
    if numero < 0: # validas el numero ingresado si es negativo
        count_negativo += 1 # aumentas el contador
    else: # validas el numero ingresado si es positivo
        count_positivo += 1 # aumentas el contador
        
    num_elementos += 1 #aumentas el contador en 1 la cantidad de elementos - se vuelve a repertir el ciclo hasta que sea igual a 6
        

# imprimes la lista a validar
print(f"Lista de números : {lista_numeros}")
# imprimes la cantidad de numeros positivos
print(f"Cantidad de números positivos : {count_positivo}") 
# imprimes la cantidad de numeros negativos
print(f"Cantidad de números negativos : {count_negativo}")