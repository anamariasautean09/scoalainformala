# numele clasei cu CamelCase si litera mare la inceput
# pt mostenire NumeClasa()  ---> neaparat paranteze
# class MyFirstClass:
#     pass
#
# my_first_object = MyFirstClass()

# class Caine:
#     nr_picioare = 4
#     # atribut declarat la nivel de clasa
#
#     def __init__(self, name, age):
#         self.nume = name
#         self.varsta = age
#
#     def __str__(self):
#         return f"{self.nume} - {self.varsta}"
#
#     def schimba_nume(self, name):
#         self.nume = name
#
#     def schimba_varsta(self, age):
#         self.varsta = age


# print(Caine.nr_picioare)


# cainele_meu = Caine("Rex", "2")
# # print(cainele_meu.nume)
# # print(cainele_meu.schimba_nume("Ben"))
# print(cainele_meu.varsta)


class Calculator:

    def __init__(self, op1, op2, operation):
        self.operator1 = op1
        self.operator2 = op2
        self.operatie = operation

    def adunare(self):
        return self.operator1 + self.operator2

    def scadere(self):
        return self.operator1 - self.operator2

    def inmultire(self):
        return self.operator1 * self.operator2

    def impartire(self):
        return self.operator1 / self.operator2

    def __str__(self):
        if self.operatie == '+':
            return f"{self.adunare()}"
        if self.operatie == '-':
            return f"{self.scadere()}"
        if self.operatie == '*':
            return f"{self.inmultire()}"
        if self.operatie == '/':
            return f"{self.impartire()}"


nr1 = int(input("Introduceti primul operator: "))
nr2 = int(input("Introduceti al doilea operator: "))
simbol_operatie = input("Introduceti tipul operatiei: ")

calcul = Calculator(nr1, nr2, simbol_operatie)
print(calcul)
