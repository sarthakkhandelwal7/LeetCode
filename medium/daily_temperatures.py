class Solution:
    def dailyTemperatures(self, T):
        if not T:
            return []
        
        ans = [0]*len(T)
        stack = list()
        stack.append((T[0], 0))
        for i in range(1, len(T)):
            while stack and stack[-1][0] < T[i]:
                top = stack.pop()
                day = top[1]
                ans[day] = i-day

            else:
                stack.append((T[i], i))

        return ans


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))