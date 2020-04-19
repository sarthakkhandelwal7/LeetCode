from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        positions = defaultdict()
        start = end = 0
        max_length = 0
        for i in range(0, len(s)):
            if s[i] in positions and start <= positions[s[i]]:
                start = positions[s[i]] + 1

            else:
                max_length = max(i - start + 1, max_length)

            positions[s[i]] = i
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
