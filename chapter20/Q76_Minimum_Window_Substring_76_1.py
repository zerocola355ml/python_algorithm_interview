# My solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_checked = set()
        char_count_t = collections.Counter(t)
        num_of_char = len(char_count_t.keys())
        char_count_s = collections.defaultdict(int)

        i = 0
        left = None
        while len(char_checked) < num_of_char:
            if i == len(s):
                return ""
            if s[i] in char_count_t:
                if left is None:
                    left = i
                right = i
                char_count_s[s[i]] += 1
                if char_count_s[s[i]] == char_count_t[s[i]]:
                    char_checked.add(s[i])
            i += 1
        while char_count_s[s[left]] > char_count_t[s[left]]:
            char_count_s[s[left]] -= 1
            left += 1
            while s[left] not in char_count_t:
                left += 1

        result = s[left:right + 1]

        while i < len(s):
            if s[i] in char_count_t:
                char_count_s[s[i]] += 1
                while char_count_s[s[left]] > char_count_t[s[left]]:
                    char_count_s[s[left]] -= 1
                    left += 1
                    while s[left] not in char_count_t:
                        left += 1
                if i - left + 1 < len(result):
                    result = s[left: i + 1]
            i += 1

        return result