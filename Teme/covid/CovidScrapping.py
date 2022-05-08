import csv
from collections import defaultdict
import pandas as pd

from numpy import average
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_url(day):
    return f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-ianuarie-ora-13-00/"


browser = webdriver.Chrome(ChromeDriverManager().install())

date = defaultdict(list)
lista_dates = []
for zi in range(20, 28):
    lista_dates.append(f'{zi}')
    url = get_url(zi)
    browser.get(url)
    table = browser.find_element(by=By.XPATH, value="//table[1]")
    rows = table.text.split("\n")
    header = rows[0]

    for i, row in enumerate(rows[1:], start=1):
        row = row.replace("Satu Mare", "Satu-Mare")
        row = row.replace("Mun. București", "București")

        if i <= 42:
            nr_crt, judet, cazuri, cazuri_noi, incidenta = row.split(" ")
            if cazuri_noi == '–':
                cazuri_noi = 0

            date[judet].append(
                (
                    int(cazuri.replace(".", "")),
                    int(cazuri_noi),
                    float(incidenta.replace(",", ".")),
                )
            )
df = pd.DataFrame(date)
df = df.T
df.to_csv('tabel.csv')
df = pd.read_csv('tabel.csv')
df = pd.DataFrame(df.values, columns=["Judet", "20.01.2022", "21.01.2022", "22.01.2022", "23.01.2022", "24.01.2022", "25.01.2022", "26.01.2022", "27.01.2022"])
df.replace(r'[)]|[(]|[\s]', '', regex=True, inplace=True)
df = df.set_index(["Judet"])
one = df['20.01.2022'].str.split(',', expand=True)
one.rename(columns={0: 'cazuri totale', 1: 'cazuri noi', 2: 'incidenta'}, inplace=True)
print(one)
one.to_csv('one.csv')
one.to_csv('one.xls')
print(df)
df.to_csv('table1.xls')
df.to_csv('table2.csv')
