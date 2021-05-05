class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:return 0
        if len(nums) == 1:return nums[0]
        M0 = 0
        M1 = nums[0]
        res = 0
        for i in range(1,len(nums)):
            res = max(M0+nums[i],M1)
            M0 = M1
            M1 = res
        
        return res
