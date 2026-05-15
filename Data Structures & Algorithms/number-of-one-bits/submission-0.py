class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            remainder = n % 2
            n /= 2
            if remainder == 1:
                count += 1
                n -= 0.5
            
            print(remainder, n, count)
        return count