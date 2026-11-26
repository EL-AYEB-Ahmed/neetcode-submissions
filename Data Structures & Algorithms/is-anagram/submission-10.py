class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        c={}
        for e in s:
            if e in c:
                c[e]+=1
            else:
                c[e]=1
        for e in t:
            if e in d :
                d[e] +=1
            else:
                d[e]=1
        return d==c