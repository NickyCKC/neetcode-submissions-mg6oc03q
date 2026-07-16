class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        use dict
        key: value == number: number+1
        loop thru list 
        check if number in dict
        if not, add number to dict and its number+1 as value
        if yes, continue

        """
        dicti = defaultdict(int)
        res = 0

        for num in nums:
            if not dicti[num]:
                dicti[num] = dicti[num-1] + 1 + dicti[num+1]
                dicti[num - dicti[num-1]] = dicti[num]
                dicti[num + dicti[num+1]] = dicti[num]
                res = max(res, dicti[num])
        return res
