class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s = ''
        carry = 0
        if len(num1) > len(num2):
            num2 = '0'*(len(num1) - len(num2)) + num2
        elif len(num1) < len(num2):
            num1 = '0'*(len(num2) - len(num1)) + num1
        while num1 or num2:
            x = num1[-1]
            num1 = num1[:-1]
            y = num2[-1]
            num2 = num2[:-1]
            temp_sum = int(x) + int(y) + carry
            carry, temp_sum = divmod(temp_sum, 10)
            s += str(temp_sum)
        if carry:
            s += str(carry)
        return s[::-1]


if __name__ == '__main__':
    print(Solution().addStrings('123', '247'))
    print(Solution().addStrings('1', '9'))
    print(Solution().addStrings('9', '99'))