class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 先进行排序
        intervals.sort(key=lambda x:x[1])
        key_val = intervals[0][1]
        i =1
        for m in range(0,len(intervals)):
            if key_val<=intervals[m][0]:
                key_val = intervals[m][1]
                i+=1

            
        
        
        
        return len(intervals) - i
