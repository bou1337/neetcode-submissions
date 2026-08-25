class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        left  = len(s) -1

        while s[left]==" ":
            left -=1
        size  =  0

        while left>=0 and  s[left] !=" ":
            left -=1
            size +=1 
        return size 
    

