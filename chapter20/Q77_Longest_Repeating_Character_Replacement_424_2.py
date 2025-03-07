# Answer
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        max_char_n = 0
        counts = collections.defaultdict(int)
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            max_char_n = max(max_char_n, counts[s[right - 1]])

            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

        return right - left