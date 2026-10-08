class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        if target > matrix[h-1][w-1] or target < matrix[0][0]:
            return False

        l, r = 0, h

        while l != r:
            print(l, r)
            mid = (l+r) // 2
            print("mid, ", mid)
            if target > matrix[mid][0]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid
            elif target == matrix[mid][0]:
                return True
            print(l, r)
            print("=============")
        l -= 1

        if self.binarySearch(matrix[l], target) != -1:
            return True
        else: 
            return False

    def binarySearch(self, arr: List[int], target):
        l, r = 0, len(arr)
        while l != r:
            mid = (l + r) // 2
            if target > arr[mid]:
                l = mid+1
            elif target < arr[mid]:
                r = mid
            else:
                return mid
        return -1