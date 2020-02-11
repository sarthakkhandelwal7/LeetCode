class Solution:
    @staticmethod
    def moveZeroes(nums: list) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = None
        for i, num in enumerate(nums):
            if num == 0:
                right = i
                if left is None:
                    left = i

            elif right is not None:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                right = i
        return nums


if __name__ == '__main__':
    print(Solution().moveZeroes([0, 0, 1]))
