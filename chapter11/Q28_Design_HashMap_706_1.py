# My Solution. (mistake)
class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        update = False
        for i, x in enumerate(self.keys):
            if x == key:
                self.values[i] = value
                update = True
                break
        if not update:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        for i, x in enumerate(self.keys):
            if x == key:
                return self.values[i]
        return -1

    def remove(self, key: int) -> None:
        for i, x in enumerate(self.keys):
            if x == key:
                del self.keys[i]
                del self.values[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)