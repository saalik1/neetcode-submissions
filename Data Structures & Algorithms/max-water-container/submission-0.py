class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        for i in range(0,len(heights)):
            for j in range(0,len(heights)):
                comp = min(heights[i],heights[j])*abs(i-j) 
                if comp > vol:
                    vol = comp
        return vol

        