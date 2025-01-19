# My solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = dict()
        length_of_longest_substring = 0
        left = 0

        for right, char in enumerate(s):
            if char in last_index and last_index[char] >= left:
                left = last_index[char] + 1
            length_of_longest_substring = max(length_of_longest_substring, right - left + 1)
            last_index[char] = right

        return length_of_longest_substring