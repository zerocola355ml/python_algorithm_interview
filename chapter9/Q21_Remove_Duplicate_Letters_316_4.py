class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index, seen, stack = dict(), set(), []

        for i in range(len(s)):
            last_index[s[i]] = i

        for i, char in enumerate(s):
            if char not in seen:
                while stack and last_index[stack[-1]] > i and stack[-1] > char:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)

        return "".join(stack)