
def threeSum(nums):
    nums.sort()
    second = 1
    third = len(nums) - 1
    out = []
    N = len(nums)
    for first in range(N-2):
        third = len(nums) - 1
        if first == 0 or (not nums[first-1] == nums[first]):
            for second in range(first+1,N-1):
                if third <= second: break
                if second == first+1 or (not nums[second-1] == nums[second]) :
                    while(nums[first]+nums[second]+nums[third]>0 and third > second):
                        third -= 1
                    if nums[first]+nums[second]+nums[third]==0 and third > second:
                        out.append([nums[first],nums[second],nums[third]])
    return out

print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))