class Solution:
    def pre(self, s1, s2):
        i =  0 
        while(i < len(s1) and i < len(s2) and s1[i] == s2[i]):
            i += 1
        return s1[:i]
    def longestCommonPrefix(self, strs: List[str]) -> str:

        rs  = ""
        p = strs[0]
        for  i  in strs:
            rs =self.pre(p,i)
            p = rs
        return rs


