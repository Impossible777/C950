from createHashMap import createHashMap
import csv

packageInfoPath = 'packageInfo.csv'

with open(packageInfoPath, 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)