class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        result=[]
        for i  in  strs:
            srt = "".join(sorted(i))
            if srt not in dic :
                dic[srt]=[] 
            dic[srt].append(i) 
        for _ ,value  in dic.items():
            result.append(value)
        
        return result 
