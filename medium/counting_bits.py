class Solution:
    def countBits(self, num: int) -> list:
        counts = [0]
        for i in range(1, num + 1):
            j = i & 1
            counts.append((counts[i >> 1]) + j)
        return counts


if __name__ == '__main__':
    print(Solution().countBits(8))