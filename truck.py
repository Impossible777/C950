class truck:
    def __init__(self, maxPackages, avgSpeed, packages = [], currentLocation = 'HUB'):
        self.maxPackages = maxPackages
        self.avgSpeed = avgSpeed
        self.packages = packages
        self.currentLocation = currentLocation
    
    def __str__(self):
        return f"This truck is currently at {self.currentLocation} and has {self.packages} on board."
    
    def addPackages(self, package):
        if len(self.packages) >= self.maxPackages:
            print("This truck is full.")
        else:
            self.packages.append(package)
    
    def removePackages(self, package):
        self.packages.remove(package)
    
    def currentLocation(self, location):
        self.currentLocation = location

    
    

    

