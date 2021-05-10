class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k> len(bloomDay):return -1
        # 首先找出和可能开花的天数
        SelectableDays = [j for j in bloomDay]
        # for i in bloomDay:
        #     if not i in SelectableDays:SelectableDays.append(i)

        #对待选天数排序
        SelectableDays.sort()
        start = 0
        end = len(SelectableDays)
        #开始二分查找
        while start < end:
            #中间点为P
            p = (end+start)//2

            day = SelectableDays[p]
            k_val = k
            m_val = m

            # 修改 m_val的值
            # 简单的想法，由于只有花期里的时间才会对结果产生影响，对花期先排序，利用二分查找寻找左边界

            for i in range(len(bloomDay)):
                if bloomDay[i] - day <= 0:
                    k_val -= 1
                    if k_val == 0:
                        m_val -= 1
                        k_val = k
                        continue
                    if i + 1 < len(bloomDay) and bloomDay[i + 1] -day<= 0: continue
                    k_val = k
            # 修改条件
            if m_val<=0:
                end = p
            else:start = p+1

        return SelectableDays[start]
