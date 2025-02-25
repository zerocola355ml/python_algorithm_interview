# Answer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            # nums = numbers[k + 1:] - 슬라이싱하면 느려진다. 대신 bisect 의 파라미터로 k + 1 넣기
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1