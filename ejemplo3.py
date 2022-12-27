tema = input("Ingrese un tema : ")

opcion1 = input( "Seleciona una opcion: \n 1.- Estoy Informado \n 2.- No sé  \n " )

if opcion1 == "1":
    print("Procedo a Comentar sobre el Tema")
else: 
    opcion2 = input("Seleciona una opcion: \n 1.- Me voy a informar \n 2.- Estoy Callado \n " ) 
    if opcion2 == "2":
        print("Estoy Callado")
    else:
        opcion3 = input("Seleciona una opcion: \n 1.- He entendido \n 2.- Todavia no entiendo \n " )
        while opcion3 == "2":
            opcion3 = input("Seleciona una opcion: \n 1.- He entendido \n 2.- Todavia no entiendo \n " )
        if opcion3 == "1":
            print("Procedo a Comentar sobre el Tema")