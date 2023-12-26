from truck import truck
from createHashMap import createHashMap
import csv

# Path to the packageInfo.csv file
packageInfoPath = 'packageInfo.csv'
distanceTablePath = 'WGUPS Distance Table (1).csv'
distanceCSV = 'distanceCSV.csv'
addressCSV = 'addressCSV.csv'

# Creating the hash table
packageInfo = createHashMap()



distanceData = []
addressData = []
packageList1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
Truck2PackageList = ['2', '3', '4', '5', '18', '36', '38', '6', '25', '28', '32', '33', '35', '36', '38', '39']

with open(addressCSV, 'r', encoding='utf-8-sig') as addressCSVFile:
    addressReader = csv.reader(addressCSVFile)
    for row in addressReader:
        addressData.append(row[2])


with open(distanceCSV, 'r', encoding='utf-8-sig') as distanceCSVFile:
    distanceReader = csv.reader(distanceCSVFile)
    for row in distanceReader:
        distanceData.append(row[0:])


#Accessing the packageInfo.csv file and inserting the data into the hash table
with open(packageInfoPath, 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        key = row[0]
        value = row[1:]

        packageInfo.insert(key, value)

def distanceBetweenLocations(address1, address2):
    distance = distanceData[addressData.index(address1)][addressData.index(address2)]
    if distance == '':
        return 0.0
    print(address1, address2, distance)
    return float(distance)


def minDistanceFrom(truck):
    minDistance = 100000.00
    for package in truck.packages:
        package_info = packageInfo.search(package)
        if package_info is not None:
            distance = distanceBetweenLocations(packageInfo.search(package)[0], truck.currentLocation)
            if distance < minDistance:
                minDistance = distance
    return minDistance        
    

# Creating the truck objects
truck1 = truck(16, 18, packageList1)
truck2 = truck(16, 18, Truck2PackageList)
truck3 = truck(16, 18, packageList1)

addressOne = '4001 South 700 East'
addressTwo = '1060 Dalton Ave S'


print(minDistanceFrom(truck2))








    

    




            

    

