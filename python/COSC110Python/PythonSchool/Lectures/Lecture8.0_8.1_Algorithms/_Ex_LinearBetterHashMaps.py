

class LinearMap:

    def __init__(self):
        self.items = []
        self.count = 0

    # constant time: O(1)
    # just adds to end of list, always the same.
    def add(self, k, v):
        self.items.append((k, v))
        self.count += 1

    # linear time: O(n)
    # keeps looking (in operator) until it finds the key.
    def get(self, k):
        for key, val in self.items:
            if key == k:
                return val
        return KeyError

    # constant time: O(1)
    # because we keep track of count in add method
    def length(self):
        return self.count




class BetterMap:

    # making a list of linear maps
    def __init__(self, n=10):
        self.maps = []
        self.linMapCount = n
        for i in range(n):
            self.maps.append(LinearMap()) # contains 100 linear maps


    # note: k = any unmutable object that can be hashed. hash(k) returns integer
    # that we use to find index. Using % in case hash(k) is too large for len. So different
    # hash values wrap to same index. But hash function spreads things out evenly so we expect
    # that we access the linear maps in list about same number of times.
    # note: HASH: two objects with different vals can return same hash value
    # note: HASH: equivalent hashable objects always return same value.

    # note: finding which map a particular key is stored in.
    # constant time: O(1): just getting an element
    def findMap(self, k):
        index = hash(k) % len(self.maps) # bounding with %
        return self.maps[index]

    # constant time: O(1) - no need to search in all the lists.
    # It appends key value tuple to list.
    def add(self, k, v):
        linMap = self.findMap(k) # key 5 = map 5 (one map per slot)
        linMap.add(k, v)

    # linear time: O(n) - no need to search in all the lists.
    # But about 100 times faster than before because we narrow out lists to one.
    # help but isn't this technically constant time O(1) because we keep a fixed number of linear maps?
    def get(self, k):
        linMap = self.findMap(k) # constant time and reducing searchables by just finding the correct map
        return linMap.get(k) #  O(n) now we search in that particular map.










class HashMap:

    # note: hashmap contains 1 better map that contains 2 linearmaps.
    def __init__(self):
        self.maps = BetterMap(2)
        #self.numLinMaps = 2
        self.itemCount = 0 # count of items in the hashtable.

    # constant time: O(1) - keeping size of lists bounded gives constant time on average
    # (assuming we only copy to new location once in a while)
    def get(self, k):
        return self.maps.get(k)

    def add(self, k, v):
        # note: if item num == same as items in linear map, then resize.
        if self.itemCount == self.maps.linMapCount:
            self.resize()

        self.maps.add(k, v)
        self.itemCount += 1


    def resize(self):
        newMaps = BetterMap(self.itemCount * 2)

        for aMap in self.maps.maps:
            for k, v in aMap.items:
                newMaps.add(k, v) # flattening out ? note help
                #self.numLinMaps += 1

        self.maps = newMaps





def main():
    print("\nTesting linear map")
    aMap = LinearMap()
    aMap.add(1, 2)
    print(aMap.get(1))
    print(aMap.get(10))

    # appending 10 different lists to our list of maps.
    print("\nTesting better map")
    better = BetterMap() # we can input at index 9 at the fourth adding because better map starts with 10 linear maps.
    better.add(4, 144)
    better.add(0, 100)
    better.add(1, 111)
    better.add(9, 199)
    better.add(4, 444) # stores it but no way to access because we're not supposed to do this.
    # note: each individual linear map stores SINGLE key,value pairs.
    better.add(5, 155)
    better.add(6, 166)
    better.add(8, 188)
    better.add(2, 122)
    better.add(3, 133)
    better.add(7, 177)

    for i in range(10):
        linMapValue = better.get(i)
        print("i = ", i, "    v = ", linMapValue, sep="")



    print("\n\nTesting hashmap: ")
    '''
    # note: this fails because we add at indexes 8 and 10 and since the hashmap goes from carrying
    # 2 linear maps to carrying 4, the indexes are only 0,1,2,3 so the % operation in findMap() finds a map
    # at an index that may already CONTAIN a map! That's why the slot we thought the map should be found in is empty
    # and why another slot has two maps which is why we get keyerror when we try to print all and find some empty map slots.
    hasher = HashMap()
    hasher.add(0, 100)
    hasher.add(8, 188)
    hasher.add(10, 110)
    hasher.add(2, 122)
    for i in range(hasher.itemCount):
        print("i = ", i, "   v = ", hasher.get(i), sep="")
    '''
    # note: but this passes because all indexes are in the length range so all safe and no chance of inputting in other slot,
    # note leaving others empty.
    hasher = HashMap()
    hasher.add(0, 100)
    hasher.add(3, 110)
    hasher.add(1, 188)
    hasher.add(2, 122)
    for i in range(hasher.itemCount): # itemCount == map count because each map houses exactly 1 item-value pair.
        print("i = ", i, "   v = ", hasher.get(i), sep="")



if __name__ == "__main__":
    main()