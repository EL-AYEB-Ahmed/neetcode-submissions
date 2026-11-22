class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        k=1
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if (nums[i]+1 == nums[i+1]):
                k+=1
            elif not(nums[i] == nums[i+1]):
                if (k>res):
                    res=k
                k=1
        res = max(res, k)

        return res