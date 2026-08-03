class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k =  len(nums) 
        c= 0 
        while val  in  nums:
            c +=1
            nums.remove(val)
        return  k -c 

    
