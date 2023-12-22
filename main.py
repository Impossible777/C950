from truck import truck
from createHashMap import createHashMap
import csv

# Path to the packageInfo.csv file
packageInfoPath = 'packageInfo.csv'

# Creating the hash table
packageInfo = createHashMap()


#Accessing the packageInfo.csv file and inserting the data into the hash table
with open(packageInfoPath, 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        key = row[0]
        value = row[1:]

        packageInfo.insert(key, value)


# Creating the truck objects
truck1 = truck(16, 18)
truck2 = truck(16, 18)
truck3 = truck(16, 18)