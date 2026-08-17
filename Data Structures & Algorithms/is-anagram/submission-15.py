class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        data1 = [0]*26
        data2 =[0]*26
        for i in s:
            data1[ord(i)-ord('a')] +=1
        for i in t:
            data2[ord(i)-ord('a')] +=1
        return data2==data1
        