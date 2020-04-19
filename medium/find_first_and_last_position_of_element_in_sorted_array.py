from bisect import bisect_left, bisect_right


class Solution:

    def searchRange(self, nums, target: int):
        ans = list()
        ans.append(bisect_left(nums, target))
        ending = bisect_right(nums, target)
        ans.append(ending if ending == ans[0] else ending - 1)
        if not nums or len(nums) == ans[0] or ans[0] == ans[1] and nums[ans[0]] != target:
            ans[0], ans[1] = -1, -1

        return ans

if __name__ == '__main__':
    print(f'0 {Solution().searchRange([2, 2], 3)}\n')
    print(f'1 {Solution().searchRange([], 0)}\n')
    print(f'2 {Solution().searchRange([], 1)}\n')
    print(f'3 {Solution().searchRange([0], 0)}\n')
    print(f'4 {Solution().searchRange([1], 0)}\n')
    print(f'5 {Solution().searchRange([1], 1)}\n')
    print(f'6 {Solution().searchRange([1], 2)}\n')
    print(f'7 {Solution().searchRange([5, 7, 7, 8, 8, 10], 8)}')