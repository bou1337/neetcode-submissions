class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        data_in_set =  set(nums)

        return len(data_in_set)!=len(nums)
        