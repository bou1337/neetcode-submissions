class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0 
        c = 0
        for  i in range(len(s)):

            while j < len(t):
                if s[i]==t[j]:
                    c +=1
                    j +=1
                    break 
        
                j +=1 

        return c == len(s)
    


            