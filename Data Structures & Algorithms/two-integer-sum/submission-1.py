class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            j = i + 1
            while (j < len(nums)):
                result = nums[i] + nums[j]
                #print(i, nums[i], j, nums[j], result)
                if result == target:
                    answer.append(i)
                    answer.append(j)
                j = j + 1
        return answer
                
