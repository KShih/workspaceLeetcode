'''
    dummy -> entry -> entry ->entry -> entry(tail)
    entryFinder = { key, {key, value} }
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0 # Current size of the cache (linklist)
        self.dummy = Node(-1,-1)
        self.tail = self.dummy # Point to the end of list
        self.entryFinder = {} #  { key, {key, value} }

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        entry = self.entryFinder.get(key)
        if entry is not None:
            self.renew(entry)
            return entry.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        entry = self.entryFinder.get(key)
        if entry is None:
            entry = Node(key, value)
            self.entryFinder[key] = entry

            # link new node to the tail of list
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry

            # Check if over the capcity
            if self.size < self.capacity:
                self.size += 1
            else:
                # Remove the Node at the most front of the list
                head = self.dummy.next
                if head is not None:
                    self.dummy.next = head.next
                    head.next.prev = self.dummy
                # Remove it from dictionary
                del self.entryFinder[head.key]
        else:
            # Put the renew data, whose key exist but the value update, the the tail of the list
            entry.value = value
            self.renew(entry)

    # Move the used data to the end of the list
    def renew(self, entry):
        if self.tail != entry:
            # delete(jump over) the entry and linked
            prevNode = entry.prev
            nextNode = entry.next
            prevNode.next = nextNode
            nextNode.prev = prevNode

            # link the entry to the tail of the list
            entry.next = None
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
