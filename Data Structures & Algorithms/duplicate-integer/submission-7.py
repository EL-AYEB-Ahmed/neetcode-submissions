class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """n=len(nums)
        i=0
        stop = False
        while i<n-1 and not(stop):
            j=i+1
            while j<n and not(stop):
                if nums[i]==nums[j]:
                    stop=True
                else:
                    j+=1
            i+=1

        return stop """
        seen=set()
        i=0
        stop=False
        while i<len(nums) and not(stop):
            if nums[i] in seen:
                stop=True
            else:
                seen.add(nums[i])
                i+=1
        return stop
                




        