class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        cur = []
        i = 0

        while(i<len(arr)):
            last = arr[i]
            j = i
            while(i<len(arr) and last == arr[i]):i+=1
            cur.append(i-j)
        
        cur.sort()
        last = cur[0]
        for i in range(1,len(cur)):
            if cur[i]==last:return False
            last = cur[i]
        return True         