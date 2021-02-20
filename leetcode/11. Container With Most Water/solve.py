class Solution:
    def calculate_area(self, start, end, height):
        top = min(height[start], height[end])
        length = end - start
        return length * top

    def maxArea(self, height: List[int]) -> int:
        top_area = -1

        left = 0
        right = len(height) - 1

        while left < right:

            area = self.calculate_area(left, right, height)

            top_area = max(top_area, area)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return top_area
