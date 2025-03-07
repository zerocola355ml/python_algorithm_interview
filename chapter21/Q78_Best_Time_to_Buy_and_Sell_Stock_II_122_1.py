# My solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stack = []

        for price in prices:
            if not stack or stack[-1] <= price:
                stack.append(price)
            else:
                profit += stack[-1] - stack[0]
                stack = [price]
        profit += stack[-1] - stack[0]

        return profit