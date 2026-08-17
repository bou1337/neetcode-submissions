class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26

        if len(t)!=len(s):
            return False 
        for   i  in range(len(s)):
            count[ord(s[i])-ord('a')] +=1
            count[ord(t[i])-ord('a')] -=1
        return count==[0]*26
