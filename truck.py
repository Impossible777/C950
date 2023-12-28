import datetime

class truck:
    def __init__(self, number, maxPackages, avgSpeed, packages, startTime, currentLocation = '4001 South 700 East', milesDriven = 0.0):
        self.maxPackages = maxPackages
        self.avgSpeed = avgSpeed
        self.packages = packages
        self.currentLocation = currentLocation
        self.milesDriven = milesDriven
        self.startTime = startTime
        self.number = number
    
    def __str__(self):
        return f"This truck is currently at {self.currentLocation} and has {self.packages} on board."
    
    def addPackage(self, package):
        if len(self.packages) >= self.maxPackages:
            print("This truck is full.")
        else:
            self.packages.append(package)
    
    
    def removePackages(self, package):
        self.packages.remove(package)
    
    def currentLocation(self, location):
        self.currentLocation = location
    
    def drive(self, miles):
        self.milesDriven = self.milesDriven + miles
    
    def changeTime(self, time):
        self.startTime = self.startTime + datetime.timedelta(minutes = time)
    
    def changeExactTime(self, time):
        self.startTime = time

    
    

    

