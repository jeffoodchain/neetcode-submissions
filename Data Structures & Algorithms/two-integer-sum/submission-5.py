class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we store the mapping (target - n) : index in the dict
        s = {}
        for i, n in enumerate(nums):
            # print(f"i: {i}, n: {n}")
            # print(s)
            if target - n in s:
                return [s[target - n], i]
            s[n] = i