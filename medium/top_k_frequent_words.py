import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        counts = Counter(words)
        heap = []
        for key, val in counts.items():
            heapq.heappush(heap, (-val, key))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


if __name__ == '__main__':
    print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
