

 vector <int>  str_vec(string s)
 {
    vector <int>v(26,0) ;
    
    for(int i = 0 ; i<s.size(); i++)
    {
        v[s[i]-'a']++ ;
    }
    return v ;
 }

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
     map<vector<int>,vector<string>> map  ;
     vector <vector<string>> v ; 
     for(int i = 0 ; i<strs.size(); i++)
     {
        map[str_vec(strs[i])].push_back(strs[i]) ;
     }
    for(auto it = map.begin() ; it!=map.end();it++)
    {
        v.push_back(it->second) ;
    }

    return v ; 
}
} ;
// if  i want  to explain what  i do exactly here  i try to find a vector of 26 emlement 
// so every string will have a vector and if two vector  are anagram they will have same vector 
// afeter  i declare a map this vecotr as a key and this string as value 