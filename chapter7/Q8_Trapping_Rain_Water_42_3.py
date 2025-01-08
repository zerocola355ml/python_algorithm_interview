class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        stack = []

        for curr in range(len(height)):
            while stack and height[stack[-1]] < height[curr]:
                prev = stack.pop()
                if stack:
                    width = curr - stack[-1] - 1
                    water += width * (min(height[stack[-1]], height[curr]) - height[prev])

            stack.append(curr)

        return water