class Solution:
    def __init__(self):
        self.memo = {}

    def make_decoded_string(self, index, s):
        if index == len(s):
            return 1

        if s[index] == '0':
            return 0

        if index == len(s)-1:
            return 1

        if index in self.memo:
            return self.memo[index]

        ans = self.make_decoded_string(index+1, s) + (self.make_decoded_string(index+2, s) if int(s[index:index+2]) <= 26 else 0)

        self.memo[index] = ans
        return ans

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.make_decoded_string(0, s)


if __name__ == '__main__':
    print(Solution().numDecodings("27"))