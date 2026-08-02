class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> map ;

        for(int i : nums)
            map[i] = i ;

        return (map.size()!=nums.size()) ;
    }
};