class Solution:
    @staticmethod
    def numIslands(grid) -> int:
        def utility(grid, marker, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not marker[i][j] and int(grid[i][j]):
                marker[i][j] = True
                utility(grid, marker, i, j+1)
                utility(grid, marker, i + 1, j)
                utility(grid, marker, i, j-1)
                utility(grid, marker, i - 1, j)
        marker = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j]) and not marker[i][j]:
                    utility(grid, marker, i, j)
                    count += 1

        return count


if __name__ == '__main__':
    print(Solution().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
