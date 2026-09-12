class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def insert(self, node):
        node.next, node.prev = self.right, self.right.prev
        self.right.prev = node
        node.prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value) 
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap: 
            del self.cache[self.left.next.key]
            self.remove(self.left.next) 

# we have a hashmap with keys and nodes as values       
# 
# put
# if no capacity, grab left.next and remove
# 
#
# get and put:
# whenever a value is added or getted, we add the value to front
# to access value, we get its key from hashmap
# the hashmap points to the object
# so we can go to the object this way

# get:
# make prev = right.prev