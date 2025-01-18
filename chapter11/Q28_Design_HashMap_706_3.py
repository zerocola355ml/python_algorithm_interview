# Answer2
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size
        # self.table = [[]]*self.size 이렇게 했다가 얕은 복사라서 오답

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if not self.table[index]:
            self.table[index] = ListNode(key, value)
            return
        prev = self.table[index]
        if prev.key == key:
            prev.value = value
            return
        while prev:
            if prev.key == key:
                prev.value = value
                return
            if not prev.next:
                break
            prev = prev.next
        prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if not self.table[index]:
            return -1
        prev = self.table[index]
        while prev:
            if prev.key == key:
                return prev.value
            prev = prev.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if not self.table[index]:
            return
        prev = self.table[index]
        if prev.key == key:
            if prev.next:
                self.table[index] = prev.next
            else:
                self.table[index] = None
            return
        while prev.next:
            if prev.next.key == key:
                break
            prev = prev.next
        if prev.next:
            prev.next = prev.next.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)