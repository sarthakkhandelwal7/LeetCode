class Solution:
    def findCircleNum(self, matrix) -> int:

        def dfs(visited, i):
            for j in range(len(matrix)):
                if not visited[j] and matrix[i][j]:
                    visited[j] = True
                    dfs(visited, j)

        count = 0
        visited = [False]*len(matrix)
        for i in range(len(matrix)):
            if not visited[i]:
                dfs(visited, i)
                count += 1

        return count


if __name__ == '__main__':
    print(Solution().findCircleNum([[1,1,0],
 [1,1,1],
 [0,1,1]]))