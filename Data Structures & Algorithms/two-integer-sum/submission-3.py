class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort() # this sorting is nlogn?

        left, right = 0, len(nums) - 1
        while left < right:
            curr_val = A[left][0] + A[right][0]
            if curr_val == target:
                return [min(A[left][1], A[right][1]), max(A[left][1], A[right][1])]
            elif curr_val > target:
                right -= 1 
            elif curr_val < target:
                left += 1
        return []