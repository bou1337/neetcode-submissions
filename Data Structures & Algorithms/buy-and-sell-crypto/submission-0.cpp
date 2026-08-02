class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int profit  = 0 ;
        int  min  =  prices[0] ;
        for(int  i = 1 ; i<prices.size();i++)
        {
            if(min<prices[i])
            {
                profit = max(profit ,prices[i]-min) ;
            }
            else 
          {
            min  = prices[i] ;
          }
    
        
        }

        return profit ;
    }
};
