# My solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if not matrix[row][0] <= target <= matrix[row][-1]:
                continue
            else:
                left, right = 0, len(matrix[row]) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[row][mid] > target:
                        right = mid - 1
                    elif matrix[row][mid] < target:
                        left = mid + 1
                    else:
                        return True
        return False