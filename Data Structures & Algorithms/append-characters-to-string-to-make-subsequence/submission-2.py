class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
         
        j = 0 
        c = 0
        for  i in range(len(t)):

            while j < len(s):
                if t[i]==s[j]:
                    c +=1
                    j +=1
                    break 
                j +=1 
            if j == len(s):
                break 
        return len(t) - c                
