class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def helper(st: str, open_parentheses: chr, close_parentheses: chr):
            string_builder = ''
            balance = 0
            for i in st:
                if i == open_parentheses:
                    balance += 1

                elif i == close_parentheses:
                    if balance == 0:
                        continue

                    balance -= 1

                string_builder += i

            return string_builder
        s = helper(s, '(', ')')
        s = helper(s[::-1], ')', '(')
        return s[::-1]


if __name__ == '__main__':
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
    print(Solution().minRemoveToMakeValid(''))