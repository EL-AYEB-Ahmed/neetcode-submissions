class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid # Target found
            elif arr[mid] < target:
                left = mid + 1 # Search right half
            else:
                right = mid - 1 # Search left half

        return -1 # Target not found