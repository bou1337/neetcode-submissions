class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> v1(26,0) ;
        vector<int> v2(26,0) ;
        if(s.size()!=t.size())
        return false ;
        for(size_t i = 0 ; i<s.size(); i++)
        {
            v1[s[i]-'a']++ ;
            v2[t[i]-'a']++  ;
        }

        return (v1==v2) ;
    }
};
