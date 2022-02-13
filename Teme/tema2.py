# EX1: Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă numere întregi sau reale.

def function(*args, **kargs):
    sum = 0
    for elem in args:
        type_of_elem = type(elem)
        if type_of_elem == int or type_of_elem == float:
            sum = sum + elem
    return sum


print("Funcție care primește un număr nedefinit de parametrii: \n")
# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
print(function(1, 5, -3, "abc", [12, 56, "cad"]))

# ○ your_function() va returna 0.
print(function())

# ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).
print(function(2, 4, "abc", param_1=2))

print("\n")

#
# # EX2:  Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:

# ○ suma tuturor numerelor de la [0, n]
def sum_recursiv(n: int) -> int:
    if n == 0:
        return 0

    return n + sum_recursiv(n - 1)

x = int(input("Introduceti o valoare pentru n: "))
print(f"Suma primelor {x} numere este: ", sum_recursiv(x))
print("\n")

print(f"Suma numerelor, calculata recursiv, din intervalul [0,n] este:")
print("Suma numerelor este egala cu: ")
print(sum_recursiv(10))  # va afisa 55

print("Suma numerelor este egala cu: ")
print(sum_recursiv(7))  # va afisa 28
print("\n")

# ○ suma numerelor pare de la [0, n]

def sum_pare_recursiv(n: int)-> int:
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return n + sum_pare_recursiv(n - 1)
        else:
            return sum_pare_recursiv(n - 1)

y = int(input("Introduceti o valoare pentru n: "))
print(f"Suma primelor {y} numere pare este: ", sum_pare_recursiv(y))
print("\n")

print(f"Suma numerelor pare, calculata recursiv, din intervalul [0,n] este:")
print("Suma numerelor pare este egala cu: ")
print(sum_pare_recursiv(10))  # va afisa 30
print("Suma numerelor pare este egala cu: ")
print(sum_pare_recursiv(7))  # va afisa 12
print("\n")

# # ○ suma numerelor impare de la [0. n]
def sum_impare_recursiv(n):
    if n == 0:
        return 0
    else:
        if n % 2 !=0 :
            return n + sum_impare_recursiv(n-1)
        else:
            return sum_impare_recursiv(n-1)

z = int(input("Introduceti o valoare pentru n: "))
print(f"Suma primelor {z} numere impare este: ", sum_impare_recursiv(z))
print("\n")

print(f"Suma numerelor impare, calculata recursiv, din intervalul [0,n] este:")
print("Suma numerelor impare este egala cu: ")
print(sum_impare_recursiv(10)) #va afisa 25
print("Suma numerelor impare este egala cu: ")
print(sum_impare_recursiv(7)) #va afisa 16


# #  EX3: Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează valoarea 0.

def my_function():
    n = input("Introduceti ceva: ")
    if n.isnumeric() == True:
        return n
    else:
        return 0

print(my_function())
