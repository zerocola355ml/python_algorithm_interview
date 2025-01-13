class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        for char in sorted(set(s)):
            char_index = s.find(char)

            if set(s) == set(s[char_index:]):
                s = re.sub(char, "", s[char_index:])  # 처음에 re.sub(r"[char]", "", s[char_index:]) 라 해서 틀림
                return char + self.removeDuplicateLetters(s)