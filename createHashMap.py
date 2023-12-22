class createHashMap:
    def __init__(self, initial_capacity=10):
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
       print(bucket_list)

       if key in bucket_list:
           item_index = bucket_list.index(key)
           return bucket_list[item_index]
       else:
           return None
    
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)