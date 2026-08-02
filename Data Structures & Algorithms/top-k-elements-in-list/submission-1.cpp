class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int  , int> map  ;
        vector<vector<int>> v(nums.size()+1) ;
        vector <int> result ;
        for(int i  =0 ; i< nums.size();i++)
        {
            map[nums[i]]++ ;
        }

        for(auto it =  map.begin(); it!=map.end(); it++)
        {
            v[it->second].push_back(it->first) ;//
        }

        for(int i =v.size()-1 ;  i>=0 ; i--)
        {
            if(k)
            {  
               int  j = v[i].size() ;
                while(j&&k)
                {   

                    result.push_back(v[i][j-1]) ;
                    v[i].pop_back() ;
                    k-- ;
                    j-- ;
                }
            }
        }
        return result ;
    }
};
