# My solution
class Trie:

    def __init__(self):
        self.set = set()

    def insert(self, word: str) -> None:
        self.set.add(word)

    def search(self, word: str) -> bool:
        return word in self.set

    def startsWith(self, prefix: str) -> bool:
        for word in self.set:
            if prefix == word[:len(prefix)]:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)