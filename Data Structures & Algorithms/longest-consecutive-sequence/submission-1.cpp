
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

       
       int max  ;
       int max_max = 0  ;
        unordered_set <int> set ;

        for(int i:nums)
        {
            set.insert(i) ;
        }

        for( int  i = 0  ; i<nums.size() ; i++)
        {
            max = 1 ;
            int j = 1 ;
             while(set.find(nums[i]+j)!=set.end())
             {
                max++ ;
                j++ ;
             }

             if(max>max_max)
             max_max = max ;

        }

     return    max_max ;
    }

     
};