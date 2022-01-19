lista = [1, 2, 3, "string", 2.3]
print(type(lista))
print(lista[3])
print(lista[2:4])
print(lista[2::4])
print(lista[2:])
print(lista[0:4:2])  # elementele din 2 in 2

# denumire_lista[inde-inceput : index_final-1 : pas]

print(lista[-1]) #ultimul element din lista
print(lista[-1:-3:-1]) #pas negativ
print(lista[-1::-1]) #pas negativ
print(lista[5:])

lista.append("super")
lista[3] = "mere"
print(lista)
print(len(lista)) #lungime lista

print(lista.index(2))
print(lista.index(3))

print(lista.insert(3, "element nou")) #insereaza un elem nou pe indexul 3
print(lista)

lista.remove(3) #stergere din lista cu valoarea din lista
print(lista)

lista.pop()
print(lista)

lista.pop(2)  #stergere din lista cu referire la index
print(lista)

lista.reverse() #inverseaza lista
print(lista)

lista.pop(1)  #stergere din lista cu referire la index
print(lista)

lista.sort()
print(lista)

lista2 = ["2", "-5", "21"]
lista2.sort()
print(lista2)