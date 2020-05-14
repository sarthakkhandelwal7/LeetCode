class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result, _sum, diff = float('inf'), 0, None
        nums.sort()

        for i in range(0, len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            p = i + 1
            q = len(nums) - 1

            while p < q:
                _sum = nums[i] + nums[p] + nums[q]
                if _sum == target:
                    return _sum

                if abs(_sum - target) < abs(result - target):
                    result = _sum

                elif _sum < target:
                    while p < len(nums) - 1 and nums[p] == nums[p + 1]:
                        p += 1

                    p += 1

                else:
                    while q > 1 and nums[q] == nums[q - 1]:
                        q -= 1

                    q -= 1

        return result
