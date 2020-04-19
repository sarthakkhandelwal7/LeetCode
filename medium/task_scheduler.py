from heapq import heappush, heappop
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        cycles, heap = 0, []
        for k, v in Counter(tasks).items():
            heappush(heap, (-1*v, k))

        while heap:
            temp, i = [], 0
            while i <= n:
                cycles += 1
                if heap:
                    x, y = heappop(heap)
                    if x != -1:
                        temp.append((x+1, y))

                if not heap and not temp:
                    break

                else:
                    i += 1

            for item in temp:
                heappush(heap, item)
        return cycles


if __name__ == '__main__':
    print(Solution().leastInterval(["A","A","B","B","C"], 3))
    print(Solution().leastInterval(["A", "A", "B", "B", "B", "A"], 0))
    print(Solution().leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
    print(Solution().leastInterval(["A","A","A","B","C","D","E"], 2))
