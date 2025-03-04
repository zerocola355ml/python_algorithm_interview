# Answer3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        result = []
        it = iter(nums)

        for i, v in enumerate(itertools.islice(it, k)):
            while q and nums[q[-1]] < v:
                q.pop()
            q.append(i)
        result.append(nums[q[0]])

        for i, v in enumerate(it, start=k):
            while q and nums[q[-1]] < v:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.popleft()
            result.append(nums[q[0]])

        return result