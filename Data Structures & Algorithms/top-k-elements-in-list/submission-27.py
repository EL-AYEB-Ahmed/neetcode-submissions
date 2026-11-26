class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for e in nums:
            if e in d:
                d[e]+=1
            else:
                d[e] =1
        l=sorted(d.values(),reverse=True)
        res=[]
        for i in range(k):
            for k in d.keys():
                if d[k] == l[i] and( k not in res):
                    res.append(k)
                    
        return res
