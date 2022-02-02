#2 variabile
#operator
#rezultat


def suma(a: int, b: int) -> str:
    return f"{a} + {b} = {a + b}"

def diferenta(a: int, b: int) -> str:
    return f"{a} - {b} = {a - b}"

def inmultire(a: int, b: int) -> str:
    return f"{a} * {b} = {a * b}"

def impartire(a: int, b: int) -> str:
    if b == 0:
        while b == 0:
            b = int(input("Aloca o noua valoare pentru al doilea operator"))
    return f"{a} / {b} = {a/b}"


def operator() -> str:
    op = input("alege operatorul: ")
    if op in ["+", "-", "*", "/"]:
        return op
    else:
        while op not in ["+", "-", "*", "/"]:
            op = input("alege operaotrul:")
    return op

def calculator():
    nr1 = int(input("Primul numar: "))
    nr2 = int(input("Al doilea numar: "))
    op = operator()
    if op == "+":
        rezultat = suma(nr1, nr2)
    elif op == "-":
        rezultat = diferenta(nr1, nr2)
    elif op == "*":
        rezultat = inmultire(nr1, nr2)
    else:
        rezultat = impartire(nr1, nr2)
    return rezultat

print(calculator())