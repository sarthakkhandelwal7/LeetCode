from collections import defaultdict, deque


class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        pair_sum = defaultdict(deque)
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                pair_sum[nums[i] + nums[j]].append((i, j))

        for s in list(pair_sum.keys()):
            while pair_sum[s]:

                pair1 = pair_sum[s].popleft()
                for pair2 in pair_sum[target - s]:

                    if pair1[0] not in pair2 and pair1[1] not in pair2:
                        temp = []
                        for i in pair1 + pair2:
                            temp.append(nums[i])

                        ans.add(tuple(sorted(temp)))

            if s != target - s:
                del pair_sum[s]
                if target - s in pair_sum:
                    del pair_sum[target - s]

        return ans


if __name__ == '__main__':
    print(Solution().fourSum([-2, -1, 0, 0, 1, 2], 0))
    print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
