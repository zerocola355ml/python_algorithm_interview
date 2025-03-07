# Answer1
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        char_count_t = collections.Counter(t)
        char_count_s = collections.Counter()
        required = len(char_count_t)
        formed = 0

        left = 0
        min_length = float('inf')
        min_window = ""

        for right in range(len(s)):
            char = s[right]
            if char in char_count_t:
                char_count_s[char] += 1
                if char_count_s[char] == char_count_t[char]:
                    formed += 1

            while formed == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]

                left_char = s[left]
                if left_char in char_count_t:
                    char_count_s[left_char] -= 1
                    if char_count_s[left_char] < char_count_t[left_char]:
                        formed -= 1

                left += 1

        return min_window
