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

class ClasaExemplu:

    def __init__(self, val = 1):
        self.first = val
        self.second = 0

    def set_second(self, val = 2):
        self.second = val

    def __str__(self):
        return f"{self.first} {self.second}"

obiect_1 = ClasaExemplu()
obiect_2 = ClasaExemplu(2)
obiect_3 = ClasaExemplu(3)

print(obiect_1)
print(type(obiect_1).__name__)
print(obiect_2)
print(obiect_3.first)


