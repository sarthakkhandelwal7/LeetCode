class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_vol = 0
        while left < right:
            max_vol = max(max_vol, min(height[left], height[right])*(right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_vol