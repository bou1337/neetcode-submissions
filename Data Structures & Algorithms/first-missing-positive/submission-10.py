class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        data  = set(nums) 
        i  = 1 
        while i in data:
            i +=1 
        return i 
