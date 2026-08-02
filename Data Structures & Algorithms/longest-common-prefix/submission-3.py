class Solution:
    def pre(self,s1, s2):
        s =""
        i = 0
        i = 0
        sz = min(len(s1),len(s2))
        while(i<sz and s1[i]==s2[i] ):
            i +=1 
        return s1[:i]
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        for  i in  strs:
            p = self.pre(s,i)
            s = p 
            if p=="":
                break 
        return p 