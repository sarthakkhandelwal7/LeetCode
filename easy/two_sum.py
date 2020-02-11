from collections import defaultdict
class Solution:
    def twoSum(self, nums, target: int):
        hash_map = defaultdict()
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [nums.index(target - num), i]
            else:
                hash_map[num] = target - num
            print(hash_map.items())

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))