class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_brackets = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in close_brackets:
                if not stack or stack.pop() != close_brackets[char]: # empty stack case
                    return False
            else:
                stack.append(char)

        return not stack