class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = [None] * k
        self.size = k
        self.p1 = k - 1
        self.p2 = 0

    def insertFront(self, value: int) -> bool:
        if self.dq[self.p1] is None:
            self.dq[self.p1] = value
            self.p1 = (self.p1 - 1) % self.size
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.dq[self.p2] is None:
            self.dq[self.p2] = value
            self.p2 = (self.p2 + 1) % self.size
            return True
        return False

    def deleteFront(self) -> bool:
        if self.dq[(self.p1 + 1) % self.size] is not None:
            self.p1 = (self.p1 + 1) % self.size
            self.dq[self.p1] = None
            return True
        return False

    def deleteLast(self) -> bool:
        if self.dq[(self.p2 - 1) % self.size] is not None:
            self.p2 = (self.p2 - 1) % self.size
            self.dq[self.p2] = None
            return True
        return False

    def getFront(self) -> int:
        if self.dq[(self.p1 + 1) % self.size] is not None:
            return self.dq[(self.p1 + 1) % self.size]
        return -1

    def getRear(self) -> int:
        if self.dq[(self.p2 - 1) % self.size] is not None:
            return self.dq[(self.p2 - 1) % self.size]
        return -1

    def isEmpty(self) -> bool:
        return (self.p1 - self.p2 + 1) % self.size == 0 and self.dq[(self.p1 + 1) % self.size] is None

    def isFull(self) -> bool:
        return (self.p1 - self.p2 + 1) % self.size == 0 and self.dq[(self.p1 + 1) % self.size] is not None

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()