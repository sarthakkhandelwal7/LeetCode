class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''

        def find_string(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        for i in range(len(s)):
            # odd case, like "aba"
            tmp = find_string(i, i)
            if len(tmp) > len(result):
                result = tmp

            # even case, like "abba"
            tmp = find_string(i, i + 1)
            if len(tmp) > len(result):
                result = tmp

        return result


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
