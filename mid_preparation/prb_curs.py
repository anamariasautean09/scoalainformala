# Sa se verifice daca doua stringuri sunt anagrame

def verify(str1, str2):
    if sorted(str1) == sorted(str2):
        return "String-urile introduse sunt anagrame."
    return "String-urile introduse NU sunt anagrame."


# str1 = input("Introduceti primul string: ")
# str2 = input("Introduceti al doilea string: ")
# print(verify(str1, str2))

# Sa se elimine toate duplicatele dintr-o lista

# def my_function(x):
#   return list(dict.fromkeys(x))
#
# mylist = my_function(["a", "b", "a", "c", "c"])
# print(mylist)

#  Sa se verifice daca un string este palindrom

def palindrom(string):
    if string[::-1] == string:
        return "String-ul este palindrom!"
    return "String-ul nu e palindrom!"


# str_palindrom = input("Introduceti un string: ")
# print(palindrom(str_palindrom))


# Sa se verifice ce numere lipsesc dintr-un interval
def find_missing(lista):
    return [x for x in range(lista[0], lista[-1] + 1)
            if x not in lista]


lista = [1, 2, 4, 6, 7, 9, 10]
# print(find_missing(lista))

# Sa se afiseze inversul unul string

def reverse_str(string):
    rev = string[::-1]
    return f"Inversul string-ului este {rev}."

# str_reverse = input("Introduceti un string: ")
# print(reverse_str(str_reverse))

# Sa se afiseze toate permutarile dintr-un string

from itertools import permutations

lista1 = [''.join(p) for p in permutations('day')]

print(lista1)