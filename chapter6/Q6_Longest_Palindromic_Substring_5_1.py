class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        result = ""
        for mid in range(len(s) - 1):
            if s[mid] == s[mid + 1]:
                left, right = mid, mid + 1
                while s[left] == s[right]:
                    temp = s[left:right + 1]
                    if len(temp) > len(result):
                        result = temp
                    left -= 1
                    right += 1
                    if left < 0 or right >= len(s):
                        break
            left = right = mid
            while s[left] == s[right]:
                temp = s[left:right + 1]
                if len(temp) > len(result):
                    result = temp
                left -= 1
                right += 1
                if left < 0 or right >= len(s):
                    break

        return result
