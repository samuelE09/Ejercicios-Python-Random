"""
Nuevo Equipamiento de Futbol

Cada miembro de un equipo de futbol ha decidido encargar un par de nuevas botas. Necesitamos escribir un programa en el sea posible ingresar los nombres y tallas de los jugadores de futbol y, que se muestren las tallas de los jugadores usando sus nombres. Si la persona no existe, se debe mostrar "No existe dicha persona en el Equipo"
"""
def menu():
    print("======================")
    print("1.- Registrar Jugador")
    print("2.- Consultar Jugador")
    print("3.- Terminar Programa")
    print("======================")

class Team:
    def __init__(self, nombre, talla):
        self.nuevojugador = {}   
        self.nombre = nombre 
        self.talla = talla
          
    def add_player(self):
        self.nuevojugador["talla"] = self.talla
        self.nuevojugador["nombre"] = self.nombre
        players[self.nuevojugador["nombre"]] = self.nuevojugador
        
        
players = {
        'Juan': {'talla': '20', 'nombre': 'Juan'},
        'Pedro': {'talla': '32', 'nombre': 'Pedro'},
        'Martin': {'talla': '42', 'nombre': 'Martin'}}


while True:
    menu()
    resp = input("Que deseas Realizar? \n")
    if resp == "1":
        nombre = input("Nombre del jugador: ")
        talla = input("Talla del jugador: ")
        team = Team(nombre, talla)
        team.add_player()
        print("El jugador ha sido agregado satisfactoriamente...!")
    elif resp == "2":
        nombre = input("Nombre del jugador: ")
        if nombre in players:
            print("=====================")
            print(f"El jugador {nombre} existe en el equipo")
            print("=====================")
            print(f"Datos del Jugador {nombre}")
            print(f'Nombre : {players[nombre]["nombre"]}')
            print(f'Talla : {players[nombre]["talla"]}')
            print("=====================\n")
            
        else:
            print(f"No existe el jugador {nombre} en el equipo")
    elif resp == "3":
        print("Terminando el Programa......!")
        break
    else: 
        print("Ingrese una opcion valida \n")