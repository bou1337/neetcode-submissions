class Solution:
    def scoreOfString(self, s: str) -> int:
        
        i  = 1
        rs = 0 
        while i  < len(s):
            ab =  abs(ord(s[i]) - ord(s[i-1]))
            rs += ab 
            i +=  1  
        return rs  