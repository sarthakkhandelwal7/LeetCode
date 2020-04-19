class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if not numerator*denominator else ''
        if numerator == 0:
            return '0'
        remainder = []
        numerator, denominator = abs(numerator), abs(denominator)
        n, r = divmod(numerator, denominator)
        ans = sign + str(n)+'.'
        temp = ''
        while r not in remainder:
            remainder.append(r)
            r *= 10
            n, r = divmod(r, denominator)
            temp += str(n)

        index = remainder.index(r)
        ans += temp[:index]+'('+temp[index:]+')'
        return ans


if __name__ == '__main__':
    print(Solution().fractionToDecimal(2707, 990))