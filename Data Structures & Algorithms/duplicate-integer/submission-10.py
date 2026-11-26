class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = set()
        for e in nums:
            r.add(e)
        return len(r) != len(nums)