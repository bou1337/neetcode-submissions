class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        size = len(nums)
        if size<3:
            return nums
        for i in nums:
            c = 0
            while   i  in nums:
                c +=1
                nums.remove(i)
            if c >size/3:
                result.append(i)
        return result 