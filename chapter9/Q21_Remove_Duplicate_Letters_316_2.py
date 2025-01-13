class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            char_index = s.index(char)
            tail = s[char_index:]
            if set(s) == set(tail):
                return char + self.removeDuplicateLetters(tail.replace(char, ""))
        return ""