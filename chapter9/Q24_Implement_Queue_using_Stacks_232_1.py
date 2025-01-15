class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return None
        while self.stack:
            self.temp.append(self.stack.pop())
        result = self.temp.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return result

    def peek(self) -> int:
        if not self.stack:
            return None
        while self.stack:
            self.temp.append(self.stack.pop())
        result = self.temp.pop()
        self.stack.append(result)
        while self.temp:
            self.stack.append(self.temp.pop())
        return result

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()