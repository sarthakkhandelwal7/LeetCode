class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        left = 0
        temp_sum = 0
        ans = float('inf')
        for i, num in enumerate(nums):
            temp_sum += num
            while temp_sum >= s:
                ans = min(ans, i+1-left)
                temp_sum -= nums[left]
                left += 1
        return ans if ans < float('inf') else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(11, [1,2,3,4,5]))
