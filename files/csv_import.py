import csv

masini = [
      ['DACIA', 'LOGAN', 2005, 75],
      ['RENAULT', 'CLIO', 2005, 75]
]

with open('data.csv', 'a') as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=',')
      for masina in masini:
            csv_writer.writerow(masina)


