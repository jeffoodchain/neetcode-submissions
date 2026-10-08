class Heap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, v: int):
        # leftchild = 2 * i
        # rightchild = 2 * i + 1
        # parent = i // 2
        self.heap.append(v)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()

        minimum = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1

        while 2 * i < len(self.heap):
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]:
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                break
        return minimum

    def top(self):
        if self.heap > 1:
            return self.heap[1]
        return None

    def heapify(self, arr: List[int]):
        pass   

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap()
        for n in nums:
            self.heap.push(n)
        self.k = k

    def add(self, val: int) -> int:
        self.heap.push(val)
        
        popped = []
        
        while len(self.heap.heap) > 1:
            popped.append(self.heap.pop())
        
        for p in popped:
            self.heap.push(p)

        return popped[-self.k]