class Solution:
    def reverseBits(self, n: int) -> int:
        res = [0] * 32
        total = 0
        for i in range(32):
            remainder = n % 2
            n /= 2
            if remainder:
                res[i] = 1
                n -= 0.5
        for i in range(31, -1, -1):
            total += res[i] * 2**(31-i)
        return total
