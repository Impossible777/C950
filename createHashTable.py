
class createHashTable:

    #Initializes the hash map with a table of 60 buckets
    def __init__(self, initial_capacity=60):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    #Allows the user to insert a key and an array into the hash map
    def insert(self, key, array):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #If the key already exists in the hash map, the array is updated
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = array
                return True
        #If the key does not exist in the hash map, the key and array are added to the hash map       
        key_value = [key, array]
        bucket_list.append(key_value)
        return True
    
    #Allows the user to look up a key in the hash map
    def look_up(self, key):
       bucket = hash(key) % len(self.table)
       bucket_list = self.table[bucket]
       
       #If the key exists in the hash map, the array is returned
       for stored_key, stored_item in bucket_list:
            if stored_key == key:
                return stored_item
       #If the key does not exist in the hash map, None is returned
       return None
    
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)
    
    #Allows the user to update a value in the array
    def update_array_index(self, key, index, new_value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1][index] = new_value
                return True
        
        return False
    
        
            

