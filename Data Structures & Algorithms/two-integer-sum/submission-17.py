class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        rsl = []
        for i  in range(len(nums)):
            if  nums[i] in dct:
                rsl.extend([dct[nums[i]] ,i])
                break
            dct[target-nums[i]] = i
        return rsl