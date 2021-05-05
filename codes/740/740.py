class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        res = [nums[0]]
        times = []
        cur = nums[0]
        j = 0

        for ele in nums:
            if cur == ele:j+=1
            else:
                times.append(j)
                j = 1
                cur = ele
                res.append(ele)
        times.append(j)

        if len(res)==1 : return res[0]*times[0]


        s1 = 0
        s2 = res[0]*times[0]

        for i in range(1,len(res)):
            if res[i]-1 == res[i-1]:total = max(s1+res[i]*times[i],s2)
            else: total = s2+res[i]*times[i]
            s1 = s2
            s2 = total
        return total
        # for i in range(nums):


        # return total
