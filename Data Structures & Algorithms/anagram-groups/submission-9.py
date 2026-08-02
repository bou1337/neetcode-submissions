class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}
        rsl = []
        for  i in strs:
            srt = "".join(sorted(i))
            if srt  not  in dic:
                dic[srt]=[]
            dic[srt].append(i)
        for v in dic.values():
            rsl.append(v)
        
        return rsl 
