class Solution {
public:

    string encode(vector<string>& strs) {

        string str = ""  ;
        string i ;
        for(int  i = 0  ;  i<strs.size() ; i++)
        {
            str=str+strs[i]+"1337" ;
        }
        return str ;
    }

    vector<string> decode(string s) {
        vector <string> str ;
        
        size_t  pos =0 ;
        while((pos=s.find("1337"))!=string::npos)
        {
            str.push_back(s.substr(0,pos)) ;
            s.erase(0 , pos+4) ;
        }

        return str ;
    }

};
