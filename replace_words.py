word = "vacasat"   
unknow = "_"*len(word)

letter = input("Ingresda una letra : ")
num_letras= word.count(letter)   # a  3 

#  v  a  c  a  s  a
#  0  1  2  3  4  5

if num_letras>0:
    indice = 0
    new_unknow = list(unknow)
    
    for i in range(num_letras):
        indice = word.index(letter, indice)
        new_unknow[indice] = letter
        print(f"La posicion: {indice}")
        indice += 1
    print(new_unknow)

else:
    print(word, unknow)
