# Answer2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return list(zip(*count.most_common(k)))[0]