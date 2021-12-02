class DLinkNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {} ###

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key, value):
        if key not in self.cache:
            node = DLinkNode(key, value)
            self.cache[key] = node ###
            self.addToHead(node)
            self.size += 1 ###
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1 ###
        else:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def addToHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node