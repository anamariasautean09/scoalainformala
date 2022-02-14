# Codul numeric personal sau CNP este codul unic al fiecărei persoane născute în România, format din exact 13 cifre.
# De regulă el este atribuit la naștere fiecărui nou născut, 
# din acest motiv el poate fi regăsit pe certificatul de naștere.
# CNP figurează și pe buletinul de identitate sau cartea de
# identitate precum și pe permisul de conducere.
# A fost introdus ca element obligatoriu în actele de identitate, 
# de stare civilă și în alte acte personale printr-un decret prezidențial semnat de Nicolae Ceaușescu, la 2 martie 1978.

# Format: S AA LL ZZ JJ NNN C
# S - sexul si secolul in care s-a nascut persoana respectiva
# AA - ultimele 2 cifre din anul nasterii
# LL - ultimele 2 cifre din luna nasterii
# ZZ - ultimele 2 cifre din ziua nasterii
# JJ - codul judetului
# NNN - numar de 3 cifre din intervalul 001-999
# C - cifra de control care are formula :(S*2 + A*7 + A*9 + L*1 + L*4 + Z*6 + Z*3 + J*5 + J*8 + N*2 + N*7 + N*9) % 11

import datetime

# despart string-ul primit ca input in partile sale componente S,AA,LL,ZZ,JJ,NNN,C


def split_cnp(cnp: str) -> tuple[str, str, str, str, str, str, str]:   # realizarea unui tuplu de string-uri
    s = cnp[:1]
    aa = cnp[1:3]
    ll = cnp[3:5]
    zz = cnp[5:7]
    jj = cnp[7:9]
    nnn = cnp[9:12]
    c = cnp[12]
    return s, aa, ll, zz, jj, nnn, c

# verific data de nastere si aflul anul exact de nastere


def birth_date(s: str, aa: str, ll: str, zz: str) -> datetime.date.__class__:
    if "12".__contains__(s):   # daca S este 1 sau 2 atunci anul nasterii este cuprins intre 1900 si 1999
        aa = "19" + aa
    elif "34".__contains__(s):  # daca S este 3 sau 4 atunci anul nasterii este cuprins intre 1800 si 1899
        aa = "18" + aa
    elif "56".__contains__(s):  # daca S este 5 sau 6 atunci anul nasterii este cuprins intre 2000 si 2099
        aa = "20" + aa
    # daca S este 7,8 sau 9 atunci ori sunt persoane straine rezidente in Romania ori perosane straine
    elif "789".__contains__(s):  
        if aa.__eq__("00"):
            aa = "20" + aa    # pentru cazurille 7,8,9 se considera secolul 20 care e reprezentat de anii 1901-2000
        else:
            aa = "19" + aa

    try:
        date_of_birth = datetime.date(int(aa), int(ll), int(zz))    
        # verificare existenta data de nastere (in cazul lunii februarie)
        return date_of_birth
    except ValueError:
        return Exception("INVALID CNP - DATA INEXISTENTA")    
        # exceptie in cazul in care data nu exista (exemplu : 30 februarie, 29 februarie 2001)

# verificare cifra de control


def check_control_number(cnp: str, c: int):
    factors = "279146358279"
    s = 0
    for character, factor in zip(cnp[:-1], factors):  
        # am folosit functia zip care imi returneaza tupluri cu elemente din structurile initiale
        s += int(character) * int(factor)
    control = s % 11 if s % 11 < 10 else 1  
# am folosit un if-then-else intr-o singura line (one line) pentru stabilirea valorii ce va fi pus in cifra de control
    if not control == c:
        return False
    return True

# verificare data nastere (daca data nasterii e in viitor atunci cnp-ul este invalid)


def verify_date(s: str, aa: str, ll: str, zz: str, today: datetime.date.__class__):
    date_of_birth = birth_date(s, str(aa), str(ll), str(zz))
    if date_of_birth > today:
        return False
    return True
    
# verificare judet


def check_judet(jj: str):
    if int(jj) > 52 or int(jj) < 1 or int(jj) == 47 or int(jj) == 48 or int(jj) == 49 or int(jj) == 50:
        return False 
    return True


# verificare NNN
# PENTRU O VERIFICARE MAI AMANUNTITA ESTE NEVOIE DE:
# CNP-URILE INREGISTRATE IN ACEEASI ZI IN ACELASI SECTOR/JUDETdef check_nnn(nnn: int):

def check_nnn(nnn: int):
    if nnn < 1:
        return False
    return True     

# functia pentru validarea cnp-ului


def validate_cnp(cnp: str) -> str:
    if not len(cnp) == 13:         # verificare dimensiunea sirului ce reprezinta cnp-ul
        return Exception("INVALID CNP - LUNGIME CNP NECORESPUNZATOARE")   
        # exceptie pentru lungimea string-ului introdus care reprezinta cnp-ul

    s, aa, ll, zz, jj, nnn, c = split_cnp(cnp)   # atribuirea componentelor in fct de cnp-ul introdus

    if check_judet(jj) is False:    # apel fct pentru verificare judet
        return False
    if check_nnn(int(nnn)) is False:    # apel fct pentru verificare NNN
        return False
    if check_control_number(cnp, int(c)) is False:  # apel fct pentru verificare cifra de control
        return False
    if verify_date(s, aa, ll, zz, datetime.date.today()) is False:  # apel fct pentru verificare data
        return False

    return True


def functie_principala():
    try:
        cnp = input("Introduceti un CNP pentru a afla daca este valid sau nu: ")  
        # introducere de la tastatura a unui string care reprezinta cnp-ul
        validate_cnp(cnp)   # apelarea functiei de validare cnp
        if validate_cnp(cnp) is not True:
            return "CNP INVALID"
        return "CNP VALID"
    except Exception as e:  # exceptie generala
        return e


if __name__ == "__main__":
    print(functie_principala())
