class Solution:
    @staticmethod
    def pivot_index(nums: list) -> int:
        sum_list = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == (sum_list - left_sum - num):
                return i
            left_sum += num
        return -1


if __name__ == '__main__':
    print(Solution().pivot_index([1, 7, 3, 6, 5, 6]))
