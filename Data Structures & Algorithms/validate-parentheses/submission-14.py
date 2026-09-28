class Solution:
    def isValid(self, s: str) -> bool:
        #I am using a stack as a datastructure LIFO
        stack=[]
        opened="({["
        closed=")}]"
        stop=False
        i=0
        n=len(s)
        while i<n and not(stop):
            e=s[i]
            if e in opened:
                stack.append(e)
            else:
                index=closed.index(e)
                if stack==[]:
                    stop = True
                elif stack[-1]==opened[index]:
                    stack.pop()
                else:
                    stop=True
            i+=1
        return stack==[] and (not(stop))
                    


