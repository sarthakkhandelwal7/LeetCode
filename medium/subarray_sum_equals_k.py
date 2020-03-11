from collections import Counter


class Solution:
    def subarraySum(self, nums, k):
        count = Counter()
        sum = 0
        count[0] = 1
        ans = 0
        for num in nums:
            sum += num
            ans += count[sum - k]
            count[sum] += 1
        return ans


if __name__ == '__main__':
    # print(Solution().subarraySum([1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2], 42))
    # print(Solution().subarraySum([1, 1, 1, 1, 1], 2))
    print(Solution().subarraySum([1, 6, 1, 2, 3, 2, 1, 7, 4, 3], 7))