class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            while i:
                remainder = i % 2
                i /= 2
                if remainder:
                    i -= 0.5
                    count += 1
            res.append(count)
        return res