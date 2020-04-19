class Solution:
    @staticmethod
    def exist(board: list, word: str) -> bool:

        def is_str_present(i, j, char):

            if char == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) :
                return False

            if board[i][j] == word[char]:
                temp = board[i][j]
                board[i][j] = '#'
                is_present = is_str_present(i + 1, j, char+1) or is_str_present(i, j + 1, char+1) or is_str_present(i - 1, j, char+1) or is_str_present(i, j - 1, char+1)
                board[i][j] = temp
                return is_present

            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if is_str_present(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    print()
    print(Solution().exist([["A","B","C","E"], ["S","F","E","S"], ["A","D","E","E"]], "ABCESEEEFS"))

