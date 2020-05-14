class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 1 or not coordinates:
            return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # y = mx+c
        m = float('inf') if x2 - x1 == 0 else (y2 - y1) / (x2 - x1)
        c = x1 if m == float('inf') else y1 - m * x1
        are_in_line = True
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if not self.is_on_line(x, y, m, c):
                are_in_line = False
                break

        return are_in_line

    def is_on_line(self, x, y, m, c):
        if m == float('inf'):
            return c == x

        else:
            return y == m * x + c
