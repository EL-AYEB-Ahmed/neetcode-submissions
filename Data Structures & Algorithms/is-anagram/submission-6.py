class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ds={}
        dt={}
        for i in range(len(s)):
            if ds.get(s[i], "Key not found")=="Key not found":
                ds[s[i]]=1
            else:
                ds[s[i]]+=1
            if dt.get(t[i], "Key not found")=="Key not found":
                dt[t[i]]=1
            else:
                dt[t[i]]+=1
        return ds==dt
        