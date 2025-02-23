# My solutions2
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = map(str, nums)

        nums = sorted(
            nums, key = cmp_to_key(lambda x, y: 1 if x + y < y + x else -1)
        )

        return str(int("".join(nums)))