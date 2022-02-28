from random import choice


#name of the player
nume_jucator = input('Cum te cheama?\n')

#greet and show options
print("Optiunile tale sunt: \n piatra\n foarfeca\n hartie\n")

while True:

    alegere_jucator = input('Alege o optiune: ')

    alegeri_totale = ["piatra", "foarfeca", "hartie"]

    alegere_calculator = choice(alegeri_totale)

    print(f"Tu ai ales {alegere_jucator},iar calculatorul a ales {alegere_calculator}")
    print('\n')
    if alegere_calculator == alegere_jucator:
        print("Ati ales la fel.Try again")
        print('\n')
    elif alegere_jucator == "piatra" and alegere_calculator == "foarfece":
        print("Piatra bate foarfeca. Ai castigat!")
        print('\n')
    elif alegere_jucator == "piatra" and alegere_calculator == "hartie":
        print("Hartia bate foarfeca. Ai pierdut!")
        print('\n')
    elif alegere_jucator == "foarfeca" and alegere_calculator == "hartie":
        print("Foarfeca bate hartia. Ai castigat!")
        print('\n')
    elif alegere_jucator == "foarfeca" and alegere_calculator == "piatra":
        print("Piatra bate foarfeca. Ai pierdut!")
        print('\n')
    elif alegere_jucator == "hartie" and alegere_calculator == "foarfeca":
        print("Foarfeca bate hartia. Ai pierdut!")
        print('\n')
    elif alegere_jucator == "hartie" and alegere_calculator == "piatra":
        print("Hartia bate piatra. Ai castigat!")
        print('\n')

    restart_joc = input("Vrei sa reincepi jocul?\n")
    if restart_joc != 'da':
        break
