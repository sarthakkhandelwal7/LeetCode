class Solution:
    def myAtoi(self, string: str) -> int:
        ans = ''
        for i in string:
            if not ans and i.isspace():
                continue

            elif i in '-+' and not ans:
                ans += i

            elif i.isdigit():
                ans += i

            else:
                break
        ans = int(ans) if not (len(ans) == 1 and ans[0] in '-+') and ans else 0
        if ans < -2**31:
            return -2**31

        elif ans > 2 ** 31 - 1:
            return 2**31 - 1

        else:
            return ans


if __name__ == '__main__':
    print(Solution().myAtoi('+'))
    print()
    print(Solution().myAtoi('--'))
    print()
    print(Solution().myAtoi('-124+25c'))
    print()
    print(Solution().myAtoi("-91283472332"))
    print()
    print(Solution().myAtoi("-01 3"))
    print()
    print(Solution().myAtoi("-0"))
    print()
    print(Solution().myAtoi("-5t0"))
    print()
    print(Solution().myAtoi("42i0"))
    print()
    print(Solution().myAtoi("   -42"))
    print()
    print(Solution().myAtoi("4193 with words"))
    print()
    print(Solution().myAtoi("words and 987"))
