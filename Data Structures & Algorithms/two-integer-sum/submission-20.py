class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        result = []

        for i  in range(len(nums)):
            
            if target - nums[i] not in dic : 
                dic[nums[i]]= i
            else:
                result.extend([dic[target - nums[i]],i])
        return result 
            