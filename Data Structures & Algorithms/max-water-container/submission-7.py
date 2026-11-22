class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        n=len(heights)
        j=n-1
        m=min(heights[i],heights[j]) * (j-i)
        while (i<j):
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
            m=max(m,min(heights[i],heights[j]) * (j-i))
        return m