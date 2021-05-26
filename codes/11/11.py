class Solution:
    def maxArea(self, height: List[int]) -> int:
        p_left = 0
        p_right = len(height)-1
        res = 0
        while p_left<p_right:
            res = max((p_right-p_left)*min(height[p_left],height[p_right]),res)
            if height[p_left]<height[p_right]:
                p_left += 1
            else: p_right-=1
        return res
