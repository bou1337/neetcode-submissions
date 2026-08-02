class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic ={}
        for  word in strs:

            c=[0]*26
            for i in word:
                c[ord(i)-ord('a')]+=1
            if tuple(c)  in dic:
                dic[tuple(c)].append(word)
            else:
                dic[tuple(c)]=[]
                dic[tuple(c)].append(word)
        
        return list(dic.values())
        

