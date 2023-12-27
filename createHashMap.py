
class createHashMap:
    def __init__(self, initial_capacity=60):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
    
    def insert(self, item):
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(item)

    def insert(self, key, array):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = array
                return True
        
        key_value = [key, array]
        bucket_list.append(key_value)
        return True
    
    def search(self, key):
       bucket = hash(key) % len(self.table)
       bucket_list = self.table[bucket]
       

       for stored_key, stored_item in bucket_list:
            if stored_key == key:
                return stored_item
    
       return None
    
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)
    
    def update_array_index(self, key, index, new_value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1][index] = new_value
                return True
        
        return False
