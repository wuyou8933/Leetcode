class DLinkedNode(): 
    def __init__(self,k,v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.head = DLinkedNode(0, 0)
        self.tail = DLinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.cache:
            currNode = self.cache[key]
            self._remove(currNode)
            self._add(currNode)
            return currNode.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        currNode = DLinkedNode(key, value)
        self._add(currNode)                 # add to DLL
        self.cache[key] = currNode          # store value in cache i.e hashmap.
        if len(self.cache) > self.size:     # evict LRU now from both DLL,HM
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
            
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)