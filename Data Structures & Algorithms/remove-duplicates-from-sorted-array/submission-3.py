class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        res = []
        for n in nums:
            if n not in unique:
                unique.add(n)
                res.append(n)
        cnt = len(res)
        print(res)
        res.sort()
        print(res)
        for i, num in enumerate(nums):
            if i < cnt:
                nums[i] = res[i]
            else:
                nums[i] = 0
        return cnt
