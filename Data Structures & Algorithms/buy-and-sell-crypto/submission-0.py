class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        point1 = 0
        point2 = 1
        max = 0
        while point1 < len(prices) - 1:
            profit = prices[point2] - prices[point1]
            #print(profit)
            if profit > max:
                max = profit
            if point2 == len(prices) - 1:
                point1 += 1
                point2 = point1 + 1
            else:
                point2 += 1
        return max

        