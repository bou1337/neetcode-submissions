class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rlt=strs[0]
        for i in strs:
            j = 0 
            while(j<len(i)and  j<len(rlt) and i[j]==rlt[j]):
                j +=1 
            rlt =rlt[0:j]
        return rlt 