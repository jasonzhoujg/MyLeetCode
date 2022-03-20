class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        N =  len(s)
        flag = 1 
        for i in range(N):
            if not s[N-1-i] == ' ':
                l += 1
                flag = 0 
            elif (flag == 0):
                break
        return l