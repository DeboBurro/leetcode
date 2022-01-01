class Node:
    def __init__(self, val = None, key = None):
        self.val = val
        self.key = key
        self.pre = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key in self.d:
            self.insert_to_head(self.remove_node(self.d[key]))
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.d[key].key = key
            self.insert_to_head(self.remove_node(self.d[key]))
        else:
            if len(self.d) == self.cap:
                node = self.remove_node(self.tail.pre)
                del self.d.pop[node.key]
            tmp = Node(value, key)
            self.d[key] = tmp
            self.insert_to_head(tmp)
            
    def remove_node(self, cur):
        pre = cur.pre
        nxt = cur.nxt
        pre.nxt = nxt
        nxt.pre = pre
        return cur
            
    def insert_to_head(self, cur):
        head = self.head
        first = self.head.nxt
        head.nxt = cur
        first.pre = cur
        cur.nxt = first
        cur.pre = head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)