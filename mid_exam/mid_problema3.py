# Scrie un program care sa afiseze toate combinarile de 2 litere
# dintre valorile dictionarului de mai jos:
#
dictionar = {"1": "abc",
             "2": "s",
             "3": "o",
             "4": "n",
             "5": "lm",
             "6": "jk",
             "7": "gi",
             "8": "def",
             "9": "abc"}

# elimin duplicatele

def duplicates(dictionar):
    a = list(dict.values(dictionar))
    return list(dict.fromkeys(a))

# sepoar valorile din dict in litere
def combination_2letters(dictionar):
    lista = duplicates(dictionar)
    for element in lista:
        for letter in element:
            a = list(letter)
            print(a)


print(combination_2letters(dictionar))
