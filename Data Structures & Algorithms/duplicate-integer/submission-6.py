class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for n in nums:
            h[n] = 0
        for n in nums:
            h[n] += 1
            if h[n] > 1:
                return True
        return False