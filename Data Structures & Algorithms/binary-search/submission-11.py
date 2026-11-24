class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n -1
        while ( i <= j ):
            if nums[(i+j) //2] < target: 
                i =( i+j )//2 +1
            elif nums[(i+j) //2] > target:
                j =( i+j )//2 -1
            else:
                return (i+j)//2
        return -1