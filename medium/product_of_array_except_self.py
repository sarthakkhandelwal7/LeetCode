class Solution:
    def productExceptSelf(self, nums):
        ans = [0] * len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        right = 1
        for i in range(len(nums)):
            ans[len(nums) - 1 - i] = ans[len(nums) - 1 - i] * right
            right *= nums[len(nums) - 1 - i]
        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))