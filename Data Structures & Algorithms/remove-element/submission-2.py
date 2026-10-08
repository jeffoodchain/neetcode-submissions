class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        cnt = 0
        for n in nums:
            if n is not val:
                res.append(n)
                cnt += 1

        for i, n in enumerate(res):
            nums[i] = res[i]
        return cnt