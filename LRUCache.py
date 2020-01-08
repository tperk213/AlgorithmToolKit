

class LinkedList:
    def __init__(self, key, val, previous = None):
        self.previous = previous
        self.next = None
        self.value = val
        self.key = key

    def insert(self, key, val):
        self.next = LinkedList(key, val, previous = self)
    
    def delete(self):
        if self.previous is not None:
            self.previous.next = self.next
        if self.next is not None:
            self.next.previous = self.previous

class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.table = {}
        self.head = None
        self.tail = None
    
    def delete(self, key):
        nodeToDelete = self.table[key]
        del self.table[key]
        if nodeToDelete == self.head and nodeToDelete == self.tail:
            self.head = None
            self.tail = None
            return
        elif nodeToDelete == self.tail:
            self.tail = nodeToDelete.previous
        nodeToDelete.delete()

    def moveToHead(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail = node.previous
        if node.previous is not None or node.next is not None:
            node.previous.next = node.next
            if node.previous.next is not None:
                node.previous.next.previous = node.previous
        if self.head is not None:
            self.head.previous = node
        node.next = self.head
        node.previous = None
        self.head = node

    def insertKeyValuePair(self, key, value):
        # check if room in table
        if len(self.table.keys()) and len(self.table.keys()) == self.maxSize:
            # if not delete the last entry
            temp = self.tail.previous
            self.delete(self.tail.key)
            self.tail = temp
        # create Node for key value
        node = LinkedList(key, value)
        # set head of list to node
        self.moveToHead(node)
        #check if its first node if so make it tail
        # enter key node in table
        self.table[key] = node
        if len(self.table.keys()) == 1:
            self.tail = self.table[key]
    
    def getValueFromKey(self, key):
        if key not in self.table:
            return None
        self.moveToHead(self.table[key])
        return self.table[key].value
    
    def getMostRecentKey(self):
        return self.head.key
        

def testLruOfSize(size, testContext):
    lru = LRUCache(size)
    

if __name__ == "__main__":
    
    letterMaps = {
        "a":0,
        "b":1,
        "c":2,
        "d":3,
        "e":4,
        "f":5,
        "g":6,
        "h":7,
        "i":8,
        "j":9,
    }
    letters = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j"]


    
    
    
    # cache = LRUCache(3)
    # cache.insertKeyValuePair("a",2)
    # cache.insertKeyValuePair("b",3)
    # t = cache.getMostRecentKey()
    # cache.insertKeyValuePair("c",5)
    # cache.insertKeyValuePair("d",1)
    # b = cache.getValueFromKey("b")
    # cache.insertKeyValuePair("a",5)
    # a = cache.getValueFromKey("d")
    # print("done")
    