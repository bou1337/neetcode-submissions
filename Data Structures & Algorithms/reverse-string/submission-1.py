class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = 0 
        left  = len(s) -1
        while right< left:
            swap = s[right]
            s[right] = s[left]
            s[left]  = swap 
            right +=1
            left -=1 
        

        