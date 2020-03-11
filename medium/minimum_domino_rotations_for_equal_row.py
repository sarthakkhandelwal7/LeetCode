class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def helper(x) -> int:
            rotation_a = rotation_b = 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    return -1

                elif A[i] == x:
                    rotation_a += 1

                elif B[i] == x:
                    rotation_b += 1

            return min(rotation_a, rotation_b)


        rotation = helper(A[0])

        if rotation and A[0] == B[0]:
            return rotation

        else:
            return helper(B[0])


