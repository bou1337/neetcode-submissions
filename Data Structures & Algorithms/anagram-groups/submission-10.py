class Solution:
    def vec(self,s):
        lst = [0]*26
        for  i in s:
            lst[ord(i)-ord('a')] +=1
        return lst
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}
        rsl = []
        for  i in strs:
            vl = tuple(self.vec(i))
            if vl not in dic:
                dic[vl] = []
            dic[vl].append(i)
        for j in dic.values():
            rsl.append(j)
        return rsl 
