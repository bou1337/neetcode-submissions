class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l1=[1]*len(nums)
        l2=[1]*len(nums)
        result =[]
        for  i in range(len(nums)):
            if i>0:
                l1[i]=nums[i-1]*l1[i-1]
        
        for j  in  range(len(nums)-1,-1,-1):
            if(j<len(nums)-1):
                l2[j]=l2[j+1]*nums[j+1]
        
        for  i in   range(len(nums)):

            result.append(l1[i]*l2[i])
        
        return result 