class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        lst =[0]*26

        if(len(s)!=len(t)):
            return False
        for  i  in range(len(s)):
            lst[ord(s[i]) -ord('a')]+=1
            lst[ord(t[i])-ord('a')]-=1
        
        for  j in  lst:
            if(j!=0):
                return  False 
        return True 