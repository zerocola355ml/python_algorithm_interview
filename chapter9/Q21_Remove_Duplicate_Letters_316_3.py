class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char not in seen:
                while stack and counter[stack[-1]] > 0 and stack[-1] > char:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)

        return "".join(stack)  # str(stack) 해서 틀림