class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        low = 0
        high = n1

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (n1 + n2 + 1) // 2 - partition_x

            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == n1 else nums1[partition_x]

            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n2 else nums2[partition_y]

            if max_left_x <= min_right_y and min_right_x >= max_left_y:
                if (n1 + n2) % 2 != 0:
                    return max(max_left_y, max_left_x)

                else:
                    return (max(max_left_y, max_left_x) + min(min_right_x, min_right_y)) / 2

            else:
                if max_left_x > min_right_y:
                    high = partition_x - 1

                else:
                    low = partition_x + 1
