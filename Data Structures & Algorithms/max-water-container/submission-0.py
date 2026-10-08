class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxH = 0
        area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                if area < (j - i) * min(heights[i], heights[j]):
                    area = (j - i) * min(heights[i], heights[j])
        return area