class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        i  = 0 
        buy_day = 0
        while i < len(prices)-1:

            if prices[buy_day]>prices[i+1]:
                buy_day = i+1
            else :
                profit += prices[i+1] - prices[buy_day]
                buy_day = i + 1
                
            i+=1

        return profit 
            
