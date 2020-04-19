from random import randint


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return self.quick_select(nums, len(nums) - k, 0, len(nums)-1)

    @staticmethod
    def partition(nums, left, right, pivot_index) -> int:
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        i = left-1
        for j in range(left, right):
            if nums[j] < pivot:

                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[right], nums[i] = nums[i], nums[right]
        return i

    def quick_select(self, nums, k_smallest, left, right):

        if left == right:
            return nums[left]

        pivot_index = randint(left, right)
        pivot_index = self.partition(nums, left, right, pivot_index)

        if pivot_index == k_smallest:
            return nums[pivot_index]

        elif pivot_index < k_smallest:
            return self.quick_select(nums, k_smallest, pivot_index+1, right)

        else:
            return self.quick_select(nums, k_smallest, left, pivot_index-1)


if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))