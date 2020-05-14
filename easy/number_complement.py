class Solution:
    def findComplement(self, num: int) -> int:
        bitmask = num
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        return bitmask ^ num


if __name__ == '__main__':
    print(Solution().findComplement(5))