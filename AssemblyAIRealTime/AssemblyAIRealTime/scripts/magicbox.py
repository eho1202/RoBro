import random
import csv
from text_to_speech import convert_text_to_speech

def selmagicbox():
    with open('magicbox.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        endval = random.randint(0,19)
        for row in csv_reader:
            convert_text_to_speech(str(row[endval]))

#selmagicbox()
