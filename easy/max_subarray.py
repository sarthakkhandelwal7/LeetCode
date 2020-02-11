class Solution:
    @staticmethod
    def max_sub_array(nums: list) -> int:
        temp_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            temp_sum = max(temp_sum + nums[i], nums[i])
            max_sum = max(temp_sum, max_sum)
        return max_sum


if __name__ == '__main__':
    print(Solution().max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
