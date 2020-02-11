class Solution:
    def minDominoRotations(self, list1, list2) -> int:
        l1_count = [0] * 6
        l2_count = [0] * 6
        max1 = [0, 0]
        max2 = [0, 0]
        for i, j in enumerate(list1):
            if list2[i] != j:
                l1_count[j - 1] += 1
                l2_count[j - 1] += 1
            else:
                l1_count[j - 1] += 1

        for i in range(6):
            if l1_count[i - 1] > max1[1]:
                max1[1] = l1_count[i - 1]
                max1[0] = i

            if l2_count[i - 1] > max2[1]:
                max2[1] = l2_count[i - 1]
                max2[0] = i

        if len(list1) - max1[1] == 0:
            return 0

        elif min(len(list1) - max1[1], len(list1) - max2[1]) <= :
            return len(list1) - max1[1]

        elif len(list1) - max2[1] <= l1_count[max2[0] - 1]:
            return len(list1) - max2[1]

        else:
            return -1


if __name__ == '__main__':
    print(Solution().minDominoRotations([1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1]))