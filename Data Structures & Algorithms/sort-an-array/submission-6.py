class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums)<=1):
            return nums
        mid = len(nums)//2
        right = nums[:mid]
        left  = nums[mid:]
        right = self.sortArray(right)
        left = self.sortArray(left)
        merged = []
        i = j = 0
        while i<len(right) and j<len(left):
            if(right[i]<left[j]):
                merged.append(right[i])
                i +=1 
            else : 
                merged.append(left[j])
                j+=1
        merged.extend(right[i:])
        merged.extend(left[j:])
        return merged
     
