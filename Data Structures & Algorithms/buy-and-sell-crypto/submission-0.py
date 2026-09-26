class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minx=prices[0]
        max_profit=0

        for price in prices:
            minx=min(minx, price)
            profit = price - minx
            max_profit = max(profit, max_profit)
        
        return max_profit