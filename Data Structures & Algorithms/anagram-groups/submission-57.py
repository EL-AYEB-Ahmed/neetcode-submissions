class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            if tuple(sorted(s)) in d:
                d[tuple(sorted(s))].append(s)
            else:
                d[tuple(sorted(s))] = [s]
        return list(d.values())