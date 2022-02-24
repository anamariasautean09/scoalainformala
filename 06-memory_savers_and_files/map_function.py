def adunare(n):
    return n + n

lista_numere = [1, 2, 3, 4]
lista_numere_2 = [5, 6, 7, 8]
rezultat = map(adunare, lista_numere)
print(list(rezultat))

rezultat1 = map(lambda n: 2 * n, lista_numere)
print(list(rezultat1))

rezultat1 = map(lambda n, m: n + m, lista_numere, lista_numere_2)
print(list(rezultat1))