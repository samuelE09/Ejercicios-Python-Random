import random

class NIF: 
    def __init__(self, DNI = 0):
        self.DNI = DNI
        self.letra = ""
        
    def leer(self):
        abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
        if self.DNI == 0 and self.letra == "":
            return "NIF No valido"
        else:
            self.letra = random.choice(abc).upper()
            return f"{self.DNI}-{self.letra}"

nif = NIF("12345678")

print(nif.leer())