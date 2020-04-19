class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        num, sign, stack = 0, '+', []
        for i, char in enumerate(s):

            if char.isdigit():
                num = num * 10 + int(char)

            if (not char.isdigit() and not char.isspace()) or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    temp = stack.pop()
                    if temp // num < 0 and temp%num != 0:
                        stack.append(temp//num+1)
                    else:
                        stack.append(temp//num)
                sign = char
                num = 0
        return sum(stack)



if __name__ == '__main__':
    print(Solution().calculate("3+2*2"))