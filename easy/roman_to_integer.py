"""
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    Input: "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Input: "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(0, len(s) - 1):
            if symbols[s[i]] < symbols[s[i]]:
                num -= symbols[s[i]]

            else:
                num += symbols[s[i]]
        num += symbols[s[-1]]
        return num


if __name__ == '__main__':
    print(Solution().romanToInt("LVIIII"))