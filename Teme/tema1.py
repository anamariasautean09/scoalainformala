
#declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("lista initiala")
print(lista)
print('\n')

# afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
print("lista ordonata ascendent")
lista.sort()
print(lista)
print('\n')

# afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
print("lista ordonata descendent")
lista.sort(reverse=True)
print(lista)
print('\n')

# afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
print("lista ordonata cu numerele pare")
lista.sort()
print(lista[1:10:2])
print('\n')

# afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
print("lista ordonata cu numerele impare")
lista.sort()
print(lista[0:9:2])
print('\n')

# afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice)
print("lista ordonata cu numerele multipli ai lui 3")
lista.sort()
print(lista[2:10:3])