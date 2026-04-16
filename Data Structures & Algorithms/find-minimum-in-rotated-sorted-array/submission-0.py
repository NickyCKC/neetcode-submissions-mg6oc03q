class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        return nums[0]
        