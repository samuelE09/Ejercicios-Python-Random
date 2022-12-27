# Pedir al usuario el número de jugadores
num_players = int(input("Ingresa el número de jugadores: "))

# Crear una lista vacía para almacenar los nombres de los jugadores
players = []

# Pedir al usuario que ingrese el nombre de cada jugador
for i in range(num_players):
    name = input(f"Ingresa el nombre del jugador {i+1}: ")
    players.append(name)

# Si el número de jugadores es impar, agregar un "fantasma" a la lista
if num_players % 2 != 0:
    players.append("Fantasma")

# Crear las parejas utilizando la función zip()
pairs = list(zip(players[::2], players[1::2]))

# Imprimir las parejas creadas
for i, pair in enumerate(pairs):
    print(f"Pareja {i+1}: {pair[0]} y {pair[1]}")
