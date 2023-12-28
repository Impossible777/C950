import datetime

class truck:
    
    #Creating the constructor for the truck class
    def __init__(self, number, maxPackages, avgSpeed, packages, startTime, currentLocation = '4001 South 700 East', milesDriven = 0.0):
        self.maxPackages = maxPackages
        self.avgSpeed = avgSpeed
        self.packages = packages
        self.currentLocation = currentLocation
        self.milesDriven = milesDriven
        self.startTime = startTime
        self.number = number
    
    
    #Creating the print function for the truck class
    def __str__(self):
        return f"This truck is currently at {self.currentLocation} and has {self.packages} on board."
    
    #A method that adds a package to the truck
    def addPackage(self, package):
        
        #If the truck has 16 packages, it will not be allowed to add more
        if len(self.packages) >= self.maxPackages:
            print("This truck is full.")
        else:
            self.packages.append(package)
    
    
    #A method that removes a package from the truck
    def removePackages(self, package):
        self.packages.remove(package)
    
    #A method that updates the location of the truck
    def currentLocation(self, location):
        self.currentLocation = location
    
    #A method that updates the miles driven by the truck
    def drive(self, miles):
        self.milesDriven = self.milesDriven + miles
    
    #A method that updates the time of the truck
    def changeTime(self, time):
        self.startTime = self.startTime + datetime.timedelta(minutes = time)
    
    #A method that changes the absolute time of the truck
    def changeExactTime(self, time):
        self.startTime = time

    
    

    

