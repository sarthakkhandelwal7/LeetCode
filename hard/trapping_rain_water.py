class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        ans = 0
        n = len(height)
        left = 0 if height[0] > height[1] else 1
        right = 0

        for i in range(1, n):
            if not (left < i < right):
                right = i
                for j in range(i + 1, n):
                    right = right if height[right] > height[j] else j

            if height[i] > height[left]:
                left = i

            ans += min(height[left], height[right]) - height[i]

        return ans
