class Solution:
    def orangesRotting(self, grid) -> int:
        timer = 0
        rotten = {(i, j) for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j] == 2}
        fresh = {(i, j) for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j] == 1}
        while fresh:
            if not rotten:
                return -1
            temp = set()
            for i, j in rotten:

                for nr, nc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (i + nr, j + nc) in fresh:
                        temp.add((i + nr, j + nc))
                rotten = temp
            fresh -= rotten

            timer += 1
        return timer


if __name__ == '__main__':
    print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))