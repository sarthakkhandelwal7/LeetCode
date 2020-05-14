class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        right_good = n - 1
        for i in range(n - 2, -1, -1):
            right_good = i if i + nums[i] >= right_good else right_good

        return right_good == 0
