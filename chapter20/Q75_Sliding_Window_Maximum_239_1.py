# My solution
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        M = 0
        heap = []
        for i in range(k):
            if nums[i] >= nums[M]:
                M = i
            else:
                heapq.heappush(heap, (-nums[i], i))

        right = k
        result = [nums[M]]

        while right < len(nums):
            left = right - k + 1
            if nums[right] >= nums[M]:
                M = right
                heap = []
            else:
                heapq.heappush(heap, (-nums[right], right))
                if left > M:
                    M = -1
                    while M < 0:
                        temp = heapq.heappop(heap)[1]
                        if temp >= left:
                            M = temp
            result.append(nums[M])
            right += 1

        return result