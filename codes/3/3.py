class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        if len(s)==1: return 1
        p_l = 0
        p_r = 1
        s_max = s[p_l]
        res = 1
        while p_r<len(s):
            while p_r<len(s) and (not s[p_r] in s_max) : 
                s_max +=s[p_r]
                p_r+=1
            res = max(len(s_max),res)
            p_l+=1
            s_max = s[p_l]
            p_r=p_l+1
        return res
