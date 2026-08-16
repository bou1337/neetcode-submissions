class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
      
        Long=0
        data = set(nums)

        for  i in nums:
            j = i
            c = 0
            while j in data:
                j -= 1
            j +=1
            while j in data:
                data.remove(j) 
                j += 1 
                c += 1
            if c>Long:
                Long = c
        return Long