import heapq as h
from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = []
        ans = ""
        for k, v in Counter(S).items():
            h.heappush(heap, (-1 * v, k))
        while heap:
            temp, i = [], 0
            while i < 2:

                i += 1
                if heap:
                    x, y = h.heappop(heap)
                    if x + 1:
                        temp.append((x + 1, y))
                    ans += y

                elif not temp and not heap:
                    return ans

                else:
                    return ''

            for item in temp:
                h.heappush(heap, item)

        return ans


if __name__ == '__main__':
    print(Solution().reorganizeString("aab"))
    print(Solution().reorganizeString("aaabc"))