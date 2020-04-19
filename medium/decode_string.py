class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ''
        for char in s:
            if char.isdigit():
                num += char

            elif char == '[':
                stack.append(['', int(num)])
                num = ''

            elif char == ']':
                st, n = stack.pop()
                stack[-1][0] += st*n

            else:
                stack[-1][0] += char

        return stack[0][0]
