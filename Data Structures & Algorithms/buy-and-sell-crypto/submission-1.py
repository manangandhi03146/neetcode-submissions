class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        mins=prices[0]
        for price in prices:
            mins=min(price, mins)
            maxProfit=max(maxProfit, price-mins)
        
        return maxProfit
