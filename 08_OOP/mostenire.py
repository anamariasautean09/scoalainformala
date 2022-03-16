# Exemplul 1
# 1. vehicul
# 1.1 vehicule de apa
# 1.2 vehicule de aer
# 1.3 vehicul de spatiu
# 1.4 vehicul terestru
# 1.4.1 vehicul de teren
# 1.4.2 vehicul de curse

# 1. este super clasa pentru 1.1 -> 1.4
# 1.1 -> 1.4 este subclasa pentru 1

# Exemplul 2
# 2. Animale
# 2.1 mamifere
# 2.1.1 animale salbaticr
# 2.1.2 animale domestice
# 2.2 reptile

# 2. este super clasa pentru 2.1 si 2.2
# 2.1 si 2.2 subclase pentru 2
# 2.1.1 si 2.1.2 subclase pentru 2.1
# 2.1.1 si 2.1.2 subclase pentru 2

# Max este un caine mare care doarme toata ziua.
# obiectul -> Max (substantiv)
# clasa -> caine (substantiv)
# proprietatea -> mare (adjectiv)
# activitatea: doarme (verb) -> metoda

# Un logan masina verde merge incet .
# obiectul -> logan
# clasa -> masina
# proprietatea -> verde
# activitatea-> merge -> metoda

# Lenovo-ul gri se poate cumpara la un pret mai mic de pe un magazin online.
# obiectul -> Lenovo
# clasa -> laptop
# proprietatea -> gri
# activitatea-> se poate cumpara -> metoda

# x&0 intre 2 jucatori
# primul jucator este mereu calculator
# exista reguli de joc pt mutari
# obiecte -> calculator/player
# clasa -> jocul
# proprietate -> primul jucator este mereu calculatorul
# activitate -> mutarile/ calculul scorului

# class MyFirstClass:
#     pass
#
# my_object = MyFirstClass()

# stack = []
#
# def push(value):
#     stack.append(value)
#     return stack
#
# def pop():
#     value = stack[-1]
#     del stack[-1]
#     return value

# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())


# class Stack:
#
#     def __init__(self):
#         self.__stack_list = []   # __ private
#
#     def push(self, value):
#         self.__stack_list.append(value)
#
#     def pop(self):
#         value = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return value
#
#     def __str__(self):
#         return f"{self.__stack_list}"
#
# obiect_stiva = Stack()
#
# obiect_stiva.push(3)
# print(obiect_stiva)
# obiect_stiva.push(2)
# print(obiect_stiva)
# obiect_stiva.push(1)
# print(obiect_stiva)
#
# print(obiect_stiva.pop())
# print(obiect_stiva)
# print(obiect_stiva.pop())
# print(obiect_stiva)
# print(obiect_stiva.pop())
# print(obiect_stiva)

# class ClasaExemplu:
#
#     def __init__(self, val = 1):
#         self.first = val
#         self.second = 0
#
#     def set_second(self, val = 2):
#         self.second = val
#
#     def __str__(self):
#         return f"{self.first} {self.second}"
#
# obiect_1 = ClasaExemplu()
# obiect_2 = ClasaExemplu(2)
# obiect_3 = ClasaExemplu(3)
#
# print(obiect_1)
# print(type(obiect_1).__name__)
# print(obiect_2)
# print(obiect_3.first)

# class Star:
#
#     def __init__(self, nume, galaxie):
#         self.name = nume
#         self.galaxy = galaxie
#
#     def __str__(self):
#         return f"{self.name} este in {self.galaxy}"
#
# soare = Star("Soarele", "Calea Lactee")
# print(soare)


# vehicul
# vehicul_de_teren
# vehicul_de_tractare

# class Vehicul:
#     pass
#
#
# class Vehicul_teren(Vehicul):
#     pass
#
#
# class Vehicul_tractare(Vehicul_teren):
#     pass

# parinti sunt Vehicul pt Vehicul_teren si Vehicul_tractare (indirect)
# parinti sunt Vehicul_teren pt Vehicul_tractare
# parintii sunt superclase pt copii (superClass)
# copiii sunt Vehicul_teren si Vehicul_tractare (indirect) pt Vehicul
# copiii sunt Vehicul_tractare  pt Vehicul_teren
# copiii se numesc subclase

# print("Vehicul   Vehicul_teren   Vehicul_tractare")
# for cls1 in [Vehicul, Vehicul_teren, Vehicul_tractare]:
#     for cls2 in  [Vehicul, Vehicul_teren, Vehicul_tractare]:
#         print(issubclass(cls1, cls2), end='\t')
#     print()

# vehicul1 = Vehicul()
# vehicul_teren = Vehicul_teren()
# vehicul_tractare = Vehicul_tractare()

# print(isinstance(vehicul1, Vehicul_teren))
#
# for obj in [vehicul1, vehicul_teren, vehicul_tractare]:
#     for cls in  [Vehicul, Vehicul_teren, Vehicul_tractare]:
#         print(isinstance(obj, cls), end='\t')
#     print()

# class Exemplu:
#
#     def __init__(self, val):
#         self.value = val
#
# obiect_1 = Exemplu(0)
# obiect_2 = Exemplu(2)
# obiect_3 = obiect_1
# obiect_3.value += 1
#
# print(obiect_1 is obiect_2)
# print(obiect_2 is obiect_3)
# print(obiect_3 is obiect_1)
# print(obiect_1.value, obiect_2.value, obiect_3.value)

# class SuperClass:
#     supVar = 1
#     variabilaClasa = 6
#
#     def __init__(self, nume):
#         self.name = nume
#         # self.var_1 = 101
#
#     def __str__(self):
#         return f"Numele meu este {self.name}"
#
# class Clasa3:
#     variabilaClasa = 5
#     def __init__(self, nume):
#         self.name = nume
#         self.var_2 = 201
#         self.var_1 = 101
#
# class SubClass(Clasa3, SuperClass):  # ordinea de verificare a superclaselor mostenite e de la stg la dr
#
#     subVar = 2
#     supVar = 3
#     def __init__(self, nume):
#         super().__init__(nume)
#         self.var_3 = 301
#         # SuperClass.__init__(self, nume)
#
# obiect = SubClass("Alexandra")
# # print(obiect.supVar)
# # print(obiect.variabilaClasa)
# print(obiect.var_3, obiect.var_2, obiect.var_1)

