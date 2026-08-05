class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        arr1 = [1]*len(nums)
        arr2 = [1]*len(nums)
        p = 1
        for i in range(len(nums)-1):
            p *= nums[i]
            arr1[i+1]=p
        j = len(nums) -2 
        p =1
        while(j!=-1):
            p *=nums[j+1]
            arr2[j] = p 
            j -=1
        result =[]
        for  i in range(len(nums)):
            result.append(arr1[i]*arr2[i])
        return result   

