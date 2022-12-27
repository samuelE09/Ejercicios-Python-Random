#definir una funcion que haga el cambio de moneda de soles a dollar 

def conversor(moneda_soles):
    dollar = moneda_soles / 3.48  
    return dollar 


def pasaje(distancia_ida):
    costo_boleto = (distancia_ida * 2) * 0.17
    return costo_boleto
    
    

distancia_ida = int(input("Ingresa distancia de ida : "))  ## variables globales
moneda_soles = float(input("Ingresa moneda : "))
valor_convertido = conversor(moneda_soles)

valor_pasaje = pasaje(distancia_ida) * 0.70


print(valor_convertido)
print(valor_pasaje)


