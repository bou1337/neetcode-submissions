class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> v1(26,0) ;
       // vector <int> v2(26,0) ;
        if(s.size()!=t.size())
        return false ;

        for(int i = 0 ;  i<s.size() ;i++)
        {
            v1[s[i]-'a']++ ;
            v1[t[i]-'a']-- ;
        }

        for(int  i : v1)
        {
            if(i!=0)
            return false  ;
        }

        return true;
    }
};
