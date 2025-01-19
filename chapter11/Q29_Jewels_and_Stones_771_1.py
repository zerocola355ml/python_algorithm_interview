# My solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        count = 0

        for jewel in jewels:
            count += counter[jewel]

        return count