class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        currRes = []

        def dfs(i, target, currRes):
            target -= nums[i]
            currRes.append(nums[i])
            print(currRes)

            if target < 0:
                target += currRes.pop()
                return
            elif target == 0:
                print(f"BANG!: {currRes}")
                res.append(currRes.copy())
                currRes.pop()
                return

            for j in range(i, len(nums)):
                dfs(j, target, currRes)
            target += currRes.pop()

        for i in range(len(nums)):
            print(f"{i}th iteration: ")
            curr = []
            dfs(i, target, curr)
        for k in range(2,3):
            print(k)
        return res

# [2,5,6,9] t=9

# [3,4,5] t=16