class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        data = set()
        max_len =1
        if(nums==[]):
            return 0 
        for  i in nums:
            if i  not  in data:
                data.add(i)
        
        for  i in data:
            
            if i-1 not    in data:
                j = i
                k=1
                while(j +1 in data):
                    k+=1 
                    j+=1
                if(k>max_len):
                    max_len =  k
        
        return  max_len 
            
            
