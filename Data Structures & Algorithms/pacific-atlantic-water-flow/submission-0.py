class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_visited = set()
        a_visited = set()
        rows = len(heights)
        cols = len(heights[0])

        

        def dfs(row, col, visited):
            # add border cells
            if (row, col) not in visited:
                visited.add((row, col))

            # check if can flow down
            if row + 1 < rows and heights[row][col] <= heights[row + 1][col] and (row + 1, col) not in visited:
                visited.add((row + 1, col))
                dfs(row + 1, col, visited)
            # check if can flow right
            if col + 1 < cols and heights[row][col] <= heights[row][col + 1] and (row, col + 1) not in visited:
                visited.add((row, col + 1))
                dfs(row, col + 1, visited)
            # check if can flow up
            if row - 1 >= 0 and heights[row][col] <= heights[row - 1][col] and (row - 1, col) not in visited:
                visited.add((row - 1, col))
                dfs(row - 1, col, visited)
            # check if can flow left
            if col - 1 >= 0 and heights[row][col] <= heights[row][col - 1] and (row, col - 1) not in visited:
                visited.add((row, col - 1))
                dfs(row, col - 1, visited)

        for row in range(rows):
            dfs(row, 0, p_visited)
            dfs(row, cols - 1, a_visited)
        for col in range(cols):
            dfs(0, col, p_visited)
            dfs(rows - 1, col, a_visited)

        res = [[row, col] for row, col in (p_visited & a_visited)] 
        return res       