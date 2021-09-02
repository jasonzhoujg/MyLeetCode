
def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if not haystack:
        return -1

    next_a = [0]
    now = 0

    for i in range(1, len(needle)):
        if needle[i] == needle[now]:
            now += 1
            next_a.append(now)
        elif now:
            now = next_a[now - 1]
            i -= 1
        else:
            next_a.append(0)
    k = 0
    p = 0
    N = len(needle)
    M = len(haystack)
    # ini = 0
    while p <= M - 1:
        if needle[k] == haystack[p] and k < N - 1:
            k += 1
            p += 1
        elif needle[k] == haystack[p] and k == N - 1:
            return p - N + 1
        else:
            p += next_a[k] + 1 - k
            k = 0


    return -1


print(strStr(haystack="mississippi",
             needle="issip"))