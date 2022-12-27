## Formato JSON  ---> sql APIS , analsis 

def kilos_libras(pes):
    libras = round(pes*2.20462,2)   ###  158 lb 
    return libras

option = int(input(" Elije una opcion: "))

data = {
    "dino1": {
        "pes":140,
        "long":2,
    },
    "dino2": {
        "pes":180,
        "long":5,
    },
    "dino3": {
        "pes":270,
        "long":4,
    },
    "dino4": {
        "pes":120,
        "long":16,
    }, 
}

if option == 1:
    nom = "Dino1"
    data_dino = data.get("dino1")  ### pes , long 
    print(data_dino)
    pes = data_dino["pes"]   ## dino4   pes=120
    long = data_dino["long"]
    pes_libras = kilos_libras(pes) 
    print(f"El dinosaurio {nom} pesa {pes_libras} libras , y mide {long} metros")
    
elif option == 2:
    nom = "Dino2"
    data_dino = data.get("dino2")  ### pes , long 
    print(data_dino)
    pes = data_dino["pes"]
    long = data_dino["long"]
    pes_libras = kilos_libras(pes) 
    print(f"El dinosaurio {nom} pesa {pes_libras} libras , y mide {long} metros")
    
elif option == 3:
    nom = "Dino3"
    data_dino = data.get("dino3")  ### pes , long 
    print(data_dino)
    pes = data_dino["pes"]
    pes_libras = kilos_libras(pes) 
    long = data_dino["long"]
    print(f"El dinosaurio {nom} pesa {pes_libras} libras , y mide {long} metros")
    
elif option == 4:
    nom = "Dino4"
    data_dino = data.get("dino4")  ### pes , long 
    print(data_dino)
    pes = data_dino["pes"]
    pes_libras = kilos_libras(pes) 
    long = data_dino["long"]
    print(f"El dinosaurio {nom} pesa {pes_libras} libras , y mide {long} metros")
    
else: 
    print("Dino no encontrado - Elije una opcion valida")      
        
        
        
    







