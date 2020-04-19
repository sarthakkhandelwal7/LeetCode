class Solution:
    def searchMatrix(self, matrix, target):
        i, j = len(matrix)-1, 0
        switch = 1
        while True:
            try:
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    i -= 1
                else:
                    j += 1
            except:
                return False


if __name__ == '__main__':
    print(Solution().searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5))
    print(Solution().searchMatrix([[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]],13))