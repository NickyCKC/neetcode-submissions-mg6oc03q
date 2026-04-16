class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        while r - l > 1:
            print(f"Left = {l, nums[l]}, Right = {r, nums[r]}")
            mid = (r + l) // 2
            if nums[l] > nums[r] and nums[r] < nums[mid]:
                l = mid
            elif nums[l] > nums[r] and nums[r] > nums[mid]:
                r = mid
            elif nums[r] > nums[l]:
                return nums[l]


        return min(nums[l], nums[r])
        