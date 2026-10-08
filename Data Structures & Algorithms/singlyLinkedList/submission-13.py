class Node:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.nextNode = nextNode

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        curr = self.head
        i = 0
        print(self.head.val)
        while curr and curr.nextNode:
            if i == index:
                break
            i += 1
            curr = curr.nextNode
        if i < index:
            return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return
        tmp = self.head
        self.head = Node(val, tmp)
        curr = self.head
        self.debug()

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return
        curr = self.head
        while curr.nextNode:
            curr = curr.nextNode
        curr.nextNode = Node(val)
        self.debug()
    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            if self.head.nextNode is None:
                self.head = None
            else:
                self.head = self.head.nextNode
            return True
        curr = self.head

        for i in range(index-1):
            curr = curr.nextNode

        if curr is None or curr.nextNode is None:
            return False
        else:
            if curr.nextNode.nextNode is None:
                curr.nextNode = None
                return True
            else:
                tmp = curr.nextNode.nextNode
                curr.nextNode = tmp
                return True

    def getValues(self) -> List[int]:
        out = []
        if self.head is None:
            return out
        curr = self.head
        while curr.nextNode:
            out.append(curr.val)
            curr = curr.nextNode
        out.append(curr.val)
        return out

    def debug(self) -> None:
        curr = self.head
        print("[DEBUG]")
        while curr.nextNode is not None:
            print(curr.val, end = "")
            curr = curr.nextNode
        print(curr.val, end="")
        print("\n_________")