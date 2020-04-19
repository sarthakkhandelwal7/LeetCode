class Solution:
    def threeSum(self, nums):

        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if num >= 0:
                break
            if i>0 and num == nums[i-1]:
                continue
            # Left goes form left to right
            # Right goes from right to left
            left = i+1
            right = len(nums) - 1

            while left < right:
                print(f'left: {left}\tright: {right}')
                total = nums[left] + nums[right] + num
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))