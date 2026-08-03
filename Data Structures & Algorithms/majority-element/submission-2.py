class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d =  defaultdict(int)

        for i  in  nums :
            d[i] +=1
        
        for key  , value  in d.items():
            if(value>len(nums)/2):
                return key 

        
        