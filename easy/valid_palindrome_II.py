class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(l, r):
            return all(s[l + j] == s[r - 1 - j] for j in range(r - l))

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] != s[high]:
                return helper(low, high) or helper(low + 1, high + 1)
            low += 1
            high -= 1
        return True
