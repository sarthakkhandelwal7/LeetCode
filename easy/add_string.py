class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s = ''
        carry = 0
        while num1 or num2:
            x = num1[-1]
            num1 = num1[:-1]
            y = num2[-1]
            num2 = num2[:-1]
            temp_sum = int(x) + int(y) + carry
            carry = 0
            if temp_sum > 9:
                carry = 1
                temp_sum -= 10
            s += str(temp_sum)
        return s[::-1]

if __name__ == '__main__':
    print(Solution().addStrings('123', '247'))