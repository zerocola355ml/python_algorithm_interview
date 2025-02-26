# My solution
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit = x ^ y
        result = 0
        while bit > 0:
            result += bit % 2
            bit = bit // 2
        return result