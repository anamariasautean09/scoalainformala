import csv
import json
import pandas as pd
import os

input_file = {
  "id1": {
    "brand": "Dacia",
    "model": "Logan",
    "hp": "90",
    "price": "2000"
  },

  "id2": {
    "brand": "Audi",
    "model": "A4",
    "hp": "156",
    "price": "9000"
  },

  "id3": {
    "brand": "BMW",
    "model": "e320",
    "hp": "134",
    "price": "4999"
  },

    "id4": {
    "brand": "Opel",
    "model": "Corsa",
    "hp": "90",
    "price": "2900"
  },

    "id5": {
    "brand": "Volvo",
    "model": "xc40",
    "hp": "110",
    "price": "6000"
  },
    "id6": {
    "brand": "Audi",
    "model": "A3 e-tron",
    "hp": "114",
    "price": "9000"
  },
    "id7": {
    "brand": "Dacia",
    "model": "Stepway",
    "hp": "105",
    "price": "3500"
  },

    "id8": {
    "brand": "Opel",
    "model": "Astra-H",
    "hp": "77",
    "price": "3450"
  },

    "id9": {
    "brand": "Volkswagen",
    "model": "Polo",
    "hp": "75",
    "price": "2700"
  },

    "id10": {
    "brand": "Dacia",
    "model": "Spring",
    "hp": "125",
    "price": "10000"
  },

    "id11": {
    "brand": "Volkswagen",
    "model": "Arteon",
    "hp": "156",
    "price": "14000"
  },

    "id12": {
    "brand": "Dacia",
    "model": "Logan",
    "hp": "90",
    "price": "4000"
  },

    "id13": {
    "brand": "Volvo",
    "model": "v90",
    "hp": "100",
    "price": "5600"
  },

    "id14": {
    "brand": "Mercedes",
    "model": "Aclass",
    "hp": "116",
    "price": "8999"
  },

    "id15": {
    "brand": "Mercedes",
    "model": "Eclass",
    "hp": "144",
    "price": "16000"
  },

    "id16": {
    "brand": "Volkswagen",
    "model": "Golf",
    "hp": "108",
    "price": "4500"
  },

    "id17": {
    "brand": "Opel",
    "model": "Adam",
    "hp": "87",
    "price": "4800"
  },

    "id18": {
    "brand": "Audi",
    "model": "Q3",
    "hp": "156",
    "price": "11000"
  },

    "id19": {
    "brand": "Ford",
    "model": "KUGA",
    "hp": "170",
    "price": "14000"
  },

    "id20": {
    "brand": "Ford",
    "model": "Focus",
    "hp": "95",
    "price": "3999"
  }
}

fisier = pd.DataFrame(input_file)
fisier_date = fisier.to_csv('input_file.csv')
# print(fisier)

# directory = "output_data"
# parent_dir = "D:\ScoalaInformala\scoalainformala\catalog_masini"
# path = os.path.join(parent_dir, directory)
# os.mkdir(path)
# print("directory '%s' created" % directory)


# with open('masini.json') as f:
#   data = json.load(f)
# print(data)

# fisier1 = pd.read_json('masini.json')
# print(fisier1)

masini = pd.Series(input_file)
# print(masini)
# print(masini.loc['id15'])


# with open("input_file.csv", 'r') as file:
#   reader = csv.reader(file)
#   slow_cars = []
#   for line in reader:
#       for i, index in enumerate(line):
#         print(line[0])
#
#
#
# with open("output_data/slow_cars.json", 'w') as file:
#   json.dump(slow_cars, file, indent = 4)

slow_cars = []
for line in masini:
  if line.get('hp') == 156:
     json.dump(slow_cars)




