class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        v1 = [0]*26
        v2  = [0]*26

        for i in s :
            v1[ord(i)-ord('a')] +=1
        
        for j in t:
            v2[ord(j)-ord('a')] +=1
        return v1==v2 

