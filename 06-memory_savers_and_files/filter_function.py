lista_nr = [1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]

def functie_nr_pare(number):
    if number % 2 == 0:
       return True
    return False

iterator_nr_pare = filter(functie_nr_pare, lista_nr)
print(list(iterator_nr_pare))

litere = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def filter_vocale(letter):
    vocale = ['a', 'e', 'i', 'o', 'u']
    return  True if letter in vocale else False

print(filter_vocale(litere))