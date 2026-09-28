class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=[]
        for e in s: 
            if (ord("a")<=ord(e)<=ord("z")) or(ord("0")<=ord(e)<=ord("9")):
                news.append(e)
            elif (ord("A")<=ord(e)<=ord("Z")):
                news.append(chr(ord(e)+32))
        return news==news[::-1]
        