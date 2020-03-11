class Solution:
    def maxProfit(self, prices: list) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


if __name__ == '__main__':
    print(Solution().maxProfit([7, 3, 2, 4, 6, 12, 7, 13, 1, 3]))