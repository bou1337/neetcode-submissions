class Solution:

    def encode(self, strs: List[str]) -> str:

        s =""
        for  i in strs:
            s +=i+"#*"
        return s

    def decode(self, s: str) -> List[str]:

        l=[]
        r=""
        i = 0 
        while(i<len(s)):
            if(i+1<len(s) and s[i]=='#'and s[i+1]=='*'):
                l.append(r)
                r=""
                i+=2
            else:
                r+=s[i]
                i+=1

        return l 