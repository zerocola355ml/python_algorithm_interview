# Answer2
class TrieNode:
    def __init__(self):
        self.is_end = False  # 단어의 끝 여부
        self.children = {}   # 자식 노드를 저장할 dict

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # 필요할 때만 노드 생성
            node = node.children[char]
        node.is_end = True  # 단어의 끝 표시

    def findNode(self, prefix: str):
        """주어진 prefix가 있는 노드를 찾음"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word: str) -> bool:
        """완전한 단어 검색"""
        node = self.findNode(word)
        return node is not None and node.is_end  # 존재하고 단어 끝이면 True

    def startsWith(self, prefix: str) -> bool:
        """접두사(prefix) 확인"""
        return self.findNode(prefix) is not None
