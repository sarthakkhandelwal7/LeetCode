class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if len(s) and not len(wordDict):
            return False

        def check(st: str) -> bool:
            if not st:
                return True
            word = ''
            for i, char in enumerate(st):
                word += char
                if word in wordDict:
                    check(st[i+1:])
                else:
                    word = ''
        return check(s)


if __name__ == '__main__':
    # print(Solution().wordBreak('aaaaaaa', ['aaaa', 'aaa']))
    # print(Solution().wordBreak("leetcode", ["leet", "code"]))
    print(Solution().wordBreak("goalspecial", ["go","goal","goals","special"]))