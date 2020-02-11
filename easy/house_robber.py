class Solution:
    @staticmethod
    def rob(nums: list) -> int:
        curr_max = prev_max = 0
        for i, num in enumerate(nums):
            temp = curr_max
            curr_max = max(prev_max + num, curr_max)
            prev_max = temp
        return curr_max


if __name__ == '__main__':
    print(Solution().rob([2, 1, -1, 1, 3, 4]))
