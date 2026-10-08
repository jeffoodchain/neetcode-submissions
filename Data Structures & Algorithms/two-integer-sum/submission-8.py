class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we store the mapping n : index in the dict
        # s = {}
        # for i, n in enumerate(nums):
        #     # print(f"i: {i}, n: {n}")
        #     # print(s)
        #     if target - n in s:
        #         return [s[target - n], i]
        #     s[n] = i

        # brute force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
