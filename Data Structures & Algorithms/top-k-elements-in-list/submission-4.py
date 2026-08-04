class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        for i in nums: 
            count[i] +=1
        
        result =[]
        for key , value  in count.items():
            result.append([value , key])
        result.sort()
        data =[]

        while(k):
            data.append(result.pop()[1]) 
            k -=1
        return data 
    