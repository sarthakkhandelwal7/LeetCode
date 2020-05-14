class Solution:
    def updateBoard(self, board, click):
        moves = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]

        def helper(x, y):
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return
            mines_count = 0
            for i, j in moves:
                mines_count += self.check_adjacents(board, x + i, y + j)

            if not mines_count:
                board[x][y] = 'B'
                for i, j in moves:
                    p = x + i
                    q = y + j
                    if 0 <= p < len(board) and 0 <= q < len(board[0]) and board[p][q] != 'B':
                        helper(x + i, y + j)

            else:
                board[x][y] = str(mines_count)

        helper(click[0], click[1])
        return board

    @staticmethod
    def check_adjacents(board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'M':
            return 1

        else:
            return 0
