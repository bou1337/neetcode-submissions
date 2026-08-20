class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        left  = len(arr) -1
        right_max = 0
        result=[-1]*(left+1)
        while left >0 :
            if arr[left] > right_max:
                right_max = arr[left]
            result[left-1] = right_max
            left -=1
        return result 
         
            
