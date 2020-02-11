class Solution:
    @staticmethod
    def get_next(n: int) -> int:
        total = 0
        while n:
            n, temp = divmod(n, 10)
            total += temp ** 2
        return total

    def isHappy(self, n: int) -> bool:
        hash_table = set()
        while n != 1:
            if n in hash_table:
                return False

            hash_table.add(n)
            n = Solution().get_next(n)
        return True


if __name__ == '__main__':
    print(Solution().isHappy(7))