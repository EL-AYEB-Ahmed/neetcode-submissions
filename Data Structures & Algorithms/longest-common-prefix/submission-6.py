class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def et (s1:str , s2:str) -> str : 
            r=""
            i = 0
            while (i < min(len(s1),len(s2))):
                if (s1[i]==s2[i]):
                    r+=s1[i]
                    i+=1
                else:
                    return r
            return r

        res=strs[-1]
        for i in range(len(strs)-1):
            res= et(res,strs[i])
        return res