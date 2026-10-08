class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        l, r = 0, len(nums)
        while l != r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid
            else:
                return mid
        return -1