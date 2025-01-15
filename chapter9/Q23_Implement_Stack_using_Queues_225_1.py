class MyStack:

    def __init__(self):
        self.queue = collections.deque([])
        self.temp = collections.deque([])

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:
            return None
        while len(self.queue) > 1:
            self.temp.append(self.queue.popleft())
        result = self.queue.popleft()
        while self.temp:
            self.queue.append(self.temp.popleft())
        return result

    def top(self) -> int:
        if not self.queue:
            return None
        while len(self.queue) > 1:
            self.temp.append(self.queue.popleft())
        result = self.queue.popleft()
        while self.temp:
            self.queue.append(self.temp.popleft())
        self.queue.append(result)
        return result

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()