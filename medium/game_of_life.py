class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for neightbour in neighbours:
                    r = i + neightbour[0]
                    c = j + neightbour[1]
                    if r in range(len(board)) and c in range(len(board[0])):
                        if board[r][c] == 1 or board[r][c] == -1:
                            count += 1

                if board[i][j] == 1 or board[i][j] == -1:
                    if count < 2:
                        board[i][j] = -1

                    elif count > 3:
                        board[i][j] = -1

                elif board[i][j] == 0 or board[i][j] == 2:
                    if count == 3:
                        board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0

                elif board[i][j] == 2:
                    board[i][j] = 1


if __name__ == '__main__':
    mat = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
    print(mat)






