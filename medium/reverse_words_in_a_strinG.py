class Solution:
    def reverseWords(self, s: str) -> str:
        word = False
        ans = temp = ''
        s = ' ' + s
        for i in range(len(s) - 1, -1, -1):
            if not s[i].isspace():
                word = True
                temp = s[i] + temp

            elif word:
                ans += temp + ' '
                word = False
                temp = ''

        return ans[:len(ans) - 1]
