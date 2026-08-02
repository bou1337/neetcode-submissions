class Solution:
    def scoreOfString(self, s: str) -> int:
        
        i  = 1
        rs = 0 
        if len(s)<1:
            return abs(ord(s[i]))
        while i  < len(s):
            ab =  abs(ord(s[i]) - ord(s[i-1]))
            rs += ab 
            i +=  1  
        return rs  