my_lambda = lambda x, y : x + y
#denumire functie = lambda param1, param2: corp functie
my_sum = my_lambda(2, 3)
print(my_sum)

players = [{
                "first name": "Ion",
                "last name": "Gheorghe",
                "varsta": 12
            },
            {
                "first name": "Andreea",
                "last name": "Popa",
                "varsta": 35
            },
            {
                "first name": "Iza",
                "last name": "Enache",
                "varsta": 25
            }

]

jucator_sortati = sorted(players, key=lambda jucator: jucator["varsta"])
print(jucator_sortati)