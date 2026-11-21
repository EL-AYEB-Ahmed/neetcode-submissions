class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l= sorted(nums1[:m] + nums2)
        i=0
        while (i<n+m):
            nums1[i] = l[i]
            i+=1
