# My solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }

        def helper(s):
            if len(s) == len(digits):
                result.append(s)
                return
            for char in keyboard[digits[len(s)]]:
                helper(s + char)
        helper("")
        return result