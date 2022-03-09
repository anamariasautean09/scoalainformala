# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3
# pana cand lista devine goala. (1 punct)

lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def remove_delete(lista):

    while lista != []:
        print(f"Elementele care vor fi sterse sunt: {lista[::3]}")
        for i in lista[::3]:
            lista.remove(i)
        print(f"Lista ramasa: {lista} \n")
    return f"Lista este goala"

print(remove_delete(lista))





