#daca conditie:
#   print("adevarat")
#daca alta_conditie:
#   print("nici aceasta nu e adev")
#altfel:
#   print("afisez doar daca "conditie" si "alta conditie" nu sunt adev")

my_var = 7
if my_var <6 :
    print('set instructiuni @1')
elif my_var <10:
    print("set instructiuni #2")
else:
    print("set instructiuni #3")
print('a iesit\n')

var = 7
mesaj = "set instructiuni #3"
if var < 6:
    mesaj = "set instructiuni #1"
elif var < 10:
    mesaj = "set instructiuni #2"
print(mesaj)
print("a iesit")


#structuri repetitive
#while si for

var1 = 1
while var1 < 10:
    #var1 +=1
    print("bloc de instr", var1)
    var1 += 1
    #break

string = "Ana are mere"
lista2 = [1,2,3, 'a']
for i, v in enumerate(lista2):
    print(i, "=>", v)

for var_temporara  in range(0, len(lista2)):
    print(var_temporara)

print(var_temporara, ">>")

dictionar1 = {1: 'unu', 2:'doi', 3:'trei'}
for item, value in dictionar1.items():
    print(item, value)
    print(item, dictionar1.get(item))