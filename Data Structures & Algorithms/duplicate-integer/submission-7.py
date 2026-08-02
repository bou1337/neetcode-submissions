class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data  =set()
        for i in nums:
            data.add(i)
        return len(data) != len(nums)
    