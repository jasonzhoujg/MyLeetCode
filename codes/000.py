
def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i1, i2 = 0, 0
    res = []
    while (i1 < len(nums1) and i2 < len(nums2)):
        if nums1[i1] == nums2[i2]:
            res.append(nums1[i1])
            last = nums1[i1]
            while (i1 < len(nums1) and last == nums1[i1]): i1 += 1
            while (i2 < len(nums2) and last == nums2[i2]): i2 += 1
        elif nums1[i1] >= nums2[i2]:
            last = nums2[i2]
            while (i2 < len(nums2) and last == nums2[i2]): i2 += 1
        else:
            last = nums1[i1]
            while (i1 < len(nums1) and last == nums1[i1]): i1 += 1

    return res

res = intersection([4,9,5],[9,4,9,8,4])
print(res)
