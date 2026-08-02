class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {


        int right = 0 ;
        int sum ;
        int left  =  numbers.size() -1 ;
        while(right<left)
        {
            sum   = numbers[left]+numbers[right]  ;
            if(sum == target)
            return {right+1, left+1} ;
            if(sum<target)
            right ++ ;
            if(sum>target)
            left-- ;
        }

        return  {0,0} ;
    }
};
