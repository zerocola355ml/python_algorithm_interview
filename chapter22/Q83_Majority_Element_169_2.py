# Answer1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > len(nums) // 2:
                return num