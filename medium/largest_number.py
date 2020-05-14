class Solution(str):
    # operator overloaing
    def __lt__(x, y):
        return x + y > y + x

    def largestNumber(self, nums):
        nums = ''.join(sorted(map(str, nums), key=Solution))
        return '0' if nums[0] == '0' else nums
