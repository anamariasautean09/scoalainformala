import pandas as pd
import os


def fileInput():
    lista_masini = {
      "car1": {"id": "random", "brand": "Audi", "model": "A1", "hp": "90", "price": "1900"},
      "car2": {"id": "random", "brand": "Dacia", "model": "Stepway", "hp": "110", "price": "1990"},
      "car3": {"id": "random", "brand": "Ford", "model": "Kuga", "hp": "60", "price": "1800"},
      "car4": {"id": "random", "brand": "Renault", "model": "Clio", "hp": "90", "price": "1990"},
      "car5": {"id": "random", "brand": "Volkswagen", "model": "Polo", "hp": "66", "price": "975"},
      "car6": {"id": "random", "brand": "Ford", "model": "Galaxy", "hp": "100", "price": "1500"},
      "car7": {"id": "random", "brand": "Renault", "model": "Megane", "hp": "120", "price": "900"},
      "car8": {"id": "random", "brand": "Volkswagen", "model": "Polo", "hp": "120", "price": "1500"},
      "car9": {"id": "random", "brand": "Audi", "model": "A3", "hp": "140", "price": "2500"},
      "car10": {"id": "random", "brand": "Opel", "model": "Corsa", "hp": "105", "price": "2000"},
      "car11": {"id": "random", "brand": "Audi", "model": "A8", "hp": "250", "price": "7000"},
      "car12": {"id": "random", "brand": "Dacia", "model": "Duster", "hp": "120", "price": "1500"},
      "car13": {"id": "random", "brand": "Mercedes", "model": "Aclass", "hp": "143", "price": "2500"},
      "car14": {"id": "random", "brand": "Opel", "model": "Astra", "hp": "900", "price": "7500"},
      "car15": {"id": "random", "brand": "Volkswagen",  "model": "T6", "hp": "130", "price": "3500"},
      "car16": {"id": "random", "brand": "Audi", "model": "A6", "hp": "200", "price": "3000"},
      "car17": {"id": "random", "brand": "Mercedes", "model": "Eclass", "hp": "200", "price": "3100"},
    }
    for data in lista_masini.values():
        data['id'] = data['brand'][0] + data['model'][0] + data['hp'][0] + data['price'][0]
    df = pd.DataFrame(lista_masini)
    df.to_csv('input.csv')


def make_folder():
    directory = 'output_data'
    parent_dir = r"D:\ScoalaInformala\scoalainformala\Teme\catalog_masini"
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
    except OSError:
        pass


def data_frame():
    fileInput()
    df = pd.read_csv('input.csv')
    df = df.T
    df = pd.DataFrame(df.values, columns=["id", "brand", "model", "hp", "price"])
    df = df.drop(df.index[0])
    df.hp = pd.to_numeric(df.hp)
    df.price = pd.to_numeric(df.price)
    print(df)

    make_folder()
    slow_cars = df[df.hp < 120]
    slow_cars.to_json(r'output_data\slow_cars.json')
    fast_cars = df[(df.hp >= 120) & (df.hp < 180)]
    fast_cars.to_json(r'output_data\fast_cars.json')
    sport_cars = df[df.hp >= 180]
    sport_cars.to_json(r'output_data\sport_cars.json')
    cheap_cars = df[df.price < 1000]
    cheap_cars.to_json(r'output_data\cheap_cars.json')
    medium_cars = df[(df.price >= 1000) & (df.hp < 5000)]
    medium_cars.to_json(r'output_data\medium_cars.json')
    expensive_cars = df[df.price >= 5000]
    expensive_cars.to_json(r'output_data\expensive_cars.json')


    mercedes = df.sort_values(by='brand')
    filt = mercedes['brand'].str.contains('Mercedes')
    mercedes = mercedes.loc[filt]
    mercedes.to_json(r'output_data\Mercedes.json')
    audi = df.sort_values(by='brand')
    filt = audi['brand'].str.contains('Audi')
    audi = audi.loc[filt]
    audi.to_json(r'output_data\Audi.json')
    dacia = df.sort_values(by='brand')
    filt = dacia['brand'].str.contains('Dacia')
    dacia = dacia.loc[filt]
    dacia.to_json(r'output_data\Dacia.json')
    ford = df.sort_values(by='brand')
    filt = ford['brand'].str.contains('Ford')
    ford = ford.loc[filt]
    ford.to_json(r'output_data\Ford.json')
    opel = df.sort_values(by='brand')
    filt = opel['brand'].str.contains('Opel')
    Opel = opel.loc[filt]
    Opel.to_json(r'output_data\Opel.json')
    renault = df.sort_values(by='brand')
    filt = renault['brand'].str.contains('Renault')
    renault = renault.loc[filt]
    renault.to_json(r'output_data\Renault.json')
    vw = df.sort_values(by='brand')
    filt = vw['brand'].str.contains('VW')
    vw = vw.loc[filt]
    vw.to_json(r'output_data\VW.json')


    df = df.sort_values(by='brand')

    iii = input('Introdu un filtru\n> ').capitalize()
    filt = df['brand'].str.startswith(iii)
    df = df.loc[filt]
    df.to_json(r'output_data\specific_brand.json')


if __name__ == '__main__':
    data_frame()




