class SimpleHashTable:
    def __init__(self,size=10):
        self.size = size
        self.table = [None]* size
    def _hash(self,key):
        return hash(key)%self.size
    def insert(self,key,value):
        index= self._hash(key)
        self.table[index]=(key,value)
    def get(self,key):
        index = self._hash(key)
        if self.table[index] is not None and self.table[index][0]==key:
            return self.table[index][1]
    def delete(self,key):
        index=self._hash(key)
        if self.table[index]is not None and self.table[index][0]==key:
            self.table[index]=None
            return True
        return False
if __name__=="__main__":
    ht=SimpleHashTable()
    ht.insert("apple",1)
    ht.insert("banana",2)
    print(ht.get("banana"))
    ht.delete("apple")
    print(ht.get("apple"))
