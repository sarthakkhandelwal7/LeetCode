class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]

        left = nums[0]
        ans = list()

        for i, previous in enumerate(nums, 1):
            if i == len(nums) or previous + 1 < nums[i]:
                if left == previous:
                    ans.append(str(previous))

                else:
                    ans.append(str(left)+'->'+str(previous))
                left = nums[i] if i != len(nums) else None

        return ans


if __name__ == '__main__':
    print(Solution().summaryRanges([0,1,2,4,5,7]))
    print(Solution().summaryRanges([0,2,3,4,6,8,9]))
    print(Solution().summaryRanges([1, 3,5,6,7,9]))
    print(Solution().summaryRanges([1,3]))