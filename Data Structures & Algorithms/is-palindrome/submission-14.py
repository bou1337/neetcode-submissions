class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = len(s) -1 
        r = 0 

        while r < l :
            if (s[r].isalpha() or s[r].isdigit())==False :
                r +=1 
                continue 
            if (s[l].isalpha() or s[l].isdigit())== False :
                l -=1
                continue 
            if  s[r].upper()!=s[l].upper():
                return False 
            r +=1
            l -=1
        return True 
    