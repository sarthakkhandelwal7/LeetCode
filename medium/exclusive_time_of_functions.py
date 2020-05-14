"""
3
["0:start:0","1:start:3","2:start:3","2:end:4","1:end:5","0:end:6"]
"""


class Solution:
    def exclusiveTime(self, n: int, logs):
        stack = []
        ans = [0] * n
        thread = logs[0].split(':')
        stack.append(int(thread[0]))
        previous = int(thread[2])
        for i in range(1, len(logs)):
            thread = logs[i].split(':')
            thread = list(map(lambda x: int(x) if x.isdigit() else x, thread))
            if thread[1] == 'start':
                if stack:
                    ans[stack[-1]] += thread[-1] - previous

                stack.append(thread[0])
                previous = thread[-1]

            else:
                ans[stack[-1]] += thread[-1] - previous + 1
                stack.pop()
                previous = thread[-1]+1

        return ans


if __name__ == '__main__':
    print(Solution().exclusiveTime(3, ["0:start:0","1:start:2","1:end:5","2:start:6","2:end:9","0:end:12"]))
