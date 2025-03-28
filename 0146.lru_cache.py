class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.map = {}
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNode(self, new_node):
        next_node = self.head.next
        self.head.next = new_node
        new_node.next = next_node
        new_node.prev = self.head
        next_node.prev = new_node
    
    def delNode(self, del_node):
        prevnode = del_node.prev
        nextnode = del_node.next
        prevnode.next =  nextnode
        nextnode.prev = prevnode 

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        get_node = self.map[key]
        ret = get_node.val
        self.delNode(get_node)
        self.addNode(get_node)
        return ret


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            current_node = self.map[key]
            del self.map[key]
            self.delNode(current_node)
        
        if len(self.map) == self.cap:
            del self.map[self.tail.prev.key]
            self.delNode(self.tail.prev)
        
        new_node = self.Node(key, value)
        self.addNode(new_node)
        self.map[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
