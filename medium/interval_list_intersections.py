class Solution:
    @staticmethod
    def intervalIntersection(a, b):
        if not a or not b:
            return []
        ans = []
        i = j = 0
        while i < len(a) and j < len(b):
            low = max(a[i][0], b[j][0])
            high = min(a[i][1], b[j][1])

            if low < high:
                ans.append([low, high])

            if a[i][1] < b[j][1]:
                i += 1

            else:
                j += 1

        return ans
