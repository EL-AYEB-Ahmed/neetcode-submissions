class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def place(l,index):
            aux = l[index]
            i=index
            for i in range(index,len(l)-1):
                    l[i]=l[i+1]
            l[-1] = aux
            return None
        k=0

        n = len(nums)
        i = 0
        while (i<n-1):
            if (nums[i] == nums[i+1]):
                place(nums,i)
                n-=1
                k+=1
            else:
                i+=1
        return len(nums) - k