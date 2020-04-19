class Solution:
    @staticmethod
    def findMinDifference(time_points) -> int:
        time_points.sort()
        min_difference = float('inf')
        ptr1 = ptr2 = list(map(int, time_points[0].split(':')))
        for i in range(1, len(time_points)):

            ptr2 = list(map(int, time_points[i].split(':')))
            print(ptr2)
            difference = ptr2[0]*60 + ptr2[1] - (ptr1[0]*60 + ptr1[1])
            min_difference = min(min_difference, difference)
            ptr1 = ptr2

        difference = 24*60 - (ptr2[0]*60 + ptr2[1]) + (int(time_points[0].split(':')[0])*60 + int(time_points[0].split(':')[1]))
        print(difference)
        min_difference = min(min_difference, difference)

        return min_difference


if __name__ == '__main__':
    print(Solution().findMinDifference(["23:59","00:00"]))