import heapq

class Solution:
    def minMeetingRooms(self, intervals):

        if not intervals:
            return 0

        heap = []

        intervals.sort(key=lambda x: x[0])

        heapq.heappush(heap, intervals[0][1])
        rooms = 0

        for i in range(1, len(intervals)):
            print(i)
            print(heap)
            print()
            if heap[0] <= intervals[i][0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])

        return len(heap)


if __name__ == '__main__':
    print(Solution().minMeetingRooms([[6, 9], [11, 28], [1, 4], [5, 25], [20, 24], [24, 30], [32, 38]]))