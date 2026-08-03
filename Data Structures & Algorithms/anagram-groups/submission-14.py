class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result ={} 
        last_result=[]
        for i  in strs:
            count =[0]*26 ;
            for  j in range(len(i)):
                count[ord(i[j])-ord('a')] +=1
            tpl = tuple(count) 
            if tpl  not in result : 
                result[tpl]=[] 
            result[tpl].append(i)
        for _ , value  in result.items():
            last_result.append(value)
        return last_result 