import random
import csv

def selQuote():
    with open('quotes.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        endval = random.randint(0,2)
        for row in csv_reader:
            print(row[endval])

#selQuote()