class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        p1 = 0
        p2 = 1
        while p2< len(nums) and nums[p1]==nums[p2]:p1,p2=p1+2,p2+2
        return nums[p1]
