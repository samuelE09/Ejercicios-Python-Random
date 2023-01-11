
__author__ = "Samuel Berrú"
__version__ = "1.0.1"
__maintainer__ = "Samuel Berrú"
__github__ = "samuelE09"


"""
Ejercicio: JUEGO 1

Este es un juego tipico de preguntas y respuestas. Para ello, deberá crear una base de datos de 10 preguntas; por cada pregunta, se deberá tener 3 respuestas, donde solo una es correcta. Cuando el usuario active este juego, se seleccionarán 5 preguntas aleatoriamente para mostrarlas de forma secuencial al usuario. Se mostrará la pregunta y las 3 posibles respuestas. Posteriormente, se le preguntará al usuario su seleccion. Se hará un conteo de las veces que el usuario respondió de forma correcta a las preguntas. Cuando el usuario haya respondido a todas las preguntas , el programa calculará el porcentaje de aciertos (Acc). De acuerdo a este valor, se controlarán el led RGB y el servomotor de la siguiente manera: 

Para el RGB: 

- Si Acc < 50% , se mostrará el color Rojo
- Si Acc < 80% , se mostrará el color Amarillo
- Si Acc >= 80% , se mostrará el color Verde

Para el servomotor: 

- Si Acc < 50% , se moverá hacia la izquierda
- Si Acc >= 50% , se moverá hacia la derecha

"""

from juego1_data import trivia #importamos el archivo con las preguntas y respuestas
import random #importamos la libreria random para elegir preguntas al azar

# Inicializacion de variables

PREGUNTAS = [] # lista vacia para almacenar las preguntas elegidas
cant_preguntas = 5 # numero de preguntas que se presentaran al usuario
i=0  # contador para el ciclo while
resp_correctas = 0 # contador de respuestas correctas
resp_incorrectas = 0 # contador de respuestas incorrectas

# Elegimos las preguntas al azar
PREGUNTAS = random.sample(trivia, cant_preguntas)

# Iniciamos un try-except-finally para manejar la interrupcion del usuario
try:
    while True:
        # Mostramos cada pregunta y sus respuestas al usuario
        for item in PREGUNTAS:
            print(item["pregunta"])
            for alternativa, respuesta in enumerate(item["respuestas"]):
                print(f"{alternativa}.- {respuesta}")
                
            # Validamos que el usuario ingrese una respuesta valida  
            while True:
                try:
                    resp = int(input("¿Cual es la Alternativa Correcta? : "))
                    
                    # Validamos que la respuesta sea un numero entero dentro del rango de respuestas
                    if resp in range(len(item["respuestas"])):
                        break
                    else:
                        print("Por favor ingrese una alternativa válida.")
                        
                except ValueError:
                    print("Por favor ingrese un número entero")
                    
            # comparamos si la respuesta es correcta y aumentamos el contador correspondiente
            if item["respuestas"][resp] == item["resp_correcta"]:
                print("¡Respuesta correcta! \n")
                resp_correctas += 1
            else:
                print(f"Lo siento, la respuesta correcta era: {item['resp_correcta']} \n")
                resp_incorrectas += 1
                
        # calculamos el porcentaje de aciertos
        porc_aciertos = resp_correctas / cant_preguntas
        print(f"Porcentaje de aciertos: {porc_aciertos*100}%")
        
        # acciones a realizar segun el porcentaje de aciertos
        if porc_aciertos < 0.5:
            print("Led RGB: Rojo")
            # Codigo para mover el servomotor hacia la izquierda
        elif porc_aciertos < 0.8:
            print("Led RGB: Amarillo")
        else:
            print("Led RGB: Verde")
            # Codigo para mover el servomotor hacia la derecha
        break
    
except KeyboardInterrupt:
    print("\n\nEl usuario detuvo el programa.")

finally:
    print("\n\nLimpiando recursos y cerrando procesos...\n")