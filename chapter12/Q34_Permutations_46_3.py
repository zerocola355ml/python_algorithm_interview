# Answer
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev = []

        def helper(elements):
            if len(elements) == 0:
                result.append(prev[:])

            for e in elements:
                next_element = elements[:]
                next_element.remove(e)

                prev.append(e)
                helper(next_element)
                prev.pop()

        helper(nums)
        return result