class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        """def anagram(a,b):
            if signature(a)==signature(b):
                return True, signature(a)
            return False,None"""
        def signature(a):
            n=len(a)
            sign=[0]*26
            for i in a:
                sign[ord(i)-ord('a')]+=1
            return tuple(sign)
        n=len(strs)
        if n<=1:
            return [strs]
        i=0
        dr={}
        for i in range(n):
            sign=signature(strs[i])
            if sign in dr.keys():
                dr[sign].append(strs[i])
            else:
                dr[sign]=[strs[i]]
        r=list(dr.values())
        return r

            #solution plus longue
"""
        def anagram(a,b):
            n=len(a)
            if not(set(a)==set(b)):
                return False
            else:
                da={}
                db={}
                for i in range(len(a)):
                    if da.get(a[i], "Key not found")=="Key not found":
                        da[a[i]]=1
                    else:
                        da[a[i]]+=1
                    if db.get(b[i],"Key not found")=="Key not found":
                        db[b[i]]=1
                    else:
                        db[b[i]]+=1
                return da == db
        n=len(strs)
        if n<=1:
            return [strs]
        i=0
        l=0
        r=[]
        while i<n-1:
            j=i+1
            new=True
            while j<n:
                if anagram(strs[i],strs[j]):
                    if new:
                        r.append([strs[i],strs[j]])
                        new=False
                    else:
                        r[-1].append(strs[j])
                    strs=strs[:j]+strs[j+1:]
                    n-=1
                    j-=1
                j+=1
            if new==False:
                strs=strs[:i]+strs[i+1:]
                i-=1
                n-=1
            i+=1
        if not(strs==[]):
            for e in strs:
                r+=[[e]]
        return r"""










