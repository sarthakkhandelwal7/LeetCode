class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        r, c = len(matrix), len(matrix[0])
        ans = []
        first_row = 0
        last_row = r
        first_column = 0
        last_column = c
        while first_row < last_row and first_column < last_column:

            for i in range(first_column, last_column):
                ans.append(matrix[first_row][i])

            first_row += 1

            for i in range(first_row, last_row):
                ans.append(matrix[i][last_column - 1])

            last_column -= 1

            if first_row < last_row:
                for i in range(last_column - 1, first_column - 1, -1):
                    ans.append(matrix[last_row - 1][i])

                last_row -= 1

            if first_column < last_column:
                for i in range(last_row - 1, first_row - 1, -1):
                    ans.append(matrix[i][first_column])

                first_column += 1

        return ans


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]))
    print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))