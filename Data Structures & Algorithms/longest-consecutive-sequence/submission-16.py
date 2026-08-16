class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
      
        Long=0
        data = set(nums)

        for  i in nums:
            if i -1 not  in data:
                c = 0
                j  = i
                while j  in data:
                    c += 1
                    j += 1
                Long = max(Long , c)
        
        return Long