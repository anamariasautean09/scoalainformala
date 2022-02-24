import csv
import datetime
import os

# crearea fisierului care contine categoriile de task-uri

categorii = [["curs"], ["cumparaturi"], ["munca"], ["cadouri"]]

with open("categorii.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    for categorie in categorii:
        csv_writer.writerow(categorie)
csv_file.close()


def validate_date(data_introdusa):
    try:
        datetime.datetime.strptime(data_introdusa, "%d.%m.%Y")
    except ValueError as e:
        print("ERROR DATE\n", e)
        return False
    return True


def validate_hour(ora_introdusa):
    try:
        datetime.datetime.strptime(ora_introdusa, "%H:%M")
    except ValueError as e:
        print("ERROR TIME\n", e)
        return False
    return True


def validate_task(task):
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        for line in file.readlines():
            if task in line:
                print("Task already in file")
                return False
        return True


# cerinte


def cerinte():
    raspuns_utilizator = input("Doresti sa introduci un task? (yes/no) ")
    while raspuns_utilizator != "no":
        with open("taskuri_deadline_responsabil_categorie.txt", "a") as file:
            task = input("Introduceti un task: ")
            if validate_task(task) == False:
                break

            deadline = input("Introduceti o data limita pentru rezolvarea task-ului: ")
            if validate_date(deadline) == False:
                break
            hour_deadline = input(
                "Introduceti o ora limita pentru rezolvarea task-ului: "
            )
            if validate_hour(hour_deadline) == False:
                break

            responsabil = input(
                "Introduceti numele persoanei responsabile pentru task-ul introdus anterior: "
            )

            cateogrie_task = input(
                "Introduceti categoria din care face parte task-ul introdus: "
            )
            c = [cateogrie_task]
            if c not in categorii:
                print("Cateogria introdusa nu exista!")

            file.write(task)
            file.write(", ")
            file.write(deadline)
            file.write(" ")
            file.write(hour_deadline)
            file.write(", ")
            file.write(responsabil)
            file.write(", ")
            file.write(cateogrie_task)

            raspuns_utilizator = input("Doresti sa introduci un task? (yes/no) ")

            if raspuns_utilizator == "yes":
                file.write("\n")


# cerinte suplimentare

# 1. Listare date: în afișarea inițială a datelor se realizează o sortare în funcție de categorie.
def listare_date():
    print("----------Listarea datelor----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()

        for line in sorted(informatii, key=lambda line: line.split(",")[3]):
            print(line)


# 2. Sortare: se alege o opțiune din cele 8 de mai jos:
def sortare_asc_task():
    print("----------Sortare ascendenta task----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()

        for line in sorted(informatii, key=lambda line: line.split(",")[0]):
            print(line)


def sortare_desc_task():
    print("----------Sortare descendenta task----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()

        for line in sorted(
            informatii, key=lambda line: line.split(",")[0], reverse=True
        ):
            print(line)


def sortare_asc_data():
    print("----------Sortare ascendenta data----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()
        for line in informatii:
            date = line.split()[1].split(".")
            hour = line.split()[2].split(":")
            date = datetime.datetime(
                int(date[2]),
                int(date[1]),
                int(date[0]),
                int(hour[0]),
                int(hour[1][:-1]),
            )
            indexing = informatii.index(line)
            informatii[indexing] = line.split(",")
            informatii[indexing][1] = date

        for line in sorted(informatii, key=lambda line: line[1]):
            line[1] = line[1].__str__()  # conversie din datetime in str

            print(",".join(line))


def sortare_desc_data():
    print("----------Sortare descendenta data----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()
        for line in informatii:
            date = line.split()[1].split(".")
            hour = line.split()[2].split(":")
            date = datetime.datetime(
                int(date[2]),
                int(date[1]),
                int(date[0]),
                int(hour[0]),
                int(hour[1][:-1]),
            )
            indexing = informatii.index(line)
            informatii[indexing] = line.split(",")
            informatii[indexing][1] = date

        for line in sorted(informatii, key=lambda line: line[1], reverse=True):
            line[1] = line[1].__str__()  # conversie din datetime in str

            print(",".join(line))


def sortare_asc_responsabil():
    print("----------Sortare ascendenta responsabil----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()

        for line in sorted(informatii, key=lambda line: line.split(",")[2]):
            print(line)


def sortare_desc_responsabil():
    print("----------Sortare descendenta responsabil----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()

        for line in sorted(
            informatii, key=lambda line: line.split(",")[2], reverse=True
        ):
            print(line)


def sortare_asc_cateogrie():
    print("----------Sortare ascendenta categorie----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()

        for line in sorted(informatii, key=lambda line: line.split(",")[3]):
            print(line)


def sortare_desc_cateogrie():
    print("----------Sortare descendenta categorie----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()

        for line in sorted(
            informatii, key=lambda line: line.split(",")[3], reverse=True
        ):
            print(line)


# 3.Filtrare date:
# filtrarea datelor reprezintă de fapt o listare a datelor în funcție de anumite detalii date de la tastatură.
# criteriile de filtrare sunt: task, data, responsabil, categorie
# se cere de la tastatura campul dupa care se va face filtarea


def filter_task():
    print("-----------Filtrare in functie de task-----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()
        str_filter = input(
            "Introduceti un string dupa care se va realiza filtrarea datelor: "
        )
        print(f"Task-urile care incep/contin cu {str_filter} sunt: \n")
        for line in informatii:
            result = line.split(",")[0]
            if result.__contains__(str_filter):
                print(line)


def filter_data():
    print("-----------Filtrare in functie de data-----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()
        str_filter = input(
            "Introduceti un string dupa care se va realiza filtrarea datelor: "
        )
        print(f"Datele limita care incep/contin {str_filter} sunt: \n")
        for line in informatii:
            result = line.split(",")[1]
            if result.__contains__(str_filter):
                print(line)


def filter_responsabil():
    print("-----------Filtrare in functie de persoana responsabila-----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()
        str_filter = input(
            "Introduceti un string dupa care se va realiza filtrarea datelor: "
        )
        print(f"Responsabilii ale caror nume incep/contin {str_filter} sunt: \n")
        for line in informatii:
            result = line.split(",")[2]
            if result.__contains__(str_filter):
                print(line)


def filter_categorie():
    print("-----------Filtrare in functie de cateogrie-----------\n")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()
        str_filter = input(
            "Introduceti un string dupa care se va realiza filtrarea datelor: "
        )
        print(f"Categoriile care incep/contin {str_filter} sunt: \n")
        for line in informatii:
            result = line.split(",")[3]
            if result.__contains__(str_filter):
                print(line)


# alegere tip filtrare


def choose_filter_type():
    tip_filtrare = input(
        "Introduceti categoria dupa care doriti sa se filtreze datele: "
    )
    if tip_filtrare == "task":
        filter_task()
    if tip_filtrare == "data":
        filter_data()
    if tip_filtrare == "responsabil":
        filter_responsabil()
    if tip_filtrare == "categorie":
        filter_categorie()


def add_new_task():
    new_task = input(
        "Introduceti numele noului task-ului pe care doriti sa il editati: "
    )
    with open("taskuri_deadline_responsabil_categorie.txt", "a") as file:

        task = input("Introduceti un task: ")
        if validate_task(task) == False:
            return

        deadline = input("Introduceti o data limita pentru rezolvarea task-ului: ")
        if validate_date(deadline) == False:
            return

        hour_deadline = input("Introduceti o ora limita pentru rezolvarea task-ului: ")
        if validate_hour(hour_deadline) == False:
            return

        responsabil = input(
            "Introduceti numele persoanei responsabile pentru task-ul introdus anterior: "
        )

        cateogrie_task = input(
            "Introduceti categoria din care face parte task-ul introdus: "
        )
        c = [cateogrie_task]
        if c not in categorii:
            print("Cateogria introdusa nu exista!")
        task = (
            task
            + ", "
            + deadline
            + " "
            + hour_deadline
            + ", "
            + responsabil
            + ", "
            + cateogrie_task
            + "\n"
        )
        file.write(task)


def edit_task():
    editing_task = input("Introduceti numele task-ului pe care doriti sa il editati: ")
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        informatii = file.readlines()
        for line in informatii:
            if line.split(",")[0] == editing_task:
                task = input("Introduceti un task: ")
                if validate_task(task) == False:
                    break

                deadline = input(
                    "Introduceti o data limita pentru rezolvarea task-ului: "
                )
                if validate_date(deadline) == False:
                    break
                hour_deadline = input(
                    "Introduceti o ora limita pentru rezolvarea task-ului: "
                )
                if validate_hour(hour_deadline) == False:
                    break

                responsabil = input(
                    "Introduceti numele persoanei responsabile pentru task-ul introdus anterior: "
                )
                # if validate_responsabil(responsabil) == False:
                #     break

                cateogrie_task = input(
                    "Introduceti categoria din care face parte task-ul introdus: "
                )
                c = [cateogrie_task]
                if c not in categorii:
                    print("Cateogria introdusa nu exista!")
                task = (
                    task
                    + ", "
                    + deadline
                    + " "
                    + hour_deadline
                    + ", "
                    + responsabil
                    + ", "
                    + cateogrie_task
                    + "\n"
                )
                index = informatii.index(line)
                informatii[index] = task

        with open("taskuri_deadline_responsabil_categorie.txt", "w") as file:
            file.writelines(informatii)


def remove_task():
    removable_task = input(
        "Introduceti numele task-ului pe care doriti sa il stergeti: "
    )
    with open("taskuri_deadline_responsabil_categorie.txt", "r") as file:
        with open("new_file.txt", "w") as out_file:
            for line in file:
                if not line.strip("\n").startswith(removable_task):
                    out_file.write(line)

    os.replace("new_file.txt", "taskuri_deadline_responsabil_categorie.txt")


def meniu_operatii():
    print("----------Meniu de operatii----------")
    print("1.Listare date\n")
    print("2.sortare ascendentă task\n")
    print("3. sortare descendentă task\n")
    print("4.sortare ascendentă data\n")
    print("5.sortare descendentă data\n")
    print("6.sortare ascendentă persoana responsabila\n")
    print("7.sortare descendentă persoana responsabila\n")
    print("8.sortare ascendentă categorie\n")
    print("9.sortare descendentă categorie\n")
    print("10.Filtrare date\n")
    print("11.Adaugare nou task\n")
    print("12.Editare task\n")
    print("13.Stergere task\n")
    print("14.Introducere mai multe task-uri\n")
    print("0.Exit\n")

    comenzi = {
        "0": exit,
        "1": listare_date,
        "2": sortare_asc_task,
        "3": sortare_desc_task,
        "4": sortare_asc_data,
        "5": sortare_desc_data,
        "6": sortare_asc_responsabil,
        "7": sortare_desc_responsabil,
        "8": sortare_asc_cateogrie,
        "9": sortare_desc_cateogrie,
        "10": choose_filter_type,
        "11": add_new_task,
        "12": edit_task,
        "13": remove_task,
        "14": cerinte,
    }

    operatie = "15"

    while operatie != "0":
        operatie = input("Introduceti numarul operatiei pe care doriti sa o realizati:")
        comenzi[operatie]()


meniu_operatii()
