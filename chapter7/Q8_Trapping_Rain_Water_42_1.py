class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        water = 0
        left, right = 0, len(height) - 1

        while right - left > 1:
            if height[left] < height[right]:
                mid = left + 1
                ground = 0
                while height[left] > height[mid]:
                    ground += height[mid]
                    mid += 1
                water += height[left] * (mid - left - 1) - ground
                left = mid
            else:
                mid = right - 1
                ground = 0
                while height[right] > height[mid]:
                    ground += height[mid]
                    mid -= 1
                water += height[right] * (right - mid - 1) - ground
                right = mid

        return water