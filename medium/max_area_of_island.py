class Solution:

    def maxAreaOfIsland(self, grid)
        max_area = 0

        def find_area(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]):
                return 0
            grid[i][j] = 0
            return 1 + find_area(i + 1, j) + find_area(i, j + 1) + find_area(i - 1, j) + find_area(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = find_area(i, j)
                    max_area = max(area, max_area)

        return max_area