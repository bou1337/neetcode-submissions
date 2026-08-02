
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> map ;
        vector <vector<string>> v ;

        for (string i  : strs)
        {
            string key  = i ;
            sort(key.begin(), key.end()) ;
            map[key].push_back(i) ;
        }

        for (auto it = map.begin(); it!=map.end(); it++)
        {
            v.push_back(it->second) ;
        }
        return v ;

}
} ;
// if  i want  to explain what  i do exactly here  i try to find a vector of 26 emlement 
// so every string will have a vector and if two vector  are anagram they will have same vector 
// afeter  i declare a map this vecotr as a key and this string as value 