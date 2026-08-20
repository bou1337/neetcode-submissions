class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i  = 0 
        j = 0
        while i<len(arr) :
            Max = 0
            j=i 
            while j < len(arr) -1:
                if arr[j+1] > Max:
                    Max =  arr [j+1]
                j +=1 
            arr[i] = Max
            i  +=1
        if i>0:
            arr[i-1]  = -1
        return arr 
