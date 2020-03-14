class Solution:
    def coinChange(self, coins, amount: int) -> int:
        level = seen = {0}
        number = 0
        while level:
            if amount in level:
                return number
            level = {i + j for i in level for j in coins if i + j <= amount} - seen
            seen |= level
            number += 1
        return -1


if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([2], 3))