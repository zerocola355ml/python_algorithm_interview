# Answer2
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        char_count_t = collections.Counter(t)
        required = len(t)

        left = 0
        min_length = float('inf')
        min_window = ""
        count = 0  # 현재 윈도우 내 t의 문자가 충족된 개수

        for right, char in enumerate(s):
            if char in char_count_t:
                if char_count_t[char] > 0:
                    count += 1
                char_count_t[char] -= 1

            while count == required:  # 모든 문자가 포함됨
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right+1]

                if s[left] in char_count_t:
                    char_count_t[s[left]] += 1
                    if char_count_t[s[left]] > 0:
                        count -= 1

                left += 1  # 윈도우 축소

        return min_window