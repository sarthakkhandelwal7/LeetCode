class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return res
        r, c = len(matrix), len(matrix[0])
        res = []
        row, column = 0, 0
        # direction 1 for up
        # 0 for down
        direction = 1
        while row < r and column < c:
            res.append(matrix[row][column])

            new_row = row + (-1 if direction else 1)
            new_column = column + (1 if direction else -1)

            if new_column < 0 or new_column == c or new_row < 0 or new_row == r:
                if direction:
                    row += (column == c-1)
                    column += (column < c-1)

                else:
                    column += (row == r - 1)
                    row += (row < r-1)


                direction = 1 - direction

            else:
                row = new_row
                column = new_column
        return res


if __name__ == '__main__':
    print(Solution().findDiagonalOrder([[1, 2, 3],[4, 5, 6], [7, 8, 9 ]]))
    print(Solution().findDiagonalOrder([[1,2],[4,5],[7,8],[13,14]]))