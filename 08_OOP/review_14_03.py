class ClasaMea:
    gamma = 0  # atribut / variabila de clasa

    def __init__(self):  # constructor
        self.alfa = 1  # variabila de instanta
        self.__delta = 3  # variabila de instanta privata


obj = ClasaMea()  # instantiere a clasei  ClasaMea - declarare de obiect
obj.beta = 2  # variabila de instanta si poate exista doar in interiorul obj-ului
print(obj.__dict__)
print(obj.alfa)
print(obj.gamma)
print(ClasaMea.gamma)
# print(obj._ClasaMea__delta)
