class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        data_in_dict ={}

        for   i  in range(len(nums)):
            if target - nums[i] not in data_in_dict:
                data_in_dict[nums[i]]=i
            else:
                return [data_in_dict[target - nums[i]],i]
    
