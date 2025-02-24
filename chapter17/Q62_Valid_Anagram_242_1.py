# My solution1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        for char in s_count:
            if s_count[char] != t_count[char]:
                return False

        return True