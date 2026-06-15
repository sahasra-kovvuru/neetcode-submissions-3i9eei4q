class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxwater = 0

        while left<right:
            width = right - left
            current = min(heights[left],heights[right])*(right-left)
            maxwater = max(maxwater, current)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxwater
      

            
        