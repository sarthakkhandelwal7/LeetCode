class Solution:
    def combinationSum(self, candidates, target: int):
        ans = []

        def helper(remaining_candidates, temp, sum):
            if sum == target:
                ans.append(temp)
                return

            elif remaining_candidates and sum + remaining_candidates[0] <= target:
                helper(remaining_candidates, temp + [remaining_candidates[0]], sum+remaining_candidates[0])
                helper(remaining_candidates[1:], temp, sum)

        candidates.sort()
        helper(candidates, [], 0)

        return ans


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 1, 4, 7], 7))
