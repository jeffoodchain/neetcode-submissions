class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        last = 0
        for ele in nums:
            if ele == last:
                return True
            last = ele
        return False            