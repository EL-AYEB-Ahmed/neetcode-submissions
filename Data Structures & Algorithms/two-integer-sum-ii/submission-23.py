class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while not(numbers[i]+numbers[j] == target):
            if (numbers[i]+numbers[j] > target) :
                j-=1                
            elif (numbers[i]+numbers[j] < target):
                i+=1
        return [i+1,j+1]
"""        d={}
        for i in range(len(numbers)):
            d[target - numbers[i]] = i
        for i in range(len(numbers)):
            if( numbers[i] in d.keys()):
                return [i+1,d[numbers[i]]+1]
            """