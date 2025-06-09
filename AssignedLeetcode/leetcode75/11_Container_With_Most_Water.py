class Solution:
    def maxArea(self, height: List[int]) -> int:
        areaMax = 0
        size = len(height)
        left, right = 0, size - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            areaMax = max(area, areaMax)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return areaMax
