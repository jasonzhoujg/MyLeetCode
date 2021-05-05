class Solution:
    def longestPalindrome(self, s: str) -> str:
        def IsPalindrome(nums):
            n = len(nums)
            if len(nums)//2 == len(nums)/2:
                return nums[:n//2]==nums[:n//2-1:-1]
            return nums[:n//2]==nums[:n//2:-1]
        s_max =s[0]
        l1 = 1
        if len(s)==2:
            if IsPalindrome(s):return s
            return s_max
        for n in range(1,len(s)):
            # for i in range(n-l1+1):
            #     if IsPalindrome(s[i:n+1]):
            #         s_max = s[i:n+1]
            #         l1 = len(s_max)
            #         break
            if IsPalindrome(s[n-l1:n+1]):
                s_max = s[n-l1:n+1]
                l1 = len(s_max)

            if n-l1-1>=0 and IsPalindrome(s[n-l1-1:n+1]):
                s_max = s[n-l1-1:n+1]
                l1 = len(s_max)

            
        return s_max
