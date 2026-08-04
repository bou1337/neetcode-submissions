class Solution:
    def sortColors(self, nums: List[int]) -> None:

        count =  defaultdict(int)
        for  i  in  nums: 
            count[i] +=1
        c = 0
        for  i in range(3):
            j = 0
            while j<count[i] :
                nums[c] = i
                c +=1
                j +=1
        
        
            