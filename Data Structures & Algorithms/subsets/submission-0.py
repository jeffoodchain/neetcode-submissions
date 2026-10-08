class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # with nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # without nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
# input:  [1]
# output: [[], [1]] 
# input:  [1, 2]
# output: [[], [1], [2], [1, 2]] C22 + C21 + C20

# input:  [1, 2, 3]
# output: [ [], 
#           [1], [2], [3], 
#           [1, 2], [1, 3], [2, 3]
#           [1, 2, 3] ]