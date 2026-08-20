class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r = len(arr) - 1
        max_thusfar = float('-inf')

        while r >= 0:
            if arr[r] > max_thusfar: 
                temp_max_thusfar = arr[r]

            arr[r] = max_thusfar

            max_thusfar = temp_max_thusfar

            r-=1
        
        arr[len(arr) - 1] = -1

        return arr