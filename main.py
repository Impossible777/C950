from truck import truck
from createHashMap import createHashMap
import csv
import datetime


#Name: Michael Crist
#WGU StudentID: 000397493

# Path to the packageInfo.csv file
packageInfoPath = 'packageInfo.csv'
distanceTablePath = 'WGUPS Distance Table (1).csv'
distanceCSV = 'distanceCSV.csv'
addressCSV = 'addressCSV.csv'

# Creating the hash table
packageInfo = createHashMap()

#Initializing variable for total miles driven
milesDriven = 0.0




#Initializing list for distance data
distanceData = []

#Initializing list for address data
addressData = []

#initializing lists for truck package lists
packageList1 = ['1', '13', '14', '15', '16', '19', '20', '29', '30', '31', '34', '37', '40', '39']
Truck2PackageList = ['2', '3', '4', '5', '7', '8', '18', '10', '11', '12', '33', '35', '36', '38', '22']
Truck3PackageList = ['6', '17', '21', '23', '24', '26', '27', '28', '32']

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




# Returns the distance between two locations
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



# Returns the time it takes to deliver a package
def timeToDeliver(distance):
    timeInMinutes = distance / 0.3
    return timeInMinutes


#Calculates the nearest package delivery location and delivers the package. This process is repeated until all packages have been delivered on the truck entered as an object.
#Updates the package status and delivery time in the hash table
#Updates the truck's current location and time
def deliverPackages(truck):
    numberOfPackages = len(truck.packages)
    for package in truck.packages:
        packageInfo.update_array_index(package, 6, 'En Route')
        packageInfo.update_array_index(package, 8, truck.startTime.strftime("%H:%M"))
        packageInfo.update_array_index(package, 9, 'Truck ' + str(truck.number))
    
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
        
    truck.currentLocation = '4001 South 700 East'

# Returns the total miles driven by all trucks
def totalMilesDriven():
    totalMiles = truck1.milesDriven + truck2.milesDriven + truck3.milesDriven
    return totalMiles



    



      
#Creating the start time variable for truck1 and truck2 objects    
BeginngTime = datetime.datetime(2023, 12, 27, 8, 0, 0)

#Creating the start time variable for truck3 object
Truck3StartTime = datetime.datetime(2023, 12, 27, 9, 50, 0)

# Creating the truck objects
truck1 = truck(1, 16, 18, packageList1, BeginngTime)
truck2 = truck(2, 16, 18, Truck2PackageList, BeginngTime)
truck3 = truck(3, 16, 18, Truck3PackageList, Truck3StartTime)

# Delivering the packages
(deliverPackages(truck1))
(deliverPackages(truck2))
(deliverPackages(truck3))


if truck1.packages == []:
    truck1.addPackage('25')
    truck1.changeExactTime(datetime.datetime(2023, 12, 27, 10, 0, 0))
deliverPackages(truck1)

if truck3.packages == []:
    truck3.addPackage('9')
    truck3.changeExactTime(datetime.datetime(2023, 12, 27, 11, 15, 0))
deliverPackages(truck3)





class Main:
    # Verifies that the user has entered the time in the correct format
    def verifyTimeFormatting():
        while True:
            try:
                print('Please enter the time in the following format: HH:MM')
                input2 = input()
                formattedInputTime = datetime.datetime.strptime(input2, '%H:%M')
                break
            except ValueError:
                print('Please enter the time in the correct format.')
        return formattedInputTime
    
    #User interface
    print('Welcome to the WGUPS Package Delivery System')
    print('The total milage for this route is ' + str(totalMilesDriven()) + ' miles.')
    print('To make an inquiry about a package, or packages, please enter the word "time". Any other word will cancel the inquiry.')
    input1 = input()
    if input1 == 'time':
        formattedInputTime = verifyTimeFormatting()
        print('Please enter solo if you would like to inquire about a single package, or enter all if you would like to inquire about all packages at that time.')
        input3 = input()
        
        # If the user enters solo, the program will ask for the package number and then display the package information
        if input3 == 'solo':
            print('Please enter the package number.')
            input4 = input()
            formattedPackageTime = datetime.datetime.strptime(packageInfo.search(input4)[7], '%H:%M')
            formattedDepartureTime = datetime.datetime.strptime(packageInfo.search(input4)[8], '%H:%M')
            if formattedPackageTime < formattedInputTime:
                print('PackageID: ' + input4 + "," + ' Address: ' + packageInfo.search(input4)[0] + "," + ' City: ' + packageInfo.search(input4)[1] + "," + ' State: ' + packageInfo.search(input4)[2] + "," + ' Zip: ' + packageInfo.search(input4)[3] + "," + ' Deadline: ' + packageInfo.search(input4)[4] + "," + ' Weight: ' + packageInfo.search(input4)[5] + "," + ' Status: ' + packageInfo.search(input4)[6] + "," + ' Delivery Time: ' + packageInfo.search(input4)[7] + "," + " Delivered by: " + packageInfo.search(input4)[9])
            elif formattedDepartureTime > formattedInputTime:
                packageInfo.update_array_index(input4, 6, 'At Hub')
                print('PackageID: ' + input4 + "," + ' Address: ' + packageInfo.search(input4)[0] + "," + ' City: ' + packageInfo.search(input4)[1] + "," + ' State: ' + packageInfo.search(input4)[2] + "," + ' Zip: ' + packageInfo.search(input4)[3] + "," + ' Deadline: ' + packageInfo.search(input4)[4] + "," + ' Weight: ' + packageInfo.search(input4)[5] + "," + ' Status: ' + packageInfo.search(input4)[6] + " @ " + formattedInputTime.strftime("%H:%M"))
            elif formattedDepartureTime < formattedInputTime:
                packageInfo.update_array_index(input4, 6, 'En Route')
                print('PackageID: ' + input4 + "," + ' Address: ' + packageInfo.search(input4)[0] + "," + ' City: ' + packageInfo.search(input4)[1] + "," + ' State: ' + packageInfo.search(input4)[2] + "," + ' Zip: ' + packageInfo.search(input4)[3] + "," + ' Deadline: ' + packageInfo.search(input4)[4] + "," + ' Weight: ' + packageInfo.search(input4)[5] + "," + ' Status: ' + packageInfo.search(input4)[6] + " @ " + formattedInputTime.strftime("%H:%M") + " on " + packageInfo.search(input4)[9] )
        
        # If the user enters all, the program will display all packages and there statuses at the time entered
        elif input3 == 'all':
            for i in range(1, 41):
                package = packageInfo.search(str(i))
                formattedPackageTime = datetime.datetime.strptime(package[7], '%H:%M')
                formattedDepartureTime = datetime.datetime.strptime(package[8], '%H:%M')
                if formattedPackageTime < formattedInputTime:
                    print('PackageID: ' + str(i) + "," + ' Address: ' + package[0] + "," + ' City: ' + package[1] + "," + ' State: ' + package[2] + "," + ' Zip: ' + package[3] + "," + ' Deadline: ' + package[4] + "," + ' Weight: ' + package[5] + "," + ' Status: ' + package[6] + "," + ' Delivery Time: ' + package[7]+ "," + " Delivered by: " + package[9])
                elif formattedDepartureTime > formattedInputTime:
                    packageInfo.update_array_index(str(i), 6, 'At Hub')
                    print('PackageID: ' + str(i) + "," + ' Address: ' + package[0] + "," + ' City: ' + package[1] + "," + ' State: ' + package[2] + "," + ' Zip: ' + package[3] + "," + ' Deadline: ' + package[4] + "," + ' Weight: ' + package[5] + "," + ' Status: ' + package[6]+ " @ " + formattedInputTime.strftime("%H:%M"))
                elif formattedDepartureTime < formattedInputTime:
                    packageInfo.update_array_index(str(i), 6, 'En Route')
                    print('PackageID: ' + str(i) + "," + ' Address: ' + package[0] + "," + ' City: ' + package[1] + "," + ' State: ' + package[2] + "," + ' Zip: ' + package[3] + "," + ' Deadline: ' + package[4] + "," + ' Weight: ' + package[5]  + "," + ' Status: ' + package[6]+ " @ " + formattedInputTime.strftime("%H:%M") + " on " + package[9])
    else:
        'Thank you for using the WGUPS Package Delivery System. If you would like to make another inquiry, please restart the program and enter "time."'
                
            















    

    




            

    

