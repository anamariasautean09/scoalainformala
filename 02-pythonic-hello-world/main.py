print("Numele meu este Anamaria")

print("\ntipuri de date")
print(1, type(-1)) # tipul int
print(1.1 , type(1.1)) #tipul float
print(1j , type(1j)) #tipul complex

print("\nconversii")
print(int(1.1)) #conversie la intreg
print(float(1)) #conversie la float
print(complex(1)) #conversie la complex

print("\noperatii")
print(1+1) #adunare
print(1-1) #diferenta
print(1*0) #inmultire
print(5/2) #impartire (catul)
print(5//2) #catul - impartire exacta
print(7%3) #modulo (restul impartirii)
print(2**3) #ridicare la putere

print("\noperatori de comparare cu rezultat boolean")
print(5==5) #op de egalitate
print(5==2)
print(5!=2) #op de diferentiere
print(5>2) #op de comparatie mai mare
print(5>-2) #op de comparatie mai mare sau egal
print(5<2) #op de comparatie mai mic
print(5<=2) #op de comparatie mai mic sau egal

print("\noperatori logici")
print(5>2 and 3>1) #SI logic (ambele conditii trebuie sa fie adev pt true)
print(5>2 or 3>1) #SAU logic (una dintre conditii trebuie sa fie adev pt true)
print(not(5>2 and 3>1)) # operator de negare

print("\noperatori de identitate")
print(7 is 7)
print(7 is not 7)

print("\nvariabile")

my_var, my_var_1 = 5, 1
my_var +=1
my_var *=2
print(my_var)
print(my_var_1)

var = my_var + 1
print(var)

print("\nstring-uri")
print("Ana are mere")
print('Ana are mere')
variabila = "Ana 'are' mere"
variabila1 = 'Ana "are" mere'
variabila2 = "Ana \"are\" mere"
variabila3 = """Ana
are 
mere
"""
print(variabila)
print(variabila1)
print(variabila2)
print(variabila3)

nume = "Sautean"
prenume = "Anamaria"
varsta = 21
inaltimea = 1.56
prezentare = "Numele meu este {} si prenumele este {}".format(nume, prenume)
prezentare1 = "Numele meu este {0} si prenumele este {1} si varsta {2}".format(nume, prenume, varsta)
prezentare2 = "Numele meu este " + nume + " si prenumele meu este " + prenume + " si varsta mea este " + str(varsta) + "."
print(prezentare)
print(prezentare1)
print(prezentare2)

prezentare3 = f"Numele meu este {nume} si prenumele meu este {prenume}"
print(prezentare3)


calcul = inaltimea + varsta
calcul1 = nume + prenume
print(calcul)
print(calcul1)