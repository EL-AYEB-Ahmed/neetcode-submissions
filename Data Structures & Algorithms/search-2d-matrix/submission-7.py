class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        n = len(matrix)
        m = len(matrix[0])
        j = n*m-1
        while ( i<=j):
            mid = (i+j) // 2
            im = (mid) // m
            jm = mid % m
            # 11 = (2 ,3) 11//4 = 2 et 11%4 = 3
            if (matrix[im][jm] < target):
                i=mid +1
            elif (matrix[im][jm] > target):
                j=mid -1
            else :
                return True
        return False
            