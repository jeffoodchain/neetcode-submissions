class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.last = None

# making a doubly linked list like structure (without inserting and find the element)

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if (self.head == None and self.tail == None): 
            return True
        return False

    def append(self, value: int) -> None:
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.last = self.tail
            self.tail = node

    def appendleft(self, value: int) -> None:        
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.head.last = node
            node.next = self.head
            self.head = node

    def pop(self) -> int:
        if self.tail:
            if self.head == self.tail:
                popped = self.head
                self.head = None
                self.tail = None
                return popped.val
            else:
                popped = self.tail
                self.tail.last.next = None # let last node's next = None
                self.tail = self.tail.last # making the tail the last node 
            return popped.val
        return -1
        
    def popleft(self) -> int:
        if self.head: 
            if self.head == self.tail:
                popped = self.head
                self.head = None
                self.tail = None
                return popped.val
            else: 
                popped = self.head
                self.head.next.last = None # let last node's next = None
                self.head = self.head.next # making the head the last node 
                return popped.val
        return -1
