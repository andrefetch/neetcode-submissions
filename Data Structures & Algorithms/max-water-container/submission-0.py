class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2, maxArea = 0, len(heights) - 1, 0

        while p1 < p2:
            currArea = min(heights[p1], heights[p2]) * (p2 - p1)
            maxArea = max(maxArea, currArea)

            # have to move the smaller height ptr inwards
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1

        return maxArea