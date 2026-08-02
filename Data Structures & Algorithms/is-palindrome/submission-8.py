class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        left = 0 
        right = len(s) -1 
        while(left<right):
            if(s[left].isalnum()==False):
                left+=1
                continue
            if(s[right].isalnum()==False):
                right-=1
                continue 
            if(s[right].upper()!=s[left].upper()):
                return False
            right -=1
            left +=1
                    
        return True 
            