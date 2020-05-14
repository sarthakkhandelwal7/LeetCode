class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 1:
            return

        zero = curr = 0
        two = len(nums) - 1

        while curr <= two:
            print(nums)
            print(f'curr: {curr}')

            if nums[curr] == 0:
                nums[zero], nums[curr] = nums[curr], nums[zero]
                zero += 1
                curr += 1

            elif nums[curr] == 2:
                nums[two], nums[curr] = nums[curr], nums[two]
                two -= 1

            else:
                curr += 1