#tupluri
lista = [1,2,3,1, 'a']
lista_1 = ['a', 'b', 'c']
l = lista + lista_1
print(l)

tuplu = (1,2,3,1 ,'a')
tuplu1 = (1,2,3,'b')
t = tuplu + tuplu1
print(t)

tuplu_nou = ('1',)  #tuplu de un singur element !!!!
print((type(tuplu_nou)))

#dictionare

dictionar = {"cheie1": '1',
             1: '1',
             'lista': [1,2,3]}

print(dictionar['cheie1'])
print(dictionar.get("cheie2"))
dictionar['cheie1'] = 2
dictionar.update({"cheie1":2})
print(dictionar)

dictionar['cheie2'] = 3
print(dictionar)

dictionar.update({"cheie3" : 4})
print(dictionar)

dictionar.keys()    #returneaza cheile
dictionar.values()  #returneaza valorile
print(dictionar.items())   #returneaza ca tuplu


#seturi

setul_meu ={}
setul_meu = {1,1,3}
print(setul_meu)  #afiseaza o singura data elementele duplicate
print(l)
print(set(l))  #cast lista la set



