class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxContainer = 0

        while l < r:
            curr = (r - l) * min(heights[l], heights[r])
            maxContainer = max(curr, maxContainer)

            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        
        return maxContainer