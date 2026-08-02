class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int pro = 1;
        int zero = 0;
        vector<int> prod;

        for (int i : nums) {
            if (i != 0)
                pro *= i;
            else
                zero++;
        }

        if(zero>1)
        return vector<int>(nums.size(),0) ;
        for(int i : nums)
        {
            if(zero)
            {
                if(i==0)
                prod.push_back(pro) ;
                else
                prod.push_back(0) ;
            }
            else 
            prod.push_back(pro/i) ;
        }

        return prod ;
       
    }
};
