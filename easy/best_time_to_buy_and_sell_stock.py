class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = None
        biggest_profit = 0
        for i in prices:
            if temp is None:
                temp = i

            elif i < temp:
                temp = i

            else:
                if biggest_profit < i-temp:
                    biggest_profit = i - temp
        return biggest_profit
