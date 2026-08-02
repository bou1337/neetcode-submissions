class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        dic  ={}
        for i in nums:
            if i not  in dic:
                dic[i]=0
            dic[i] +=1
        
        freq=[[] for  _ in range(len(nums)+1)]

        for i in dic:
            freq[dic[i]].append(i)
        
        for  i in   range(len(freq)-1 ,0,-1):
            
            for  j in  freq[i]:
                result.append(j)
            if(len(result)==k):
                return result 
        
        return result 