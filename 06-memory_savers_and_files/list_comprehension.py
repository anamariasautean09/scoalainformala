# lista = []
# for item in 'Ana are mere':
#     lista.append(item)

# lista = [item for item in 'Ana are mere']
# print(lista)

lista = [e for i, e in enumerate('Ana are mere') if i % 2 == 0]
print(lista)

# my_numbers = [1, 2, 3, 4, 5]
# lista_numere = [item ** 2 for item in my_numbers if item % 2 == 0 ]

lista_produse = ['ciocolata', 'suc', 'mere', 'miere', 'apa']
lsta_noua = [x for x in lista_produse if 'a' in x]
print(lsta_noua)

lista = [x for x in range(10)]
print(lista)

lista1 = [x for x in range(10) if x < 5]
print(lista1)

#if one line


