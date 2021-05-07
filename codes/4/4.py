class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)
        totallength = m+n
        k = totallength//2

        if totallength//2 == totallength/2:flag = 0
        else:flag =1

        if m == 0:
            if n // 2 == n / 2:
                return (nums2[n // 2] + nums2[n // 2 - 1]) / 2
            else:
                return nums2[n // 2]

        if n == 0:
            if m // 2 == m / 2:
                return (nums1[m // 2] + nums1[m // 2 - 1]) / 2
            else:
                return nums1[m // 2]

        

        while True:

            if k ==1:
                if flag ==1:
                    nums1 = nums1+nums2
                    nums1.sort()
                    return nums1[1]
                else:
                    nums1 = nums1 + nums2
                    nums1.sort()
                return (nums1[0] + nums1[1]) / 2


            if m == 0 :
                if flag==1:return nums2[k]
                else:return (nums2[k]+nums2[k-1])/2
            if n == 0: 
                if flag==1:return nums1[k]
                else:return (nums1[k]+nums1[k-1])/2
            

        
            if k//2-1 < m : 
                p1 = nums1[k//2-1]
            else:
                p1 = nums1[m-1]
            
            if k//2-1 < n : 
                p2 = nums2[k//2-1]
            else:
                p2 = nums2[n-1]
            
            if p1 <= p2 and k//2-1<m: nums1 = nums1[k//2:]
            elif p1 <= p2 and k//2-1>=m:nums1 = []

            if p2 < p1 and k//2-1<n: nums2 = nums2[k//2:]
            elif p2 < p1 and k//2-1>=n:nums2 = []

            m, n= len(nums1),len(nums2)
            k = k - (totallength-m-n)

            totallength = m+n
