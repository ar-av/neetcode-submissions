class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit=0

        for i in range(n):
            for j in range (i+1,n):
                diff=(prices[j]-prices[i])
                max_profit=max(max_profit,diff)
                
        return max_profit