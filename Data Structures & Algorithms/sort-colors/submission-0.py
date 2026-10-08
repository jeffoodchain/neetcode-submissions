class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1
        
        idx = 0
        for x in range(len(count)):
            length = count[x]
            for i in range(length):
                nums[idx] = x
                idx += 1
        