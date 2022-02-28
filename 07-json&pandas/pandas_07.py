import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renault'],
#     "culoare": ['rosu', 'alb', 'verde']
# }
#
# variabila = pd.DataFrame(dictionar_date)
# print(variabila)

# masini = ['Dacia', 'Volvo', 'Renault']
# var = pd.Series(masini, index = ['x', 'y', 'z'])
# print(var)
# print(var[0])
# print(var['z'])

# masini = {'x': 'dacia', 'y': 'volvo', 'z': 'renault'}
# var = pd.Series(masini,index = ['x', 'y'])
# print(var)

dictionar_date = {
    "masini": ['Dacia', 'Volvo', 'Renault'],
    "culoare": ['rosu', 'alb', 'verde']
}

var = pd.DataFrame(dictionar_date, index = ['producator1', 'producator2', 'producator3'])
# print(var.loc[[0, 1]])
# print(var.loc['producator1'])
# print(var.loc[['producator1', 'producator2']])
# print(var)

data1 = {
  "producator1": {
    "masini": "Dacia",
    "culoare": "rosu"
  },

  "producator2": {
    "masini": "Volvo",
    "culoare": "alb"
  },

  "producator3": {
    "masini": "Renault",
    "culoare": "verde"
  }
}
# var1 = pd.DataFrame("data.json")
# var1 = pd.read_json('data.json')
# url = 'https://api.exchangerate-api.com/v4/latest/USD'
# var1 = pd.read_json(url, )
# print(var1)

var1 = pd.DataFrame(data1)
fisier = var1.to_csv("data1.csv")
