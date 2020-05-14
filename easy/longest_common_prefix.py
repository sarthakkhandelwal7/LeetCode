class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        ans = ''
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                ans += x

            else:
                break

        return ans

