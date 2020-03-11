class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)

            else:
                if not stack:
                    return False
                if i is ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif i is '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        print(stack)
        return True if not stack else False


if __name__ == '__main__':
    print(Solution().isValid(']'))