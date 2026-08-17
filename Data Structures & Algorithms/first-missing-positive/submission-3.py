class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        data  =set(nums)
        i = 1
        for  _ in nums:
            
            if i not  in data:
                break
            i +=1
        return i
                
            
            