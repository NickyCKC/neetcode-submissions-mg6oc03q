class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = -1
        point1 = 0
        point2 = len(heights) - 1
        while point1 != point2:
            
            
            if heights[point1] > heights[point2]:
                size = heights[point2] * (point2 - point1)
                point2 -= 1
            else:
                size = heights[point1] * (point2 - point1)
                point1 += 1
            if size > maxi:
                maxi = size
        return maxi
        