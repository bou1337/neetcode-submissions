
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        data= defaultdict(int)
        result =[]     
        for  i in nums:
            data[i] +=1
        for  key, value  in data.items():
            if value >len(nums)//3:
                result.append(key)
        
        return result 
