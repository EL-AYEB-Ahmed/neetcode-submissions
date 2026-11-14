class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            d[target - numbers[i]] = i
        for i in range(len(numbers)):
            if( numbers[i] in d.keys()):
                return [i+1,d[numbers[i]]+1]

            