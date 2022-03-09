# 1. Scrie un program care sa calculeze suma dintre trei numere.
# Daca valorile sunt egale, returnati de trei ori suma acestora.(1 punct)

def sum3(a, b, c):
    sum = 0
    if a == b == c:
        sum = a + b + c
        return f"{3 * sum} sau {sum} {sum} {sum}"
    return a + b + c

num1 = int(input("Introduceti primul numar: "))
num2 = int(input("Introduceti al doilea numar: "))
num3 = int(input("Introduceti al treilea  numar: "))

print(sum3(num1,num2,num3))

