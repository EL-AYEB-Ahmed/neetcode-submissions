class Solution:

    def encode(self, strs: List[str]) -> str:
        ret=""
        return ''.join(str(len(e)) + "#" + e for e in strs)
    def decode(self, s: str) -> List[str]:
        r=[]
        i=0
        n=len(s)
        while i < n:
            if s[i] in"1234567890":      
                num=s[i]
                i+=1
                while not(s[i]=="#") and s[i] in "1234567890":
                    num+= s[i]
                    i+=1
                num=int(num)
                i+=1
                r.append(s[i:i+num])
                i+=num
        return r
            
                    