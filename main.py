from truck import truck
from createHashMap import createHashMap
import csv

# Path to the packageInfo.csv file
packageInfoPath = 'packageInfo.csv'
distanceTablePath = 'WGUPS Distance Table (1).csv'

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

def normalize_address(address):
    return ' '.join(address.split())

def getAddresses(address1, address2):
    
    
    # This function takes two addresses and returns the distance between them in miles
    with open(distanceTablePath, 'r', encoding='utf-8-sig') as distanceCSV:
        distanceReader = csv.reader(distanceCSV)
        for row in distanceReader:
            if row:
                normalized_address = normalize_address(row[0])
                if normalized_address(address1) == normalized_address:
                    addressOneIndex = row.index(address1)
                    break
        header = next(distanceReader, None)

        if header:
            for col_index, value in enumerate(header):
                normalized_address = normalize_address(value)
                if normalized_address(address2) == normalized_address:
                    addressTwoIndex = col_index
                    break
        
        return addressOneIndex, addressTwoIndex
    
def getCellValue(distanceTablePath, row_index, col_index):
    with open(distanceTablePath, 'r', encoding='utf-8-sig') as distanceCSV:
        distanceReader = csv.reader(distanceCSV)
        
        for _ in range(row_index + 1):
            row = next(distanceReader, None)
            if row is None:
                return None
            
        if row is not None and col_index < len(row):
            return row[col_index]
        else: return None


addressOne = "International Peace Gardens \n 1060 Dalton Ave S"
addressTwo = "Sugar House Park \n 1330 2100 S"
addressOneIndex, addressTwoIndex = getAddresses(addressOne, addressTwo)
print(getCellValue(distanceTablePath, addressOneIndex, addressTwoIndex))
            

    

