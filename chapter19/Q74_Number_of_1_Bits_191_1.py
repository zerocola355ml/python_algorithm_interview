# My solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            if n & 1:
                result += 1
            n >>= 1
        return result