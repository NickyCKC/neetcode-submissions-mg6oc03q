class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i, value in enumerate(nums):
            if value in seen:
                return True
            else:
                seen[value] = i
        return False
        