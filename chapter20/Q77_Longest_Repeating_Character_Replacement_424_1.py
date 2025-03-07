# My solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        result = 0
        left = right = 0
        char_count = collections.defaultdict(int)
        char_max = set()
        char_max_count = 0
        change = 0
        char_sum = 0

        while right < len(s):
            while change <= k and right < len(s):
                char_count[s[right]] += 1
                if char_count[s[right]] == char_max_count:
                    char_max.add(s[right])
                elif char_count[s[right]] > char_max_count:
                    char_max.clear()
                    char_max.add(s[right])
                    char_max_count = char_count[s[right]]
                change = (right - left + 1) - char_max_count
                if change <= k:
                    result = max(result, right - left + 1)
                right += 1
            right -= 1

            char_count[s[left]] -= 1
            if s[left] in char_max:
                if len(char_max) == 1:
                    char_max_count -= 1
                else:
                    char_max.remove(s[left])
            left += 1
            if left > right:
                return result
            char_count[s[right]] -= 1
            change = (right - left + 1) - char_max_count

        return result