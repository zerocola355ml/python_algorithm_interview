class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0
        ground = prices[0]

        for price in prices:
            if price < ground:
                ground = price
            else:
                profit = max(profit, price - ground)

        return profit