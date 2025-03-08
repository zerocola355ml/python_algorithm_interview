# My solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr = 0
        min_diff = 0
        min_idx = -1
        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            if curr < min_diff:
                min_diff = curr
                min_idx = i
        if curr < 0:
            return -1
        return 0 if min_idx == len(gas) - 1 else min_idx + 1
