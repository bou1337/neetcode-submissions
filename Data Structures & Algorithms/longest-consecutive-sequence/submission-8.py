class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

         data_in_set=set()
         max_con=1
         
         if(nums==[]):
            return 0

         for  i in nums:
            data_in_set.add(i)
        
         for  i   in data_in_set:
            tmp = 1
            if i-1 not  in  data_in_set:
                while(i+1 in data_in_set):
                    tmp += 1
                    i += 1
            
            if(tmp>max_con):
                max_con=tmp
        
         return  max_con

         
        
