class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result ={}
        re =[]

        for i  in strs:

            s = "".join(sorted(i))

            if s not  in  result:
                result[s]=[]
                result[s].append(i)
            else:
                result[s].append(i)
        
        for  i in result:
            re.append(result[i])
        return re 