class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        stop=False
        n=len(nums)
        while i<n-1 and not(stop):
            j=i+1
            while j<n and not(stop):
                if nums[i]+nums[j]==target:
                    stop=True
                j+=1
            i+=1
        return([i-1,j-1])