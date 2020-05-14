class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def check_palindrome(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

                count += 1

        for i in range(len(s)):
            # For even cases:
            check_palindrome(i, i + 1)

            # For odd cases:
            check_palindrome(i, i)

        return count
