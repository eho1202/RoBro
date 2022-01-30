import random
import csv

def selmagicbox():
    with open('magicbox.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        endval = random.randint(0,19)
        for row in csv_reader:
            print(row[endval])

#selmagicbox()