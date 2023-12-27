from truck import truck
from createHashMap import createHashMap
import csv
import datetime


# Path to the packageInfo.csv file
packageInfoPath = 'packageInfo.csv'
distanceTablePath = 'WGUPS Distance Table (1).csv'
distanceCSV = 'distanceCSV.csv'
addressCSV = 'addressCSV.csv'

# Creating the hash table
packageInfo = createHashMap()

milesDriven = 0.0



distanceData = []
addressData = []
packageList1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
Truck2PackageList = ['2', '3', '4', '5', '18', '6', '25', '28', '32', '33', '35', '36', '38', '22']

# Accessing the addressCSV.csv file and inserting the data into the addressData list
with open(addressCSV, 'r', encoding='utf-8-sig') as addressCSVFile:
    addressReader = csv.reader(addressCSVFile)
    for row in addressReader:
        addressData.append(row[2])

# Accessing the distanceCSV.csv file and inserting the data into the distanceData list
with open(distanceCSV, 'r', encoding='utf-8-sig') as distanceCSVFile:
    distanceReader = csv.reader(distanceCSVFile)
    for row in distanceReader:
        distanceData.append(row)


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
        return None
    return float(distance)


# Returns the distance from the truck's current location to the nearest package delivery location
def minDistanceFrom(truck):
    minDistance = 100000.00
    for package in truck.packages:
        distance = distanceBetweenLocations(packageInfo.search(package)[0], truck.currentLocation)
        if distance is not None and distance < minDistance:
            minDistance = distance
            deliverPackage = package
        else:
            distance = distanceBetweenLocations(truck.currentLocation, packageInfo.search(package)[0])
            if distance is not None and distance < minDistance:
                minDistance = distance
                deliverPackage = package
    return deliverPackage, minDistance


def deliverPackages(truck):
    milesDriven = 0.0
    numberOfPackages = len(truck.packages)
    count = 0
    
    while numberOfPackages > 0:
        deliverPackage, minDistance = minDistanceFrom(truck)
        print(deliverPackage)
        truck.removePackages(deliverPackage)
        milesDriven += minDistance
        truck.currentLocation = packageInfo.search(deliverPackage)[0]
        print(truck.currentLocation)
        packageInfo.update_array_index(deliverPackage, 6, 'Delivered')
        numberOfPackages -= 1
        count +=1
        print(count)
        print(milesDriven)
        
    
        
        
        

          
    

# Creating the truck objects
truck1 = truck(16, 18, packageList1)
truck2 = truck(16, 18, Truck2PackageList)
truck3 = truck(16, 18, packageList1)

deliverPackages(truck2)









    

    




            

    

