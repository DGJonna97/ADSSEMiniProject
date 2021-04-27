import numpy as np

class Slots:
    def __init__(self, key=None, value=None):
        self.key = key
        self.list = [value]

class HashTable:
    def __init__(self, size, method, collisionType, probeType):
        self.size = size
        self.table = [None]*size
        self.method = method
        self.collisionType = collisionType
        self.probeType = probeType
        # It is a random int, which is a value between 0 and m-1
        self.a = np.random.randint(0, self.size - 1)

    # The search operation
    def Search(self, key):
        # The direct addressing technique for searching 
        if self.method=="DirectAddressing":
            return self.table[key]

        for i in range(0, len(self.table)):
            Slots = self.table[i]
            if Slots is not None:
                if Slots.key==key:
                    return Slots

    # The insert operation
    def Insert(self, key, value):
        h=self.hashFunctions(key)
        n = self.Search(h)
        if n is not None:
            # The chaining technique for collision handling
            if self.collisionType == "Chaining":
                n.list.append(value)
                return n.key
            # The open addressing technique for collision handling
            elif self.collisionType == "OpenAddressing":
                    # The Linear probing method for open addressing    
                    if self.probeType=="Linear":
                        probehash= h%self.size
                        #print("probehash", probehash, "size", self.size)
                        for i in range(probehash, len(self.table)):
                            potentialSlots = self.table[i]
                            if potentialSlots is None:
                                element = Slots(i, value)
                                self.table[i] = element
                                return i

                        for i in range(0, probehash-1):
                            potentialSlots = self.table[i]
                            if potentialSlots is None:
                                element = Slots(i, value)
                                self.table[i] = element
                                return i
                        print("Table overflow error")
                        return False
                    # The Quadratic probing method for open addressing 
                    if self.probeType == "Quadratic":

                        for i in range(0, len(self.table)-1):
                            probehash = (h + (i * i)) % self.size #c1 = 0 and c2 = 1
                            if self.table[probehash] is None:
                                element = Slots(probehash, value)
                                self.table[probehash] = element
                                return i
                        return False
                    # Double hashing method for open addressing 
                    # Double Hashing does not work completely, it finds a slot for most keys, but there is some overflows.
                    #I think it is due to the prime value, which I have set to be 9.
                    if self.probeType == "DoubleHashing":
                        h1k = int(key% self.size) # m = self.size
                        h2k = 1 + (key % (self.size - 9))
                        for i in range(0, len(self.table)):
                            nextspot= (h1k+(i*h2k))%self.size
                            if self.table[nextspot] is None:
                                element = Slots(h, value)
                                self.table[nextspot] = element
                                return True

                    print("Table overflow error", "h1k", h1k, "h2k", h2k)
                    return False

        element = Slots(h, value)
        # The direct addressing technique for inserting
        if self.method == "DirectAddressing":
            self.table[h]=element
        else:
            for i in range(0, len(self.table)):
                if self.table[i] is None:
                    self.table[i]=element
                    break
        return h

    def Delete(self, key):
        n = self.Search(int(key))
        if n is not None:
            self.table[int(key)] = None
            print("Deleted key ", key)
            return True
        print("Failed to delete value", key)

    def print(self):
        print("Table is of size: ", len(self.table))
        for i in range(0, len(self.table)):
            n = self.table[i]
            if n is not None:
                print("-"*25)
                print("Index:" , i, "Key:", n.key,", " ,"Value: ", n.list)

    def hashFunctions(self,key):
        # The direct addressing technique for deleting a key
        if self.method == "DirectAddressing":
            return int(key)
        # The division method function for hash tables
        elif self.method == "DivisionMethod":
            h= int(key) % self.size
            return int(key) % self.size
         # The multiplication method function for hash tables
        elif self.method == "MultiplicationMethod":
            return int(np.floor(((key * 0.671) % 1) * self.size))
        # The universal method function for hash tables
        elif self.method == "UniversalMethod":
            print("Key", key, "Hash", int(key)*self.a)
            return int(key)*self.a