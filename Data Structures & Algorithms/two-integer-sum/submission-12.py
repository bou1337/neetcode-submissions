class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc = {}
        for  i in range(len(nums)):
            if  target - nums[i]  not  in dc:
                dc[nums[i]] = i
            else:
                return [dc[target - nums[i]],i]
        return []
        
                