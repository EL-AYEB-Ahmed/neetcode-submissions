class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_return={}
        for i in range(len(nums)):
            if nums[i] in dict_return.keys():
                dict_return[nums[i]]+=1
            else:
                dict_return[nums[i]]=1
        i=0
        maxi=max(dict_return.values())
        j=maxi
        output=[]
        while i<k:
            new=True
            nothing = True 
            for key , value in dict_return.items():
                if value == j:
                    output.append(key)
                    new=False
                    i+=1
                    nothing=False
            if not new or nothing:
                j-=1
        return output

            
    #solution lente
        """output=[]
        items=list(dict_return.items())
        def sort_algo_key_value(items):
            stop=False
            i=0
            n=len(items)
            while i < n-1:
                for j in range(i+1,n):
                    if items[i][1]< items[j][1]:
                        aux = items[i]
                        items[i] = items[j]
                        items[j]=aux
                i+=1
            return items
        items=sort_algo_key_value(items)
        for i in range(k):
            output.append(items[i][0])
        return output"""