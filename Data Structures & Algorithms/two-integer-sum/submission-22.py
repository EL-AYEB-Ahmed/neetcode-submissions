class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if (target -nums[i]) in nums:
                d[(nums[i],i)] =[target -nums[i], nums.index(target -nums[i])]
            else : 
                 d[(nums[i],i)] =[target -nums[i], -1]
        for k in d:
            if d[k][1] != -1 and k[1] != d[k][1]:
                return sorted([k[1] , d[k][1]])