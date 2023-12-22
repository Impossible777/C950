class truck:
    def __init__(self, maxPackages, avgSpeed, packages = [], currentLocation = 'HUB'):
        self.maxPackages = maxPackages
        self.avgSpeed = avgSpeed
    
    def __str__(self):
        return f"This truck is currently at {self.currentLocation} and has {self.packages} on board."
    
    def addPackages(self, package):
        self.packages.append(package)
    
    def removePackages(self, package):
        self.packages.remove(package)
    
    def currentLocation(self, location):
        self.currentLocation = location

    
    

    

