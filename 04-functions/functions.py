#print("mesaj")
#format()
# a = input("valoare de la tastatura")

#def functia_mea(param_1):
# pass

def suma(a:int , b:int, c:int = 3) -> (int, int):
    """
    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum of params, dif of params
    """
    return a + b + c, a - b -c;


#apelare functie
variabila_1 = 1
variabila_2 = 2
sum,dif = suma(a=variabila_1, b=variabila_2)
print(sum,dif)

