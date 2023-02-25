""" 
La aplicación debe ejecutar las siguientes funciones.
1. En un ciclo pida esos datos para cada estudiante: primero la cédula y luego los otros valores para construir cada elemento del diccionario.
Verifique que el número de cédula no se repita para dos estudiantes.
El ciclo termina cuando en el número de cédula le den el valor 0.
2. Después del ciclo imprima el diccionario, una línea por cada elemento.
Ejemplo de un diccionario:
{ 1234567: [“José”, “Solano”, “Cartago”,90],
3456712: [“Carmen”, “Vargas”, “Turrialba”, 65}
3. Después permita que se consulte la información por estudiante.
El Usuario digitará una cedula y el programa debe presentar la información asociada
Este ciclo de consulta se repite hasta que consulten la cedula 0
4. Por último, debe recorrer el diccionario e imprimir solamente los estudiantes aprobados. Es decir, los que tengan la nota mayor a 70
"""

def menu():
    print("Bienvenidos")
    opciones = {"1":"Agregar Alumno",
                "2":"Consultar Alumno",
                "3":"Mostrar Estudiantes",
                "4":"Salir"}
    print('\n'.join(f"{id}:{valor}" for id, valor in opciones.items()))
    return opciones
    
def agregar(estudiantes):
    data = []
    cedula = input("Ingresa una cedula : ")
    while len(cedula) == 7:
        if cedula in estudiantes.keys():
            print("Cedula ya se encuentra Registrada")
            break
        elif cedula == "0":
           break
        else:
            nombre = input("Ingresa el Nombre : ")
            data.append(nombre)
            apellido1 = input("Ingresa el Apellido : ")
            data.append(apellido1)
            apellido2 = input("Ingresa la Residencia :")
            data.append(apellido2)
            nota = input("Ingresa la Nota : ")
            data.append(nota)
            estudiantes[cedula] = data
            
    return estudiantes , "Usuario Agregado"

def consulta(estudiantes):
    cedula = input("Ingresa la cedula a consultar : ")
    if cedula in estudiantes.keys():
        estudiante = estudiantes[cedula]
        msg = "Usuario Encontrado" 
    else:
        estudiante = []
        msg = "Usuario no Encontrado" 
    
    return estudiante, cedula, msg

def mostrar(estudiantes, id):
    
    if id  == "1": 
        data = []
        for estudiante  in estudiantes.items():
            if estudiante[1][3] > 70 : #Establece el umbral de nota aprobada
                data.append(estudiante)
        msg_header = "Lista de Aprobados"
        msg_content = f"Hay  {len(data)} Estudiantes Aprobados"
            
    elif id == "2":
        data = []
        for estudiante  in estudiantes.items():
            if estudiante[1][3] < 60 :  #Establece el umbral de nota desaprobada
                data.append(estudiante)
                
        msg_header = "Lista de Desaprobados"
        msg_content = f"Hay  {len(data)} Estudiantes desaprobados"
    else:
        data, msg_header, msg_content = {} , "Datos no Encontrados" , "Vuelve a realizar la Operacion"
        
    return dict(data), msg_header, msg_content
   
if __name__ == "__main__":
    
    try :
        estudiantes = { 
               "1234567": ["José" , "Solano", "Cartago",90],
               "3456712": ["Carmen", "Vargas", "Turrialba", 65]
            }
        opciones = menu()
        while True: 
            opcion = input("Ingresa una opcion: ")
            if opcion in opciones.keys():
                if  opcion == "1": 
                    estudiantes, msg  = agregar(estudiantes)
                    print(msg)
                    menu()
                elif  opcion == "2": 
                    estudiante, cedula, msg = consulta(estudiantes)
                    print(msg)
                    print(cedula)
                    print(estudiante)
                    menu()   
                elif  opcion == "3": 
                    id = input("Para Aprobados (1), Desaprobados(2) : ")
                    data, msg_header , msg_content = mostrar(estudiantes, id)
                    print(msg_header)
                    print(msg_content)
                    print(data)
                    menu()
                elif  opcion == "4":
                    print("Saliendo del Programa.....")
                    exit()
            else:
                print("Elije una opcion correcta")
                menu()
    except: 
        print("\n Saliendo del Programa........")
    
    