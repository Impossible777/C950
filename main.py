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
packageList1 = ['1', '13', '14', '15', '16', '19', '20', '29', '30', '31', '34', '37', '40', '39']
Truck2PackageList = ['2', '3', '4', '5', '7', '8', '18', '10', '11', '12', '33', '35', '36', '38', '22']
Truck3PackageList = ['6', '17', '21', '23', '24', '25', '26', '27', '28', '32']

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



def timeToDeliver(distance):
    timeInMinutes = distance / 0.3
    return timeInMinutes


def deliverPackages(truck):
    numberOfPackages = len(truck.packages)
    for package in truck.packages:
        packageInfo.update_array_index(package, 6, 'En Route')
    
    while numberOfPackages > 0:
        deliverPackage, minDistance = minDistanceFrom(truck)
        truck.removePackages(deliverPackage)
        truck.drive(minDistance)
        truck.currentLocation = packageInfo.search(deliverPackage)[0]
        time = timeToDeliver(minDistance)
        truck.changeTime(time)
        packageInfo.update_array_index(deliverPackage, 6, 'Delivered')
        numberOfPackages -= 1
        packageInfo.update_array_index(deliverPackage, 7, truck.startTime.strftime("%H:%M"))
        
    truck.currentLocation = '6351 South 900 East'



    



      
    
BeginngTime = datetime.datetime(2023, 12, 27, 8, 0, 0)
Truck3StartTime = datetime.datetime(2023, 12, 27, 9, 50, 0)
# Creating the truck objects
truck1 = truck(16, 18, packageList1, BeginngTime)
truck2 = truck(16, 18, Truck2PackageList, BeginngTime)
truck3 = truck(16, 18, Truck3PackageList, Truck3StartTime)

# Delivering the packages
(deliverPackages(truck1))
(deliverPackages(truck2))
(deliverPackages(truck3))

if truck3.packages == []:
    truck3.addPackage('9')
    truck3.changeExactTime(datetime.datetime(2023, 12, 27, 11, 15, 0))
deliverPackages(truck3)














    

    




            

    

