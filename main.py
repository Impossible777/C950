from truck import truck
from createHashTable import createHashTable
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
packageInfo = createHashTable()

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
    
    #Utilizes the indexes of the addressData list to find the distance between two locations
    distance = distanceData[addressData.index(address1)][addressData.index(address2)]
    
    #If the distance is blank, the function returns None
    if distance == '':
        return None
    return float(distance)


# Returns the distance from the truck's current location to the nearest package delivery location
def minDistanceFrom(truck):
    
    #Set minDistance to a large number so that the first comparison always gets assigned to minDistance
    minDistance = 100000.00
    
    #Check each package on the truck
    for package in truck.packages:
        
        #Use the distanceBetweenLocations function to find the distance between the truck's current location and the package's delivery location
        distance = distanceBetweenLocations(packageInfo.look_up(package)[0], truck.currentLocation)
        
        #If the distance is less than minDistance, minDistance is assigned the value of distance
        if distance is not None and distance < minDistance:
            minDistance = distance
            deliverPackage = package
        else:
            #Due to the formatting of the distanceData list, it is necesssary to switch the order of the arguments
            #for the distanceBetweenLocations if the initial distance is None
            distance = distanceBetweenLocations(truck.currentLocation, packageInfo.look_up(package)[0])
            if distance is not None and distance < minDistance:
                minDistance = distance
                deliverPackage = package
    return deliverPackage, minDistance



# Returns the time it takes to deliver a package
def timeToDeliver(distance):
    timeInMinutes = distance / 0.3
    return timeInMinutes


#Calculates the nearest package delivery location and delivers the package. This process is repeated until all 
#packages have been delivered on the truck entered as an object.
def deliverPackages(truck):
    #Determines the number of packages on the truck
    numberOfPackages = len(truck.packages)
    
    #For every package on the truck 
    for package in truck.packages:
        #The status is updated
        packageInfo.update_array_index(package, 6, 'En Route')
        #The departure time is added
        packageInfo.update_array_index(package, 8, truck.startTime.strftime("%H:%M"))
        #The truck number is added
        packageInfo.update_array_index(package, 9, 'Truck ' + str(truck.number))
    
    #Continues to run the code until all packages have been delivered
    while numberOfPackages > 0:
        
        #Utilizes the minDistanceFrom function to find the nearest package delivery location and delivers it
        deliverPackage, minDistance = minDistanceFrom(truck)
        
        #The package is removed from the truck's package list once it is delivered
        truck.removePackages(deliverPackage)
        
        #Updates the trucks miles driven
        truck.drive(minDistance)
        
        #Updates the truck's current location
        truck.currentLocation = packageInfo.look_up(deliverPackage)[0]
        
        #Calculates the time it takes to deliver the package
        time = timeToDeliver(minDistance)
        
        #Updates the time of day
        truck.changeTime(time)
        
        #Updates the package status to delivered
        packageInfo.update_array_index(deliverPackage, 6, 'Delivered')
        
        #Reduces the number of packages on the truck by 1 so the while loop will eventually end
        numberOfPackages -= 1
        
        #Updates the package delivery time
        packageInfo.update_array_index(deliverPackage, 7, truck.startTime.strftime("%H:%M"))
        
    #When the truck has delivered all packages and the while loop has ended, the truck returns to the hub
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



#When truck1 has delivered it's initial packages, it returns to the hub and picks up the packages that were not ready at 8:00am
if truck1.packages == []:
    truck1.addPackage('25')
    truck1.changeExactTime(datetime.datetime(2023, 12, 27, 10, 0, 0))
deliverPackages(truck1)

#When truck3 has delivered it's initial packages, it returns to the hub and picks up the packages that were not ready at 8:00am
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
    print("Please select a number from the following options:")
    print("1: Print all package information and miles driven by all trucks")
    print("2: Print all information for a single package or all packages at a specific time")
    print("3: Exit the program")
    input1 = input()
    
    #If user enters 2,
    if input1 == '2':
        
        #The user will be asked to enter a time, and the time will be formatted appropriately by the verifyTimeFormatting function
        formattedInputTime = verifyTimeFormatting()
        
        #Once the time has been formatted, the user will be asked if they would like to inquire about a single package or all packages
        print('Please enter solo if you would like to inquire about a single package, or enter all if you would like to inquire about all packages at that time.')
        
        
        input3 = input()
        
        # If the user enters solo
        if input3 == 'solo':
            
            #They will be asked for a package number
            print('Please enter the package number.')
            input4 = input()
            
            #Formatted the package time and departure time so that they can be compared to the input time
            formattedPackageTime = datetime.datetime.strptime(packageInfo.look_up(input4)[7], '%H:%M')
            #Formatted the departure time so that it can be compared to the input time
            formattedDepartureTime = datetime.datetime.strptime(packageInfo.look_up(input4)[8], '%H:%M')
            
            #If the package time is less than the input time, the package has been delivered and the program will display the package information
            if formattedPackageTime < formattedInputTime:
                print('PackageID: ' + input4 + "," + ' Address: ' + packageInfo.look_up(input4)[0] + "," + ' City: ' + packageInfo.look_up(input4)[1] + "," + ' State: ' + packageInfo.look_up(input4)[2] + "," + ' Zip: ' + packageInfo.look_up(input4)[3] + "," + ' Deadline: ' + packageInfo.look_up(input4)[4] + "," + ' Weight: ' + packageInfo.look_up(input4)[5] + "," + ' Status: ' + packageInfo.look_up(input4)[6] + "," + ' Delivery Time: ' + packageInfo.look_up(input4)[7] + "," + " Delivered by: " + packageInfo.look_up(input4)[9])
            
            #If the departure time is greater than the input time, the package is at the hub and the program will display the package information
            elif formattedDepartureTime > formattedInputTime:
                packageInfo.update_array_index(input4, 6, 'At Hub')
                print('PackageID: ' + input4 + "," + ' Address: ' + packageInfo.look_up(input4)[0] + "," + ' City: ' + packageInfo.look_up(input4)[1] + "," + ' State: ' + packageInfo.look_up(input4)[2] + "," + ' Zip: ' + packageInfo.look_up(input4)[3] + "," + ' Deadline: ' + packageInfo.look_up(input4)[4] + "," + ' Weight: ' + packageInfo.look_up(input4)[5] + "," + ' Status: ' + packageInfo.look_up(input4)[6] + " @ " + formattedInputTime.strftime("%H:%M"))
            
            #If the departure time is less than the input time, the package is en route and the program will display the package information
            elif formattedDepartureTime < formattedInputTime:
                packageInfo.update_array_index(input4, 6, 'En Route')
                print('PackageID: ' + input4 + "," + ' Address: ' + packageInfo.look_up(input4)[0] + "," + ' City: ' + packageInfo.look_up(input4)[1] + "," + ' State: ' + packageInfo.look_up(input4)[2] + "," + ' Zip: ' + packageInfo.look_up(input4)[3] + "," + ' Deadline: ' + packageInfo.look_up(input4)[4] + "," + ' Weight: ' + packageInfo.look_up(input4)[5] + "," + ' Status: ' + packageInfo.look_up(input4)[6] + " @ " + formattedInputTime.strftime("%H:%M") + " on " + packageInfo.look_up(input4)[9] )
        
        # If the user enters all, the program will display all packages that are at the hub, en route, or delivered at the input time
        elif input3 == 'all':
            
            #Used to print the package information for all packages
            for i in range(1, 41):
                
                #Saving the package ID to a variable
                package = packageInfo.look_up(str(i))
                
                #Formatting the package time and departure time so that they can be compared to the input time
                formattedPackageTime = datetime.datetime.strptime(package[7], '%H:%M')
                
                #Formatting the departure time so that it can be compared to the input time
                formattedDepartureTime = datetime.datetime.strptime(package[8], '%H:%M')
                
                #If the package time is less than the input time, the package has been delivered and the program will display the package information
                if formattedPackageTime < formattedInputTime:
                    print('PackageID: ' + str(i) + "," + ' Address: ' + package[0] + "," + ' City: ' + package[1] + "," + ' State: ' + package[2] + "," + ' Zip: ' + package[3] + "," + ' Deadline: ' + package[4] + "," + ' Weight: ' + package[5] + "," + ' Status: ' + package[6] + "," + ' Delivery Time: ' + package[7]+ "," + " Delivered by: " + package[9])
                
                #If the departure time is greater than the input time, the package is at the hub and the program will display the package information
                elif formattedDepartureTime > formattedInputTime:
                    packageInfo.update_array_index(str(i), 6, 'At Hub')
                    print('PackageID: ' + str(i) + "," + ' Address: ' + package[0] + "," + ' City: ' + package[1] + "," + ' State: ' + package[2] + "," + ' Zip: ' + package[3] + "," + ' Deadline: ' + package[4] + "," + ' Weight: ' + package[5] + "," + ' Status: ' + package[6]+ " @ " + formattedInputTime.strftime("%H:%M"))
                
                #If the departure time is less than the input time, the package is en route and the program will display the package information
                elif formattedDepartureTime < formattedInputTime:
                    packageInfo.update_array_index(str(i), 6, 'En Route')
                    print('PackageID: ' + str(i) + "," + ' Address: ' + package[0] + "," + ' City: ' + package[1] + "," + ' State: ' + package[2] + "," + ' Zip: ' + package[3] + "," + ' Deadline: ' + package[4] + "," + ' Weight: ' + package[5]  + "," + ' Status: ' + package[6]+ " @ " + formattedInputTime.strftime("%H:%M") + " on " + package[9])
    
    #If the user enters 1, the program will display the total miles driven by all trucks and all package information
    elif input1 == '1':
        print('The total milage for this route is ' + str(totalMilesDriven()) + ' miles.')
        for i in range(1, 41):
            package = packageInfo.look_up(str(i))
            print('PackageID: ' + str(i) + "," + ' Address: ' + package[0] + "," + ' City: ' + package[1] + "," + ' State: ' + package[2] + "," + ' Zip: ' + package[3] + "," + ' Deadline: ' + package[4] + "," + ' Weight: ' + package[5] + "," + ' Status: ' + package[6] + "," + ' Delivery Time: ' + package[7]+ "," + " Delivered by: " + package[9])
    
    #If the user enters 3, the program will end
    else:
        print('Thank you for using the WGUPS Package Delivery System. If you would like to make another inquiry, please restart the program and choose a correct option.')
                
            















    

    




            

    

