class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1

        next_a = [0]
        now = 0
        for i in range(1,len(needle)):
            if needle[i]==needle[now]:
                next_a.append(now+1)
            elif now:
                now = next_a[now-1]
                i -= 1
            else: 
                next_a.append(0)

        k = 0
        N = len(needle)
        while k+N<=len(haystack):
            for j in range(N):
                if k+j==len(haystack):
                    return -1
                if not haystack[k+j]==needle[j]:
                    k+=next_a[j]
                    break
                else:
                    if j == N-1:
                        return k
            k += 1
        return -1
