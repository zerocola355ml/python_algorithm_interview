# My solutions1
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""

        def custom_compare(s1, s2):
            if s1 + s2 > s2 + s1:
                return -1
            else:
                return 0

        nums = [str(x) for x in nums]
        nums.sort(key = cmp_to_key(custom_compare))
        result = str(int("".join(nums)))
        return result if result else ""

        # cmp_to_key에 대해 정리하자.