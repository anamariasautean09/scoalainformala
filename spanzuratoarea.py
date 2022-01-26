#reguli
#daca primul caracter si ultimul se repetau in cuvant, caracterul trebuia afisat
#restul caracterelor ascunse
# 7 sanse de a ghici cuvantul
# word = o _ o _ _ _ o _ e e

word = 'onomataopee'
#litera_cuvant = input("alege o litera ")
#print(litera_cuvant)

lista_cuvant = []
for iterator in word:
    #print(iterator, word[0], word[-1])
    lista_cuvant.append('_')
    if iterator == word[0] or iterator == word[-1]:
        lista_cuvant[-1] = iterator
numar_incercari = 1

lista_litere_incercate = set()
while numar_incercari <= 7:
    litera = input("alegere o litera: ").lower()
    if litera in word:
        for index, valoare in enumerate(word):
            if valoare == litera:
                lista_cuvant[index] = litera
        #print("de adaugat in lista cuvant")
    else:
        if litera not in list(lista_litere_incercate):
            numar_incercari += 1
        lista_litere_incercate.add(litera)
        print(f"litera nu exista in cuvant "  f'deja ai incercat {",".join(lista_litere_incercate)}')
        print(f"mai ai {7 - numar_incercari} incercari")
    if 9 - int(numar_incercari) == 0:
        print(f"ai pierdut! Cuvantul era {word}")
    elif ''.join(lista_cuvant) == word:
        print("Ai castigat!")
        break
    else:
        print(' '.join(lista_cuvant))

