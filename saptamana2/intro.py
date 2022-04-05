print("Mesaj")
variabila_a_2 = 2
# variabila_a_3=None exista, dar nu are valoare, e doar declarata, ca un fel de NULL
print(variabila_a_2)
mesaj = '\tAna\'s are \n mere'
print(mesaj)
print(type(mesaj))
numar_mere= 2
numar_pere= 3
mesaj=f"Ana are {numar_mere} mere" #cea mai utilizata
mesaj="Ana are {1} mere si {1} pere". format(numar_mere, numar_pere)
mesaj="Ana are " + str(numar_pere) + " mere si " + str(numar_pere) + " pere"
print(mesaj)
lista = [2, 3, 4, "ana"]
print(len(lista))
print(lista[0])
print(lista[-1])
