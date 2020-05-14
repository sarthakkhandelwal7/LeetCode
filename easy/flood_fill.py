class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def fill(old, x, y):
            if not (0 <= x < len(image) and 0 <= y < len(image[0])) or image[x][y] != old or image[x][y] == newColor:
                return

            else:
                image[x][y] = newColor

            for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                fill(old, x + i, y + j)

        fill(image[sr][sc], sr, sc)
        return image
