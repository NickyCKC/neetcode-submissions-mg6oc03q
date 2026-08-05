class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, current, total):
            if total == target:
                res.append(current.copy())
                return
            if index >= len(nums) or total > target:
                return

            current.append(nums[index])
            dfs(index, current, total + nums[index])
            current.pop()
            dfs(index + 1, current, total)

        dfs(0, [], 0)
        return res