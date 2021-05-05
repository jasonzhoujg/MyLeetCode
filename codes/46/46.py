class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrace(nums,l):
            if not nums:
                res.append(l)
                return 
            for i in range(len(nums)):
                backtrace(nums[:i]+nums[i+1:],l+[nums[i]])

        backtrace(nums,[])
        return res
